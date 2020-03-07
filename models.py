from django.db import models

# Create your (models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    
    def _str_(self):
        return self.name

class Post(models.Model):
    statuses=[
        ("d","draft"),
        ("p","published"),
    ]
    title=models.CharField(max_length =255)
    content=models.TextField()
    status=models.CharField(max_length=1,choices=statuses)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def _str_(self):
      return self.title