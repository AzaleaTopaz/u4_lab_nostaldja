from django.db import models

# ALTER DATABASE tunr OWNER TO tunruser;

# Create your models here.
class Century(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.name
