from django.db import models
from django.utils.timezone import now
from django.forms import ModelForm

class Deal(models.Model):
    img_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200,primary_key=True)
    replay_count = models.IntegerField()
    up_count = models.IntegerField()
    cdate = models.DateTimeField(default=now)
    
    def __str__(self):
        return f'{self.title}-{self.replay_count}-{self.up_count}--{self.cdate}'

class Form(ModelForm):
    class Meta:
        model= Deal
        fields = ['img_url','title','link','replay_count','up_count','cdate']