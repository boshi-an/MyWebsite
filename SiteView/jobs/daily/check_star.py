from django_extensions.management.jobs import BaseJob, DailyJob
from SiteView.models import Star
from SiteView.utils.network import Ping
import requests
from django.conf import settings
from django.contrib.sites.models import Site

class CheckStar(DailyJob):
    help = "The job used to check the star list."

    def execute(self):
        # executing empty sample job

        websites = Star.objects.all()

        for item in websites :
            if not Ping(item.link) :
                print("Check-star: deleting {} for unable to access".format(item.link))
                item.delete()
            else :
                response = requests.get(settings.PARENT_URL + "/knock/")
                json_response = response.json()
                if 'key' not in json_response :
                    print("Check-star: deleting {} for no key".format(item.link))
                    item.delete()
                elif json_response['key'] != settings.PASSCODE :
                    print("Check-star: deleting {} for wrong key".format(item.link))
                    item.delete()
        
        # add a star to parent site
        response = requests.get(settings.PARENT_URL + '/addstar/', data={'website': Site.objects.get_current().domain})