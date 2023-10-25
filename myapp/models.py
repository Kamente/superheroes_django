# models.py

from django.db import models
class Power(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Hero(models.Model):
    name = models.CharField(max_length=255)
    super_name = models.CharField(max_length=255)
    powers = models.ManyToManyField(Power, through='HeroPower')


class HeroPower(models.Model):
    STRENGTH_CHOICES = [
        ('Strong', 'Strong'),
        ('Weak', 'Weak'),
        ('Average', 'Average'),
    ]
    strength = models.CharField(max_length=255, choices=STRENGTH_CHOICES)
    power = models.ForeignKey(Power, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
