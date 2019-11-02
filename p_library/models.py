from django.db import models

class Author(models.Model):
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    class Meta:
        verbose_name = "Authors of book"

    def __str__(self):
        return self.full_name

class Redaction(models.Model):
    name=models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    redaction = models.ForeignKey(Redaction, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

