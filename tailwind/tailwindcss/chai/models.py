from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('EL','ELYCHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    
    def __str__(self):
        return super().__str__() + " " + self.name

# One to Many relationship with User model
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return super().__str__() + " " + self.review_text

class ChaiOrder(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return super().__str__() + " " + str(self.quantity) + " " + self.chai.name  

class ChaiCart(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return super().__str__() + " " + str(self.quantity) + " " + self.chai.name
            