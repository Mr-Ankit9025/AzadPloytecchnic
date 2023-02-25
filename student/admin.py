from django.contrib import admin
from .models import *
# Register your models here.
class contactInfoAdmin(admin.ModelAdmin):
  list_display = ('Name','Email','Mobile','Msg')
admin.site.register(contactInfo,contactInfoAdmin)  


class stuplacementAdmin(admin.ModelAdmin):
  list_display=('id','name','course','branch','stupic','designation','pyear','cpic','rdate','cname','pcity')
admin.site.register(stuplacement,stuplacementAdmin)
class ugalleryAdmin(admin.ModelAdmin):
  list_display = ('id','gdes','picture')
admin.site.register(ugallery,ugalleryAdmin)  


class uregisterAdmin(admin.ModelAdmin):
  list_display = ('Rollno','Name','Smobile','Course','Year','Date','Date','Gmobile','Image')
admin.site.register(uregister,uregisterAdmin)  

class cityAdmin(admin.ModelAdmin):
  list_display=('id','cname','cdate')
admin.site.register(city,cityAdmin)


class companyAdmin(admin.ModelAdmin):
  list_display=('id','cname','clogo')
admin.site.register(company,companyAdmin)


class vgalleryAdmin(admin.ModelAdmin):
  list_display=('id','vlink','vdes','vtitle','vdate')
admin.site.register(vgallery,vgalleryAdmin)


class mycourseAdmin(admin.ModelAdmin):
  list_display=('id','cname','branch','seats','hod','duration','cpic','sdate','eligibility','fee','hodpic')
admin.site.register(mycourse,mycourseAdmin)

class infrastructureAdmin(admin.ModelAdmin):
  list_display=('id','ititle','ipic')
admin.site.register(infrastructure,infrastructureAdmin)


class teacherAdmin(admin.ModelAdmin):
  list_display=('id','tname','tbranch','tpic')
admin.site.register(teacher,teacherAdmin)

class teacherDetailAdmin(admin.ModelAdmin):
  list_display=('id','teacherName','teacherPosition','teacherPhoto','aboutTeacher')
admin.site.register(teacherDetail,teacherDetailAdmin)