from django.db import models
from main.models import Product
from account.models import User

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments',on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    product = models.ForeignKey(Product,related_name='ratings',on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name='ratings',on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])

