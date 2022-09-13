from tkinter.ttk import Style
from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator



# EVERY letters to lowercase
class Lowercase(forms.CharField):
    def to_python(self,value):
        return value.lower()
        
# EVERY letters to uppercase
class Uppercase(forms.CharField):
    def to_python(self,value):
        return value.upper()
        
        
class CandidateForm(forms.ModelForm):            
        
    # VALIDATIONS
    firstname = forms.CharField(
        label='First Name', min_length=3,max_length=50,
        validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message="Only letters is allowed!")], 
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
   

    lastname = forms.CharField(
        label='Last Name', min_length=3,max_length=50,
        validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message="Only letters is allowed!")], 
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    
    # ESTO HACE QUE SIEMPRE EN EL BACKEND, SE GRABE EN MAYUSCULAS, AUN SI EN EL FRONTEND SE INGRESO MINUSCULA
    job = Uppercase(
        label='Job Code', min_length=5,max_length=5, 
        widget=forms.TextInput(attrs={'placeholder': 'Example: FR-22'}))
    

    email = Lowercase(
        label='Email address', min_length=8,max_length=50,
        validators= [RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
        message="Put a valid address ")], 
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    
    # Method de validacion 1
    age = forms.CharField(
        label='Your Age', min_length=2,max_length=3,
        validators= [RegexValidator(r'^[0-9]*$', 
        message="Only numbers is allowed!")], 
        widget=forms.TextInput(attrs={'placeholder': 'Age'}))
    
    
    experience = forms.BooleanField   (label= "I have experiencie!")  #  alta requerid=false
    
    message = forms.CharField(
        label='About you', min_length=10,max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Talk a little about you', 'rows':4}
            )
        )
    
    # file upload
    file = forms.FileField(
        required=True, 
        widget=forms.ClearableFileInput(
            attrs={'style':'font-size 13px'}
        )
    )
    

    # method 1
    
    GENDER=[('F', 'Female'),('M', 'Male')]
    gender = forms.CharField(label="Gender", widget=forms.RadioSelect(choices=GENDER))
   
    class Meta:
        model=Candidate
        
        exclude = ['created_at', 'Situation']
        
        SALARY = {
            ('','Salary expectation (month)'),
            ('Between ($3000 and $4000)','Between ($3000 and $4000)'),
            ('Between ($4000 and $5000)','Between ($4000 and $5000)'),
            ('Between ($5000 and $7000)','Between ($5000 and $7000)'),
            ('Between ($7000 and $10000)','Between ($7000 and $10000)'),    
        }
        
        GENDER=[('F', 'Female'),('M', 'Male')]
        # OUTSIDE WIDGET
        widgets = {
            # Phone
            'phone': forms.TextInput(
                attrs={
                    'style':'font-size: 13px',  # CSS
                    'placeholder':'Phone',
                    'data-mask': '(00000) 00-0000' 
                }
            ),
            # Salary
            'salary': forms.Select(
                choices=SALARY,
                attrs={
                    'class':'form-control',  # Boostrap inside the forms.py 
                }
                
            ) ,
            # GENDER method 2
            #'gender': forms.RadioSelect (choices= GENDER , attrs={'class':'check-control'},  # Boostrap inside the forms.py                 
            'smoker': forms.RadioSelect(choices=SMOKER, attrs={'class':'btn-check'}),  # Boostrap inside the forms.py                 

        }

    # SUPER FUNCTION
    # LA SUPER FUNCION, TIENE PODER SOBRE EL RESTRO DE LAS DEFINICIONES, TANTO EN EL FORM COMO EN EL MODEL
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        
        # ------------- CONTROL PANEL (OPCIONAL METHOD TO CONTROL)  ------------------
        # input disabled
        #self.fields["experience"].disabled=False # True
        
        # input readonly
        #self.fields["email"].widget.attrs.update({'readonly':'readonly'})
        
        
        # ------------- SELECT OPTION ------------------
        #self.fields["personality"].choices = [('',"Select a personality"),] + list(self.fields["personality"].choices)[1:]
        
        
        # ------------- WIDGET CONTROL  ------------------
        
        # ------------- READ ONLY  ------------------
        #readonly = ["firstname", "lastname", "job"]
        #for field in readonly:
        #    self.fields[field].widget.attrs['readonly']='True'
