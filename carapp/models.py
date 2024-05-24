from djongo import models


class Car(models.Model):
    car_name = models.CharField(max_length=255)
    number_of_cylinders = models.IntegerField()
    number_of_passengers = models.IntegerField()
    car_color = models.CharField(max_length=255)
    cylinder_volume = models.FloatField()
    owner_name = models.CharField(max_length=255)
    # Add any additional fields you need


    class Meta:
        db_table = 'car'
