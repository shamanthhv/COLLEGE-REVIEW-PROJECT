from django import forms

class MyForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    your_review = forms.CharField(label='Your review',max_length=50)
    #All my attributes here


