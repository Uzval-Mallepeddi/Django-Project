from myportfolio.models import ContactInfo, NewProject
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = "__all__"
        labels = {
            'firstname': '',
            'lastname': '',
            'email': '',
            'phone': '',
            'comments': ''
        }
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'First name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.NumberInput(attrs={'minlength':10, 'maxlength':15, 'placeholder': 'Phone number', 'type': 'number'}),
            'comments': forms.Textarea(attrs={'cols':40, 'rows':10,'placeholder': 'Comments'})
        }

class myProjectsForm(forms.ModelForm):
    class Meta:
        model = NewProject
        fields = '__all__'
        widgets = {
            'comments': forms.Textarea(attrs = {'cols':40, 'rows': 10})
        }