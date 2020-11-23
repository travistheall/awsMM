from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from micros.models import Mainfooddesc, Foodweights


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user.png', upload_to='profile_pics')
    isDark = models.BooleanField(default=False)
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

    def __str__(self):
        return self.user.username

    """def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)"""


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
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.profile.user.username} {self.weight} {self.get_weightUnit_display()}"

    def get_calories(self):
        return int(
            ((10 * (self.weight / self.weightUnit)) + (6.25 * (self.profile.height * self.profile.heightUnit)) - (
                    5 * self.profile.age) + self.profile.sex) * self.profile.activityLevel)


class Meal(models.Model):
    id = models.CharField(max_length=50, primary_key=True, blank=False, null=False)
    profile = models.ForeignKey(Profile,
                                on_delete=models.DO_NOTHING,
                                related_name="profiles_meals",
                                blank=True,
                                null=True)
    MEAL_CHOICES = [
        ("b", "Breakfast"),
        ("l", "Lunch"),
        ("d", "Dinner"),
        ("s", "Snack"),
    ]
    name = models.CharField(choices=MEAL_CHOICES, max_length=1, default='b')
    image = models.ImageField(upload_to='meal_pics', blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"


class Food(models.Model):
    meal = models.ForeignKey(Meal,
                              on_delete=models.DO_NOTHING,
                              related_name="meals_foods",
                              blank=True,
                              null=True)
    food = models.ForeignKey(Mainfooddesc, on_delete=models.DO_NOTHING, related_name="foods_in_meal")
    servingSize = models.ForeignKey(Foodweights,
                                    related_name="portion_sizes",
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL)
    taken_serving = models.FloatField(blank=True, null=True)
    returned_serving = models.FloatField(blank=True, null=True)
