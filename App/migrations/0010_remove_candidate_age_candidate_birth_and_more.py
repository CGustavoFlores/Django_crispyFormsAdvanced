# Generated by Django 4.0.4 on 2022-09-24 19:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_candidate_company_note_alter_candidate_situation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='age',
        ),
        migrations.AddField(
            model_name='candidate',
            name='birth',
            field=models.DateField(default=datetime.datetime(2022, 9, 24, 19, 5, 28, 927000, tzinfo=utc), verbose_name='Birthday'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='Situation',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Disapproved', 'Disapproved'), ('Approved', 'Approved')], default='Pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='databases',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('MongoDB', 'MongoDB'), ('SqlLite3', 'SqlLite3'), ('Others', 'Others'), ('Oracle', 'Oracle'), ('PostGree', 'PostGree'), ('MySql', 'MySql')], default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='frameworks',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('FastAPI', 'FastAPI'), ('Angular', 'Angular'), ('Vue', 'Vue'), ('Django', 'Django'), ('Laravel', 'Laravel'), ('Others', 'Others')], default='', max_length=41),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Java', 'Java'), ('C++', 'C++'), ('Others', 'Others'), ('Ruby', 'Ruby'), ('Javascript', 'Javascript'), ('Python', 'Python')], default='', max_length=38),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='libraries',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Gsap', 'Gsap'), ('Jquery', 'Jquery'), ('React.js', 'React.js'), ('Chart.js', 'Chart.js'), ('Ajax', 'Ajax'), ('Others', 'Others')], default='', max_length=41),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='mobile',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Others', 'Others'), ('Kivy', 'Kivy'), ('React Native', 'React Native'), ('Flutter', 'Flutter'), ('Xamarin', 'Xamarin'), ('Ionic', 'Ionic')], default='', max_length=46),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='others',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('UML', 'UML'), ('DOCKER', 'DOCKER'), ('SQL', 'SQL'), ('GraphSQL', 'GraphSQL'), ('GIT', 'GIT'), ('Others', 'Others')], default='', max_length=34),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='personality',
            field=models.CharField(choices=[('I am serious', 'I am serious'), ('I am sociable', 'I am sociable'), ('I am outgoing', 'I am outgoing'), ('I am antisocial', 'I am antisocial'), ('', 'Select a personality'), ('I am discreet', 'I am discreet')], max_length=50, null=True),
        ),
    ]