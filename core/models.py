from django.db import models
from django.conf import settings

# Postings model, stores
# title of the posting
# organization creating the posting
# country
# region = state/province
# city
# hours of the posting
# description of the posting
class Posting(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    region = models.CharField(max_length=25)
    city = models.CharField(max_length=50)
    hours = models.CharField(max_length=300)
    description = models.TextField(max_length=2000)

# Applicant model, stores
# applicant, person applying
# country of the person applying
# region of the person applying
# city/town of the person applying
# message of the applicant
# status of the application
class Applications(models.Model):
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=2)
    region = models.CharField(max_length=25)
    city = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    # PENDING
    # ACCEPTED
    # DENIED
    status = models.CharField(max_length=8)