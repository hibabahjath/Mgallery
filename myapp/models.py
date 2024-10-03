from django.db import models

# Create your models here.

class GenreChoices(models.TextChoices):

    ACTION='Action','Action'
    FICTION='Fiction','Fiction'
    ROMANCE='Romance','Romance'
    THRILLER='Thriller','Thriller'
    COMEDY='Comedy','Comedy'
    SCI_FI='SCI-FI','SCI-FI'

# GENRE_CHOICES=[('Action','Action'),
#                'Fiction','Fiction',
#                'Romance','Romance']

class Movies(models.Model):

    title=models.CharField(max_length=200)

    genre=models.CharField(max_length=200,choices=GenreChoices.choices)
    # genre=models.CharField(max_length=200,choices=GENRE_CHOICES)

    language=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    run_time=models.PositiveIntegerField()

    director=models.CharField(max_length=200)



# class Classes(models.TextChoices):

#     one = 1,1
#     two = 2,2
#     three = 3,3
#     four = 4,4
#     five= 5,5
#     six=6,6
#     seven=7,7
#     eight=8,8
#     nine=9,9
#     ten=10,10

# class Div(models.TextChoices):

#     A='A','A'
#     B='B','B'
#     C='C','C'
#     D='D','D'

    
# class Student(models.Models):

#     name=models.CharField(max_length=200,null=True)

#     classs=models.CharField(max_length=200,choices=Classes.choices)
    
#     division=models.CharField(max_length=200,choices=Div.choices)

#     contact=models.IntegerField(max_length=200,null=True)

#     about_me=models.TextField(null=True)

#     image=models.ImageField()

# class Fuel(models.TextChoices):

#     EV='EV','EV'
#     PETROL='PETROL','PETROL'
#     DIESEL='DIESEL','DIESEL'

# class Car(models.Model):

#     name=models.CharField(max_length=200)

#     model=models.CharField(max_length=200)

#     year=models.IntegerField(max_length=200)

#     seat_capacity=models.IntegerField(max_length=200)

#     fuel_type=models.CharField(max_length=200,choices=Fuel.choices)

#     image=models.ImageField()

#     release_date=models.DateField()

#     perfomance=models.FloatField(max_length=500)

#     stock=models.BooleanField()
    
# class Aboutus(models.TextChoices):

#     Newspaper='News paper','News paper'

#     internet='Internet','Internet'

#     Magazine='Magazine','magazine'

#     Other='other','other'

# class Customer(models.Model):

    # First_name=models.CharField(max_length=200,null=False)

    # Last_name=models.CharField(max_length=200)

    # Address=models.CharField(max_length=200,null=False)

    # street_Address=models.CharField(max_length=200)

    # street_address_line2=models.CharField(max_length=200)

    # city=models.CharField(max_length=200)

    # state=models.CharField(max_length=200)

    # ZIP_code=models.IntegerField(max_length=200)

    # phone_number=models.CharField(max_length=100,null=False)

    # email=models.CharField(max_length=200)

    # hear_abou_us=models.CharField(max_length=200,null=False,choices=Aboutus.choices)
    
    # feedback=models.CharField(max_length=200)

    # recommending_us=models.CharField(max_length=200)



