from django.db import models

class InterviewModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    des =  models.CharField(max_length=255, blank=True, null=True)
    resume =  models.CharField(max_length=255, blank=True, null=True)
    accepted = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()


    def __str__(self):
        return self.title
