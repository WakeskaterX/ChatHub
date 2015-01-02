from django import forms

class CreateForm(forms.Form):
	user = forms.CharField(label='User Name',max_length=30,min_length=3)
	message = forms.CharField(label='Message',widget=forms.Textarea,max_length=200)
	parent = forms.IntegerField(label='Parent ID',required=False)
	
class SearchForm(forms.Form):
	search=forms.CharField(label='Search Text',max_length=30)