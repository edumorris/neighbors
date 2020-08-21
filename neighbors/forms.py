from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        exclude=['user']

class PostForm(forms.ModelForm):
    class Meta:
        fields =['title', 'content', 'image']