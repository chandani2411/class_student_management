from django.db import models
from django.contrib.auth.models import AbstractUser
SECTIONS = (('A', 'A'), ('B', 'B'), ('C', 'C'))
EXAM_NAME=(('1','Quarterly'),('2','Half_yearly'),('3','Annualy'))
SUBJECTS=(('1','Maths'),('2','Physics'),('3','Chemistry'),('4','Hindi'),('5','English'))
class Class(models.Model):
    class_name=models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return str(self.class_name)

class Section(models.Model):
    class_section=models.ForeignKey(Class)
    section = models.CharField(choices=SECTIONS, max_length=100)

    def __str__(self):
        return str(self.section)



class Subject(models.Model):
    # Store Subject Information
    subject_name = models.CharField(choices=SUBJECTS,max_length=150, null=True, blank=True)
    sub_code = models.CharField(max_length=255, unique=True, null=True,blank=True)
    sub_marks=models.IntegerField(default=0)

    def __str__(self):
        return str(self.subject_name)

class Exam(models.Model):
    # Store Exam Information

    exam_title = models.CharField(choices=EXAM_NAME,max_length=150, null=True, blank=True)
    exam_date = models.DateField(null=True, blank=True)
    exam_roll_no=models.CharField(max_length=130,null=True,blank=True)
    subject_id=models.ManyToManyField(Subject)
    exam_marks=models.IntegerField(default=0)

    def __str__(self):
        return str(self.exam_title)

class Student(models.Model):
    # Store Student Information
    first_name=models.CharField(max_length=15, null=True, blank=True)
    last_name=models.CharField(max_length=15, null=True, blank=True)
    student_class=models.ForeignKey(Class,related_name='students')
    roll_no = models.IntegerField(unique=True,null=True,blank=True)
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    subject=models.ManyToManyField(Subject)
    exam = models.ManyToManyField(Exam)
    total_marks_in_class=models.IntegerField(null=True,blank=True)


    def __str__(self):
        return str(self.first_name+self.last_name)





