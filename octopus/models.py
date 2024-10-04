from django.db import models

class DummyModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class School(models.Model):
    id = models.IntegerField(primary_key=True,db_column='sch_id')  
    name = models.CharField(max_length=255, db_column='school_name')     

    class Meta:
        managed = False  
        db_table = 'school' 

class Answer(models.Model):
    id = models.IntegerField(primary_key=True ,db_column='answer_id')  
    name = models.CharField(max_length=255,db_column='Answers')     

    class Meta:
        managed = False  
        db_table = 'answer' 

class Assess(models.Model):
    id = models.IntegerField(primary_key=True,db_column='assess_id')  
    name = models.CharField(max_length=255,db_column='assess_area')     

    class Meta:
        managed = False  
        db_table = 'assess' 


class Class(models.Model):
    id = models.IntegerField(primary_key=True,db_column='class_id')  
    name = models.CharField(max_length=255, db_column='Class')     

    class Meta:
        managed = False  
        db_table = 'class' 


class Award(models.Model):
    id = models.IntegerField(primary_key=True,db_column='award_id')  
    name = models.CharField(max_length=255,db_column='award')     

    class Meta:
        managed = False  
        db_table = 'award' 

class Student(models.Model):
    id = models.IntegerField(primary_key=True,db_column='std_id')  
    name = models.CharField(max_length=255,db_column='full_name')     

    class Meta:
        managed = False  
        db_table = 'student' 

class Subject(models.Model):
    id = models.IntegerField(primary_key=True,db_column='subj_id')  
    name = models.CharField(max_length=255,db_column='Subject')     

    class Meta:
        managed = False  
        db_table = 'subject' 