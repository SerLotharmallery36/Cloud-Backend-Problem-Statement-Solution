from django.db import models

# Create your models here.

class Schools(models.Model):
	#id = 	   models.AutoField(primary_key=True)
	REGIONID = models.PositiveSmallIntegerField()
	school =   models.CharField(max_length=100, primary_key=True)
	email =	   models.EmailField()
	principal =models.CharField(max_length=50)
	phone =	   models.CharField(max_length=8)
	address2 = models.CharField(max_length=100)

class Books(models.Model):
	#id = 	   models.AutoField(primary_key=True)
	Title = models.CharField(max_length=100,primary_key=True)
	Author_Name = models.CharField(max_length=50,blank=True)
	Date_Of_Publication = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
	Number_Of_Pages = models.PositiveIntegerField()



class Students(models.Model):
	#id = 		 models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=20)
	last_name =  models.CharField(max_length=20)
	email = 	 models.EmailField()
	gender =	 models.CharField(max_length=6,blank=True)
	school = 	 models.CharField(max_length=100)
	books = 	 models.CharField(max_length=100)
	school = 	 models.ForeignKey(Schools, on_delete=models.CASCADE,blank=True)
	books = 	 models.ForeignKey(Books, on_delete=models.CASCADE,blank=True)








