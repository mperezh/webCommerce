from django import forms

#Create your forms here
class ContactForm(forms.Form):
    sender = forms.EmailField(required=False)
    topic = forms.CharField()
    message = forms.CharField()