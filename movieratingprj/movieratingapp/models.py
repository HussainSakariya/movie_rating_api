from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class movies(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField(max_length=50)

    def no_of_ratings(self):
        rate=ratings.objects.filter(movie=self.id)
        return len(rate)
    
    def avg_ratings(self):
        rate=ratings.objects.filter(movie=self.id)
        sum=0
        for r in rate:
            sum+=r.ratings

        try:
            return sum//len(rate)
        except:
            return 0

class ratings(models.Model):
    movie=models.ForeignKey(movies,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ratings=models.IntegerField()


