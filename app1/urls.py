from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from firstpage import views as views1
from register import views as views2
from help import views as views3


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views1.index,name='Homepage'),
    url('predict',views2.predict,name='predict'),
    url('register',views2.index,name='register'),
    url('help',views3.index,name='help')
]
