from django.db import models

# Create your models here.
class contactInfo(models.Model):
  Name = models.CharField(max_length=100)
  Email=models.CharField(max_length=30)
  Mobile=models.CharField(max_length=20)
  Msg=models.TextField()
  def __str__(self):
    return self.Name
    
    
class ugallery(models.Model):
  gdes = models.CharField(max_length=200)
  picture = models.ImageField(upload_to='static/gallery/', default="")
  
class uregister(models.Model):
  
  Name = models.CharField(max_length=100)
  Rollno = models.CharField(max_length=100,primary_key=True)
  Smobile = models.CharField(max_length=10)
  Course=models.CharField(max_length=20)
  Year=models.CharField(max_length=10)
  Date=models.CharField(max_length=50)
  Email=models.CharField(max_length=200)
  Gmobile=models.CharField(max_length=20)
  Image=models.ImageField(upload_to='static/pimage/',null=True)
  def __str__(self):
    return self.Name
    
class city(models.Model):
  cname =models.CharField(max_length=30)
  cdate =models.DateField()
  
class company(models.Model):
  cname = models.CharField(max_length=200)
  clogo = models.ImageField(upload_to='static/company')
  def __str__(self):
    return self.cname
  
class stuplacement(models.Model):
  name= models.CharField(max_length=100)
  course= models.CharField(max_length=100)
  branch= models.CharField(max_length=100)
  stupic= models.ImageField(upload_to='static/profile',null=True)
  designation=models.CharField(max_length=50)
  pyear=models.CharField(max_length=50)
  cpic=models.ImageField(upload_to='static/company')
  rdate=models.DateField()
  cname=models.ForeignKey(company,on_delete=models.CASCADE,null=True)
  pcity=models.CharField(max_length=60)
  
  ##############################################

class vgallery(models.Model):
  vlink=models.TextField()
  vdes=models.TextField()
  vtitle=models.CharField(max_length=200)
  vdate=models.DateField()

class mycourse(models.Model):
  cname = models.CharField(max_length=50)
  branch=models.CharField(max_length=30)
  seats=models.CharField(max_length=50)
  hod=models.CharField(max_length=50)
  duration=models.CharField(max_length=50)
  cpic=models.ImageField(upload_to='static/course/',default="")
  hodpic=models.ImageField(upload_to='static/hod/',default="")
  sdate=models.CharField(max_length=100)
  eligibility=models.CharField(max_length=50)
  fee=models.CharField(max_length=200)
   
   
class infrastructure(models.Model):
  ititle=models.CharField(max_length=40)
  ipic=models.ImageField(upload_to='static/infra',null=True)
  
  
class teacher(models.Model):
  tname=models.CharField(max_length=50)
  tbranch=models.CharField(max_length=50)
  tpic=models.ImageField(upload_to='static/faculty', null=True)
  
  
  
class teacherDetail(models.Model):
  teacherName=models.CharField(max_length=50)
  teacherPosition=models.CharField(max_length=50)
  teacherPhoto=models.ImageField(upload_to='static/teacherPhoto',null=True)
  aboutTeacher=models.TextField()