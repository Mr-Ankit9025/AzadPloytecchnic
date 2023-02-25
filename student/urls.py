from django.urls import path
from . import views
urlpatterns = [
  path('home/',views.home),
  path('index/',views.index),
  path('aboutus/',views.aboutus),
  path('courses/',views.courses),
  path('placement/',views.placement),
  path('register/',views.register),
  path('contact/',views.contact),
  path('infra/',views.infra),
  path('gallery/',views.gallery),
  path('video/',views.vdogallery),
  path('details/',views.vdodetails),
  path('faculty/',views.faculty),
  path('teachersDetail/',views.teachersDetail),
  ]