from django import forms 
from website.models import News
# from captcha.fields import CaptchaField

class NewsForm(forms.ModelForm):

    class Meta:
        model = News 
        fields = '__all__'