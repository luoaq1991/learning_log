from django import forms

from .models import Topic , Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text':''}
		
class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text':''}
		#组建widgets, 选用文本区域,设置行高为80
		widgets = {'text': forms.Textarea(attrs={'cols':80})}

