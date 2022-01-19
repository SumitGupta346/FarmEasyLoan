"""crop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url

from bank import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('reginsert',views.reginsert,name="reginsert"),
    url('newbankcrop', views.newbankcrop, name="newbankcrop"),

    url('showapplied', views.showapplied, name="showapplied"),
url('homeshowschemes',views.homeshowschemes,name="homeshowschemes"),
    url(r'^$', views.index, name='index'),
    url('bankfarmerview', views.bankfarmerview, name="bankfarmerview"),
url('viewcroploan',views.viewcroploan,name="viewcroploan"),
url('insetuploaddocument',views.insetuploaddocument,name="insetuploaddocument"),

url('viewmeetingdetailsfarmer',views.viewmeetingdetailsfarmer,name="viewmeetingdetailsfarmer"),
url('showschemes',views.showschemes,name="showschemes"),
    url('changepass', views.changepass, name="changepass"),
    url('logcheck',views.logcheck,name="logcheck"),
    url('showfarmer',views.showfarmer,name='showfarmer'),
url('viewcroploanstatus',views.viewcroploanstatus,name='viewcroploanstatus'),
url('insertgovtschemes',views.insertgovtschemes,name='insertgovtschemes'),
url('insertbankdetails',views.insertbankdetails,name='insertbankdetails'),

url('viewmeetingdetails',views.viewmeetingdetails,name='viewmeetingdetails'),
url('insertmeetingdetails',views.insertmeetingdetails,name='insertmeetingdetails'),
url('farmerreginsert',views.farmerreginsert,name='farmerreginsert'),

url('viewcroploanstatusfarmern',views.viewcroploanstatusfarmern,name='viewcroploanstatusfarmern'),

url('insertaadhardetails',views.insertaadhardetails,name='insertaadhardetails'),
url('updateshowschemes',views.updateshowschemes,name='updateshowschemes'),
url('newstatus',views.newstatus,name='newstatus'),
url('adminupdates',views.adminupdates,name='adminupdates'),
url('newstatusadmin',views.newstatusadmin,name='newstatusadmin'),
url('adminloanstatus',views.adminloanstatus,name='adminloanstatus'),
url('editscheme',views.editscheme,name='editscheme'),
url('viewcroploanbank',views.viewcroploanbank,name='viewcroploanbank'),
url('insertcroploanstatus',views.insertcroploanstatus,name='insertcroploanstatus'),
    # delete urls
url('delcroploanstatus/(?P<pk>\d+)/$', views.delcroploanstatus, name='delcroploanstatus'),
url('editadminschemes/(?P<pk>\d+)/$', views.editadminschemes, name='editadminschemes'),
url('insertcroploan/(?P<pk>\d+)/$', views.insertcroploan, name='insertcroploan'),

url('contact',views.contact,name='contact'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)