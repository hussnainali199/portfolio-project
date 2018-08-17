from django.db import models

# Create your models here.

class Blogging(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(blank=True, null =True)
    body = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    def pack(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
