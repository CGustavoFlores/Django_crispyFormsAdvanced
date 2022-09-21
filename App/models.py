from email.policy import default
from operator import truediv
from random import choices
from django.db import models
from multiselectfield import MultiSelectField

SITUATION = {
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Disapproved','Disapproved')
}

PERSONALITY = {
    ('','Select a personality'),
    ('I am outgoing','I am outgoing'),
    ('I am sociable','I am sociable'),
    ('I am antisocial','I am antisocial'),
    ('I am discreet','I am discreet'),
    ('I am serious','I am serious')
}

SMOKER = {
    ('1','Yes'),
    ('2','No'),
}

# Multiple Chekboxes
FRAMEWORKS = {
    ('Laravel','Laravel'),
    ('Angular','Angular'),
    ('Django','Django'),
    ('FastAPI','FastAPI'),
    ('Vue','Vue'),
    ('Others','Others'),
}

LANGUAGES = {
    ('Python','Python'),
    ('Javascript','Javascript'),
    ('Java','Java'),
    ('C++','C++'),
    ('Ruby','Ruby'),
    ('Others','Others'),
}

DATABASES = {
    ('MySql','MySql'),
    ('PostGree','PostGree'),
    ('MongoDB','MongoDB'),
    ('SqlLite3','SqlLite3'),
    ('Oracle','Oracle'),
    ('Others','Others'),
}

LIBRARIES = {
    ('Ajax','Ajax'),
    ('Jquery','Jquery'),
    ('React.js','React.js'),
    ('Chart.js','Chart.js'),
    ('Gsap','Gsap'),
    ('Others','Others'),
}

MOBILE = {
    ('React Native','React Native'),
    ('Kivy','Kivy'),
    ('Flutter','Flutter'),
    ('Ionic','Ionic'),
    ('Xamarin','Xamarin'),
    ('Others','Others'),
}

OTHERS = {
    ('UML','UML'),
    ('SQL','SQL'),
    ('DOCKER','DOCKER'),
    ('GIT','GIT'),
    ('GraphSQL','GraphSQL'),
    ('Others','Others'),
}
class Candidate(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    job=models.CharField(max_length=50)
    age=models.CharField(max_length=3)
    phone=models.CharField(max_length=25)
    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50)
    gender= models.CharField(max_length=10)
    experience=models.BooleanField(null=True)
    smoker=models.CharField(max_length= 10, choices=SMOKER, default='')
    message=models.TextField()
    file = models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)
    Situation= models.CharField(max_length=50,null=True, choices=SITUATION, default='Pending')
    company_note= models.TextField(blank=True)
    # Multiple CheckBocex
    frameworks = MultiSelectField(choices=FRAMEWORKS, default="")
    languages = MultiSelectField(choices=LANGUAGES, default="")
    databases = MultiSelectField(choices=DATABASES, default="")
    libraries = MultiSelectField(choices=LIBRARIES, default="")
    mobile = MultiSelectField(choices=MOBILE, default="")
    others = MultiSelectField(choices=OTHERS, default="")

    # Capitalize (First name and Last Name)
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()
    
    def __str__(self):
        return self.firstname 
        
