import datetime
from djongo import models





class Option(models.Model):
	_id = models.ObjectIdField(editable = False)
	# id = models.AutoField()
	option_char = models.CharField(verbose_name="option_char", max_length=25)
	option_text = models.CharField(verbose_name="option_text",max_length=225)
	is_right_answer = models.BooleanField(default=False)


	class Meta:

		abstract = True




class Question(models.Model):
	_id = models.ObjectIdField(editable = False)
	created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
	question_text = models.CharField(verbose_name="Question body", max_length=255)
	option = models.ArrayField(model_container=Option,blank=True, null=True,verbose_name = "options")

	class Meta:

		abstract = True




# class Answers(models.Model):
# 	_id = models.ObjectIdField(editable = False)
# 	author = models.IntegerField(blank=True, null=True)
# 	group = models.IntegerField(blank=True,null=False)
# 	option = models.ForeignKey(Option,null=True,blank=True,on_delete = models.CASCADE)
# 	answered_at = models.DateTimeField(
# 		default=datetime.datetime.now, editable=False,
# 	)
# 	duration = models.IntegerField(blank=True,null=False)
# 	objects = models.DjongoManager()



class Test(models.Model):
	_id = models.ObjectIdField(editable = False)
	created_at = models.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )
	author = models.IntegerField(blank=True, null=True)
	title = models.CharField(max_length=255,blank=True)
	subject = models.IntegerField(blank=True , null=True)
	strart_date = models.DateTimeField(
		verbose_name="strart date",
    	editable=True,
		null=True,
	)
	duration =models.IntegerField(default = 45 ,blank = True, verbose_name="Duration Time in minutes") 
	question = models.ArrayField(model_container=Question,blank=True, null=True)
	assigned_for_group = models.IntegerField(blank=True, null=True)
	objects = models.DjongoManager()

		# class Meta:

		# 	abstract = True

# Create your models here.

