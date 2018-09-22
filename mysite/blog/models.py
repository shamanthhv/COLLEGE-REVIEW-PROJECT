from django.db import models

class college(models.Model):
    college_name = models.CharField(max_length=100)
    college_details = models.TextField()
    college_reviews = models.TextField(null=True)
    college_rating = models.CharField(max_length=15)

    def __str__(self):
        return self.college_name
