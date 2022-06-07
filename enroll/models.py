from django.db import models

class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('novel', 'Novel'),
        ('scifi','Sci-Fi'),
        ('self-help','Self-Help')
        ]
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='education')
   

