from django.db import models

# Create your models here.

SOCKET_TYPE_CHOICES = [
    ("AM4", "AM4"),
    ("AM5", "AM5"),
    ("LGA1200", "LGA1200"),
    ("LGA1700", "LGA1700"),
]

# Processor model
class Processor(models.Model):
    name = models.CharField(max_length=100)
    cores = models.IntegerField()
    threads = models.IntegerField()
    clock_speed = models.DecimalField(max_digits=5, decimal_places=2)  # GHz
    socket_type = models.CharField(max_length=50, choices=SOCKET_TYPE_CHOICES, default="AM4")
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Motherboard model
class Motherboard(models.Model):
    name = models.CharField(max_length=100)
    chipset = models.CharField(max_length=50)
    form_factor = models.CharField(max_length=50)
    socket_type = models.CharField(max_length=50, choices=SOCKET_TYPE_CHOICES, default="AM4")
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Memory model
class Memory(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()  # GB
    speed = models.IntegerField()  # MHz
    type = models.CharField(max_length=50)  # e.g., DDR4
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Storage model
class Storage(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()  # GB
    type = models.CharField(max_length=50)  # e.g., SSD, HDD
    read_speed = models.IntegerField()  # MB/s
    write_speed = models.IntegerField()  # MB/s
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# VideoCard model
class VideoCard(models.Model):
    name = models.CharField(max_length=100)
    memory = models.IntegerField()  # GB
    clock_speed = models.DecimalField(max_digits=5, decimal_places=2)  # GHz
    cuda_cores = models.IntegerField()
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Case model
class Case(models.Model):
    name = models.CharField(max_length=100)
    form_factor = models.CharField(max_length=50)
    material = models.CharField(max_length=100)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# PowerSupply model
class PowerSupply(models.Model):
    name = models.CharField(max_length=100)
    wattage = models.IntegerField()  # Watts
    efficiency_rating = models.CharField(max_length=50)  # e.g., 80 Plus Gold
    modular = models.BooleanField()  # True if modular
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
