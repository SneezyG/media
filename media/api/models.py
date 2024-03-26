from django.db import models

# Create your models here.
def generate_poster_path():
  pass

class Movie(models.Model):
    STATUS_CHOICES = [
        ('coming_up', 'Coming Up'),
        ('starting', 'Starting'),
        ('running', 'Running'),
        ('finished', 'Finished'),
    ]

    name = models.CharField(max_length=100)
    protagonists = models.TextField()
    poster = models.URLField()
    trailer = models.URLField()
    start_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='coming_up')
    ranking = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['-ranking']


