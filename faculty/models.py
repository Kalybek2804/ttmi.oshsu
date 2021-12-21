from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField()
    image = models.ImageField(upload_to = 'images',)
    phone = models.IntegerField()
    


    def __str__(self):
        return self.name




class Lesson(models.Model):
    num = models.IntegerField()
    lesson_name = models.CharField(max_length=255)
    lesson_pdf = models.FileField()
    lesson_teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='lesson_teacher',null=True, blank=True)

    def __str__(self):
        return self.lesson_name


