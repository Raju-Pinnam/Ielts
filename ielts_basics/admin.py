from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CommonUser)
admin.site.register(Trainer)
admin.site.register(TrainerToTrainer)
admin.site.register(Student)