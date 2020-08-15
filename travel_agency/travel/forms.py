from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.CharField(widget=forms.EmailInput)
    message = forms.CharField(widget=forms.Textarea)