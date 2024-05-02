from django import forms 
from website.models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News 
        fields = '__all__'