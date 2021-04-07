from django.db import models

# Create your models here.
class Medium(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Artwork(models.Model):
    medium = models.ForeignKey("Medium", null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=350)
    description = models.TextField(blank=True)
    canvas_dimension = models.CharField(max_length=30)
    canvas_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_discounted = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    review = models.TextField(blank=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

