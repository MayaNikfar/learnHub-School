from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User 

MEALS = (
    ('C', 'Chicken Nuggets'),
    ('G', 'Grilled Cheese Sandwich'),
    ('P', 'Peanut Butter and Jelly Sandwich'),
    ('M', 'Macaroni and Cheese'),
    ('C', 'Cheese Quesadilla'),
    ('P', 'Pizza'),
    ('H', 'Hot Dog'),
    ('S', 'Spaghetti with Marinara Sauce'),
    ('C', 'Chicken Tenders'),
    ('F', 'Fish Sticks'),
    ('H', 'Hamburger'),
    ('T', 'Turkey and Cheese Wrap'),
    ('M', 'Mini Corn Dogs'),
    ('V', 'Vegetable Stir-Fry'),
    ( 'P', 'Pasta Salad'),
)

# Create your models here.
class Class(models.Model):
  name = models.CharField(max_length=256)
  group = models.CharField(max_length=256)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('classes_detail', kwargs={'pk': self.id})
  
class Student(models.Model):
  name = models.CharField(max_length=100)
  contactNumber = models.CharField(max_length=25)
  age = models.IntegerField()
  # Create a M:M relationship with class
  #classes is the Related Manager
  classes = models.ManyToManyField(Class)
  # add user_id FK column
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'student_id': self.id})

  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)  

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"


class Photo(models.Model):
    url = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

def __str__(self):
    return f"Photo for student_id: {self.student_id} @{self.url}"