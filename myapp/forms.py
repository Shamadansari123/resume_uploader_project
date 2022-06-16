from cProfile import label
from tkinter import Widget
from django import forms
from myapp.models import Resume

GENDER_CHOICE=(
    ("Male","Male"),
    ("Female","Female"),
)

Job_location_choices=(
    ("New Delhi","New Delhi"),
    ("Mumbai","Mumbai"),
    ("Bangalore","Bangalore"),
    ("Lucknow","Lucknow"),
    ("Pune","Pune"),
)

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label="Preffered Job Location",choices=Job_location_choices,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['name','dob','gender','locality','city','job_city','pin','email','mobile','state','profile_image','file']
        labels={"name":"Full Name","dob":"Date of Birth","profile_image":"Profile Image","mobile":"Mobile","pin":"Pin","email":"Email ID","file":"Document"}
        widgets={
            'name':forms.TextInput(attrs={"class":"form-control"}),
            'dob':forms.DateInput(attrs={"class":"form-control","id":"datepicker"}),
            'locality':forms.TextInput(attrs={"class":"form-control"}),
            'city':forms.TextInput(attrs={"class":"form-control"}),
            'pin':forms.NumberInput(attrs={"class":"form-control"}),
            'state':forms.Select(attrs={"class":"form-control"}),
            'mobile':forms.NumberInput(attrs={"class":"form-control"}),
            'email':forms.EmailInput(attrs={"class":"form-control"}),
        }