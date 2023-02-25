from django.shortcuts import render
from .models import * 
from django.db.models import Q
# Create your views here.
def index(request):
  return render(request,'diploma/index.html')


def home(request):
  data=teacherDetail.objects.all().order_by('id')
  md={"tdetail": data}
  return render(request,'diploma/home.html',md)


def aboutus(request):
  return render(request,'diploma/aboutus.html')



def faculty(request):
  data = teacher.objects.all().order_by('-id')
  md={"fdata": data}
  return render(request,'diploma/faculty.html',md)



def courses(request):
  if request.method=="GET":
    a=request.GET.get('search')
    if a is not None:
      mycourse.objects.all().filter(Q(cname__icontains=a) | Q(branch__icontains=a) | Q(hod__icontains=a) | Q(duration__icontains=a) |Q(eligibility__icontains=a))
  x=mycourse.objects.all().order_by('-id')
  md={"cdata":x}
  return render(request,'diploma/courses.html',md)



def placement(request):
  x=stuplacement.objects.all().order_by('-id')
  md={"place":x}
  return render(request,'diploma/ourplacement.html',md)


def register(request):
  s=False
  if request.method == "POST":
    a=request.POST.get('name')
    b=request.POST.get('smob')
    c=request.POST.get('select')
    d=request.POST.get('byear')
    e=request.POST.get('date')
    f=request.POST.get('email')
    g=request.POST.get('gmob')
    h=request.POST.get('img')
    i=request.POST.get('rno')
    uregister(Name=a, Smobile=b,Course=c,Year=d,Date=e,Email=f,Gmobile=g,Image=h,Rollno=i).save()
    s=True
  return render(request,'diploma/register.html', context={"status":s})
def contact(request):
  s=False
  if request.method == "POST":
    a=request.POST.get('name')
    b=request.POST.get('email')
    c=request.POST.get('mob')
    d=request.POST.get('msg')
    contactInfo(Name=a,Email=b,Mobile=c,Msg=d).save()
    s=True
  return render(request,'diploma/contact.html', context = {"msg" : s})
def login(request):
  return render(request,'diploma/login.html')
def infra(request):
  data=infrastructure.objects.all().order_by('id')
  md={"idata":data}
  return render(request,'diploma/infra.html',md)
def gallery(request):
  x=ugallery.objects.all()
  mydict={"data":x}
  return render(request,'diploma/gallery.html', context=mydict)
  
def vdogallery(request):
  data=vgallery.objects.all().order_by('-id')
  mydic={"vdata":data}
  return render(request,'diploma/video.html',mydic)
  
def vdodetails(request):
  y=request.GET.get('msg')
  x=vgallery.objects.all().filter(id=y)
  myd={"vdata":x}
  return render(request,'diploma/details.html',myd)
  
def teachersDetail(request):
  y=request.GET.get('msg')
  x=teacherDetail.objects.all().filter(id=y)
  myd={"tdetail":x}
  return render(request,'diploma/teachersDetail.html',myd)