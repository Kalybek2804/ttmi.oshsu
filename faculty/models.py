from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField(blank=True, null=True)
    image = models.ImageField(upload_to = 'images')
    
    class Meta:
        ordering = ('name',)
    


    def __str__(self):
        return f'{self.name}'




class Lesson(models.Model):
    lesson_num = models.IntegerField(default = None)
    lesson_name = models.CharField(max_length=255,  null=True)
    lesson_pdf = models.FileField(blank=True, null=True, default = None)
    lesson_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name='lesson_teacher',null=True, blank=True)

    def __str__(self):
        return f'{self.lesson_name}'


