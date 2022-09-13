from operator import truediv
from random import choices
from django.db import models

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
    
    # Capitalize (First name and Last Name)
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()
    
    def __str__(self):
        return self.firstname 
        