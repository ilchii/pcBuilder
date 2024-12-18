from django.db import models
from django.contrib.auth.models import User  # Import the User model

SOCKET_TYPE_CHOICES = [
    ("AM4", "AM4"),
    ("AM5", "AM5"),
    ("LGA1200", "LGA1200"),
    ("LGA1700", "LGA1700"),
]

# Create your models here.

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


# class Build(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User who created the build
#     name = models.CharField(max_length=100)  # Name of the build
#     processor = models.ForeignKey(Processor, on_delete=models.CASCADE, null=True, blank=True)
#     motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE, null=True, blank=True)
#     memory = models.ForeignKey(Memory, on_delete=models.CASCADE, null=True, blank=True)
#     storage = models.ForeignKey(Storage, on_delete=models.CASCADE, null=True, blank=True)
#     video_card = models.ForeignKey(VideoCard, on_delete=models.CASCADE, null=True, blank=True)
#     case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True, blank=True)
#     power_supply = models.ForeignKey(PowerSupply, on_delete=models.CASCADE, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the build was created
#
#     def __str__(self):
#         return f"{self.name} by {self.user.username}"

class Build(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User who created the build
    name = models.CharField(max_length=100)  # Name of the build
    image = models.ImageField(upload_to='build_images/', null=True, blank=True)  # Image for the build
    processor = models.ForeignKey('Processor', on_delete=models.CASCADE, null=True, blank=True)
    motherboard = models.ForeignKey('Motherboard', on_delete=models.CASCADE, null=True, blank=True)
    memory = models.ForeignKey('Memory', on_delete=models.CASCADE, null=True, blank=True)
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE, null=True, blank=True)
    video_card = models.ForeignKey('VideoCard', on_delete=models.CASCADE, null=True, blank=True)
    case = models.ForeignKey('Case', on_delete=models.CASCADE, null=True, blank=True)
    power_supply = models.ForeignKey('PowerSupply', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the build was created

    def __str__(self):
        return f"{self.name} by {self.user.username}"

    @property
    def total_price(self):
        price_fields = [
            self.processor.price_usd if self.processor else 0,
            self.motherboard.price_usd if self.motherboard else 0,
            self.memory.price_usd if self.memory else 0,
            self.storage.price_usd if self.storage else 0,
            self.video_card.price_usd if self.video_card else 0,
            self.case.price_usd if self.case else 0,
            self.power_supply.price_usd if self.power_supply else 0,
        ]
        return sum(price_fields)
