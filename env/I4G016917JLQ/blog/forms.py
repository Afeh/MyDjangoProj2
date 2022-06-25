from django import forms
from .models import Post

#creating a form
class PostForm(forms.ModelForm):

#Create meta class
    class Meta:

        #Specify model to be used
        model = Post

        fields = [
            "title",
            "description",
        ]

