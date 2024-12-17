from django.contrib import admin
from mainapp.models import Processor, Motherboard, Memory, Storage, VideoCard, Case, PowerSupply, Build

# Register your models here.

# Registering models in the admin panel
admin.site.register(Processor)
admin.site.register(Motherboard)
admin.site.register(Memory)
admin.site.register(Storage)
admin.site.register(VideoCard)
admin.site.register(Case)
admin.site.register(PowerSupply)
admin.site.register(Build)
