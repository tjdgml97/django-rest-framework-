from django import forms
from . import models


# //모델 전체를 처리할때 - 장고가 폼을 처리할때 

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = models.Post
#         fields = "__all__"

class PostForm(forms.Form) :
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea())

class PostModelForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = ['title','content']
        #모델을 선택해서 만들수있음 . 

