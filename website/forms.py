from django import forms 
from website.models import News
from captcha.fields import CaptchaField

class NewsForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = News 
        fields = '__all__'