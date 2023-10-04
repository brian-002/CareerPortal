from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_photo/%Y/%m/%d')
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    sir_name = models.CharField(max_length=255)
    user_bio = models.TextField(null=True, blank=True)  # Account user bio
    id_no = models.CharField(max_length=255)  # Account user national identification number

    EMPLOYMENT_STATUS_CHOICES = (
        ('employed', 'Employed'),
        ('unemployed', 'Unemployed'),
        ('self_employed', 'Self-employed'),
        ('student', 'Student'),
        ('other', 'Other'),
    )
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_STATUS_CHOICES)  # Account user employment status

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not_specified', "I'd rather not disclose"),
    )
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)  # Male, female, and I'd rather not disclose

    MARITAL_STATUS_CHOICES = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    )
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)  # Account user marital status

    HIGHEST_EDUCATION_CHOICES = (
        ('high_school', 'High School'),
        ('college', 'College'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctorate', 'Doctorate'),
        ('other', 'Other'),
    )
    highest_level_of_education = models.CharField(max_length=20, choices=HIGHEST_EDUCATION_CHOICES)  # Account user highest level of education

    town_of_residence = models.TextField()  # Town of account user residence
    po_box = models.BigIntegerField()  # PO box of account user residence
    zip_code = models.BigIntegerField()  # Zip code of account user residence
    contact_email = models.EmailField()  # Account user email
    contact_phone_no = models.TextField()  # Account user primary phone no
    alternative_phone_no = models.TextField()  # Account user alternative phone no
    nok_email = models.EmailField()  # Next of kin email
    nok_phone_no = models.TextField()  # Next of kin primary phone number
    nok_alternative_phone_no = models.TextField()  # Next of kin alternative phone number

    certificates = models.FileField(upload_to='certificates/%Y/%m/%d', null=True, blank=True)  # User's certificates
    curriculum_vitae = models.FileField(upload_to='cv/%Y/%m/%d', null=True, blank=True)  # User's curriculum vitae

    def __str__(self):
        return self.user.username


    



class JobApplication(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    application_letter = models.FileField(upload_to='application_letter/%Y/%m/%d')
    additional_certificates = models.FileField(upload_to='additional_certificates/%Y/%m/%d', blank=True)
    application_date = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return f"{self.user_profile.first_name} {self.user_profile.second_name} - {self.position}"
    

class PortalPhotos(models.Model):
    portal_image = models.ImageField(upload_to='portal_photo/%Y/%m/%d')

    def __str__(self):
        return self.portal_image
