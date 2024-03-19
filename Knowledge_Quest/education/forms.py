 
from django import forms 
from .models import FeedBack
 
class Feedbackform(forms.ModelForm): 
    class Meta: 
        model = FeedBack
        fields = ['Name', 'Email', 'Feedback'] 



