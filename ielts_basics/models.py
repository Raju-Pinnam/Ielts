from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CommonUser(models.Model):
    """Common fields for all type of users"""
    mobile_number = models.CharField(max_length=10)


class Trainer(CommonUser):
    """
    to conduct training  
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return f"{self.user.username}"


class TrainerToTrainer(CommonUser):
    """
    for the fresh trainers to learn training skills 
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}"
    

class Student(CommonUser):
    """
    Student Model 
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}"

