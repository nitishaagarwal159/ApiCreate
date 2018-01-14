"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from polls import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
url(r'^employees/',views.employeeList.as_view()), #to view and post user
url(r'^em/',views.emailList.as_view()),   #to view and post uploaded emails
url(r'^email/(?P<employ>.+)/$',views.emailLi.as_view()),  #to view uploaded emails for a particular user
url(r'^ph/',views.phoneList.as_view()),   #to view and post uploaded contact numbers
url(r'^no/(?P<contactno>.+)/$',views.phoneLi.as_view()),    #to view uploaded phone numbers for a particular user
url(r'^rec/',views.receiveList.as_view()),
url(r'^rcvreq/(?P<req>.+)/$',views.receiveLi.as_view()),
url(r'^lik/',views.likesList.as_view()),
url(r'^postlike/(?P<idofpost>.+)/$',views.numoflikes.as_view()),  #lists number of likes on post
url(r'^sha/',views.shareList.as_view()),
url(r'^postshare/(?P<idofpost>.+)/$',views.numofshares.as_view()), #lists number of shares on post
]
