from django_extensions.management.jobs import BaseJob, DailyJob

class Job(DailyJob):
    help = "The job used to check the star list."

    def execute(self):
        # executing empty sample job
        
        pass
