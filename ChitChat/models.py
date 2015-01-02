from django.db import models
import datetime
# Create your models here.
class Message(models.Model):
	user=models.CharField(max_length=30)
	text=models.CharField(max_length=200)
	posted=models.DateTimeField('Date Posted',default=datetime.datetime.now())
	parent=models.ForeignKey('self',default=None,blank=True,null=True)
	linked=models.IntegerField(default=0)
	replies=models.IntegerField(default=0)
	favorites=models.IntegerField(default=0)
	topics=models.CharField(max_length=25,default=None,blank=True,null=True)
	