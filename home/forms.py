from django import forms
from .models import Profile, BlogPost
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'facebook', 'instagram', 'linkedin', 'image')
        
       
class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(attrs={'placeholder': 'Digite o conteúdo aqui...'}))

    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título do Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Coloque a palavra chave do post sem espaço e separado com hífen'}),
        }