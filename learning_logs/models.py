from django.db import models

# Create your models here.

class Topic(models.Model):
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	
	def __str__(self):
		return self.text
		
		
#具体指示,实则为创建数据库的实体类
class Entry(models.Model):
	
	#确定外键
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
	
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)
	
	class Meta:
		verbose_name_plural = 'entries'
		
	def __str__(self):
		return self.text[:50] + "..."
	
