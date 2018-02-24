from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

#类似于controller返回视图
def index(request):
	return render(request,'learning_logs/index.html')
	

#定义topic类
def topics(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topics':topics}
	return render(request,'learning_logs/topics.html',context)
	

def topic(request,topic_id):
	#查询
	topic = Topic.objects.get(id=topic_id)
	#'-date_added'为降序排列
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic,'entries':entries}
	return render(request,'learning_logs/topic.html',context)
	
	
def new_topic(request):
	if request.method != 'POST':
		#若请求非POST,则创建新表单
		form = TopicForm()
	else:
		#若请求为POST,验证后储存表单
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			#数据存储后重定向至topics页面
			return HttpResponseRedirect(reverse('learning_logs:topics'))
			
	context = {'form':form}
	return render(request,'learning_logs/new_topic.html',context)
	
	
def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	
	if request.method != 'POST':
		form = EntryForm()
	else:
		#注意data = request.POST
		form = EntryForm(data=request.POST)
		if form.is_valid():
			#commit = False 创建但不储存
			new_entry = form.save(commit = False)
			#设置外键
			new_entry.topic = topic
			new_entry.save()
			#重定向
			return HttpResponseRedirect(reverse('learning_logs:topic',args = [topic_id]))
			
	context = {'topic':topic,'form':form}
	return render(request,'learning_logs/new_entry.html',context)


	
def edit_entry(request,entry_id):
	
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	
	if request.method != 'POST':
		form = EntryForm(instance = entry)
		
	else:
		form = EntryForm(instance = entry, data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args = [topic.id]))
			
	context = {'entry':entry, 'topic':topic, 'form':form}
	return render(request,'learning_logs/edit_entry.html',context)
	
