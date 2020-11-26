from django.db import models

# Create your models here.
class Order(models.Model):
    mobile=models.CharField(max_length=120)
    user=models.CharField(max_length=120)
    quantity=models.IntegerField()
    Address=models.CharField(max_length=120)
    choices=(
        ('ordered','ordered'),('cancelled','cancelled'),('dispatched','dispatched'),('delivered','delivered')
    )
    status=models.CharField(max_length=120,choices=choices,default="ordered")
    # image=models.ImageField(upload_to="images")



    def __str__(self):
        return self.mobile+self.user
