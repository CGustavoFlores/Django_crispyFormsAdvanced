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


STATUSCOURSE = {
    ('','Select your status'),
    ('I am student','I am student'),
    ('I am broke','I am broke'),
    ('I am complete','I am complete'),
}
class Candidate(models.Model):
    # Personal (Card 1)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    job=models.CharField(max_length=50)
    #age=models.CharField(max_length=3)
    birth=models.DateField(auto_now=False,auto_now_add=False,verbose_name="Birthday")
    phone=models.CharField(max_length=25)
    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50)
    gender= models.CharField(max_length=10)
    experience=models.BooleanField(null=True)
    smoker=models.CharField(max_length= 10, choices=SMOKER, default='')
    message=models.TextField()
    file = models.FileField(upload_to='resume',blank=True, verbose_name="Resume")
    image= models.ImageField(upload_to='photo',blank=True, verbose_name="Potho")
    created_at=models.DateTimeField(auto_now_add=True)
    Situation= models.CharField(max_length=50,null=True, choices=SITUATION, default='Pending')
    company_note= models.TextField(blank=True)
    # SKILLS (Card 2)
    # Multiple CheckBocex
    frameworks = MultiSelectField(choices=FRAMEWORKS, default="")
    languages = MultiSelectField(choices=LANGUAGES, default="")
    databases = MultiSelectField(choices=DATABASES, default="")
    libraries = MultiSelectField(choices=LIBRARIES, default="")
    mobile = MultiSelectField(choices=MOBILE, default="")
    others = MultiSelectField(choices=OTHERS, default="")
    # EDUCATIONAL (Card 3)
    institution= models.CharField(max_length=50)
    course= models.CharField(max_length=50)
    started_course= models.DateField(auto_now=False, auto_now_add=False)
    finished_course= models.DateField(auto_now=False, auto_now_add=False)
    about_course= models.CharField(max_length=50)
    status_course= models.CharField(max_length=50, choices=STATUSCOURSE)
    # PROFESSIONAL (Card 4)
    company= models.CharField(max_length=50)
    position= models.CharField(max_length=50)
    started_job= models.DateField(auto_now=False, auto_now_add=False)
    finished_job= models.DateField(auto_now=False, auto_now_add=False)
    employed= models.BooleanField(null=True,verbose_name="I am employed")
    remote= models.BooleanField(null=True,verbose_name="I agree remote to work remotely")
    travel= models.BooleanField(null=True,verbose_name="I' m avaible for travel")
    # Capitalize (First name and Last Name)
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()
    
    def __str__(self):
        return self.firstname 
        
