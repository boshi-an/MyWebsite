from django.shortcuts import render
from SiteView.models import Star
from django.http import JsonResponse
from django.conf import settings

# Create your views here.

# If a new website is up, the website will send a request to the parent server,
# the parent server will add a star on its page
def AddStar(request) :

    website = request.GET.get('website')

    if website is not None :

        print("SiteView: adding site {}".format(website))

        new_star = Star.objects.get_or_create(link=website)
        new_star.save()

        data = {'status': 'success'}
    
    else :

        data = {'status': 'failed'}

    return JsonResponse(data, safe=False)

# If the parent server wants to check if a website is up,
# the parent server will send a request to the child server
# and the child server will return a code.
# The code is the only identifier of whether a website belongs to a tree
# A website with changed code will become the root of a new tree.
def Knock(request) :

    data = {'key': settings.PASSCODE}

    print("SiteView: parent {} knocking".format(settings.PARENT_URL))

    return JsonResponse(data, safe=False)