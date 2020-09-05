from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Books(models.Model):
    bookname = models.CharField(max_length=50)
    price = models.FloatField()
    author_name = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.bookname
