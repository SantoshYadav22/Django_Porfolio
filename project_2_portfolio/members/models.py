# myapp/models.py
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)  # Allowing null values temporarily
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CompanyExperience(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='experiences')
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)  # Allowing null values temporarily
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.first_name}'s Experience at {self.company_name}"

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  start_date = models.DateField(null=True, blank=True)  # Allowing null values temporarily
  end_date = models.DateField(blank=True, null=True)

class user_port(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  location = models.CharField(max_length=255)
  contact = models.IntegerField(default=18)
  language = models.CharField(max_length=255)
  skill = models.CharField(max_length=255)
  work_expirence = models.CharField(max_length=255)
  education = models.CharField(max_length=255)
  project = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  summary = models.TextField()
  image = models.ImageField(upload_to='images/', blank=True, null=True)


  start_date = models.DateField(null=True, blank=True, auto_now_add=True)
  end_date = models.DateField(blank=True, null=True, auto_now_add=True)

