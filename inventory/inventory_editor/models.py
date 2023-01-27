from django.db import models

# Create your models here.


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=3, null=False)
    quantity = models.IntegerField(default=1)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.id) + ", " + self.name + ", " + str(self.price) + ", " + str(self.quantity) + ", " + self.description
