from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.CharField(max_length=4)
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def pud_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    # Changes the admin referenced text
    def __str__(self):
        return self.title
