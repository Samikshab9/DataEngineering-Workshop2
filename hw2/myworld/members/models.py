from django.db import models

BRANCH_CHOICES = (
    ("Sales", "Sales"),
    ("Marketing", "Marketing"),
    ("Accounting", "Accounting"),
    ("Case_Study", "Case-Study"),
)

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    roll_number = models.IntegerField()
    mobile = models.CharField(max_length=10)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES)

    def __str__(self):
        return self.first_name + " " + self.last_name
