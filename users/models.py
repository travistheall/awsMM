from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from micros.models import Mainfooddesc, Foodweights


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user.png', upload_to='profile_pics')
    SEX_CHOICES = [
        (5, "Male"),
        (-161, "Female")
    ]
    sex = models.IntegerField(choices=SEX_CHOICES,
                              default=5)
    age = models.SmallIntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    HEIGHT_UNIT_CHOICES = [
        (2.54, "Inches"),
        (1, "Centimeters"),
    ]
    heightUnit = models.FloatField(choices=HEIGHT_UNIT_CHOICES,
                                   default=1)
    ACTIVITY_LEVEL_CHOICES = [
        (1.2, "Sedentary"),
        (1.375, "Light Activity"),
        (1.55, "Moderately Active"),
        (1.725, "Very Active"),
        (1.9, "Extremely Active"),
    ]
    activityLevel = models.FloatField(choices=ACTIVITY_LEVEL_CHOICES,
                                      default=1.2)

    """def get_calories(self):
        return int(((10 * (self.weight / self.weightUnit)) + (6.25 * (self.height * self.heightUnit)) - (
            5 * self.age) + self.sex) * self.activityLevel)"""

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Weight(models.Model):
    weight = models.FloatField(blank=True, null=True)
    WEIGHT_UNIT_CHOICES = [
        (2.20462, "Pounds"),
        (1, "Kilograms"),
    ]
    weightUnit = models.FloatField(choices=WEIGHT_UNIT_CHOICES,
                                   default=1)
    profile = models.ForeignKey(Profile,
                                on_delete=models.DO_NOTHING,
                                related_name="weights",
                                blank=True,
                                null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __int__(self):
        return self.weight


class Photo(models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.DO_NOTHING,
                                related_name="meal_photos",
                                blank=True,
                                null=True)
    MEAL_CHOICES = [
        ("b", "Breakfast"),
        ("ms", "Morning Snack"),
        ("l", "Lunch"),
        ("as", "Afternoon Snack"),
        ("d", "Dinner"),
        ("es", "Evening Snack"),
        ("mns", "Midnight Snack"),
    ]
    meal = models.CharField(choices=MEAL_CHOICES, max_length=3, default='b')
    image = models.ImageField(upload_to='meal_pics', blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Food(models.Model):
    photo = models.ForeignKey(Photo,
                              on_delete=models.DO_NOTHING,
                              related_name="photos_foods",
                              blank=True,
                              null=True)
    food = models.ForeignKey(Mainfooddesc, on_delete=models.DO_NOTHING, related_name="foods_in_photo")
    servingSize = models.ForeignKey(Foodweights,
                                    related_name="portion_sizes",
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL)
    taken_serving = models.FloatField(blank=True, null=True)
    returned_serving = models.FloatField(blank=True, null=True)
