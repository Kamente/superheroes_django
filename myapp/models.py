from django.db import models

class Power(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Hero(models.Model):
    name = models.CharField(max_length=255)
    super_name = models.CharField(max_length=255)
    powers = models.ManyToManyField(Power, through='HeroPower')
    
    def __str__(self):
        return self.name
    
class HeroPower(models.Model):
    STRENGTH_CHOICES = (
        ('Strong', 'Strong'),
        ('Weak', 'Weak'),
        ('Average', 'Average'),
    )
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    power = models.models.ForeignKey(Power, on_delete=models.CASCADE)
    strength = models.CharField(max_length=10, choices=STRENGTH_CHOICES)
    
    def __str__(self):
        return f'{self.hero} - {self.power}'
    
    