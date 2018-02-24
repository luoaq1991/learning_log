#user 中的urls
from django.urls import re_path
from django.contrib.auth.views import login

from . import views

app_name = 'users'

urlpatterns = [
	#登录页面
	re_path('^login/$', login, {'template_name':'users/login.html'}, name = 'login'),
	

]
