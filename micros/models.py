from django.db import models
from django.db.models import Q


class Mainfooddesc(models.Model):
    foodcode = models.IntegerField(db_column='FoodCode', primary_key=True)
    mainfooddescription = models.CharField(db_column='MainFoodDesc', max_length=200)
    wweia_categorynumber = models.IntegerField(db_column='WWEIACategoryNumber')
    wweia_categorydescription = models.CharField(db_column='WWEIACategoryDesc', max_length=80)
    startdate = models.DateTimeField(db_column='StartDate')
    enddate = models.DateTimeField(db_column='EndDate')

    # Addfooddesc related_name = 'additionalDescriptions'
    # Fnddsnutval related_name='nutrientvalues'
    # Foodweights related_name='foodweights'
    # Fnddsingred related_name='foodcode_ingredients'

    class Meta:
        ordering = ['foodcode']
        managed = False
        db_table = 'fndds_MainFoodDesc'

    def __str__(self):
        return self.mainfooddescription

    def abbNutVal(self):
        return Fnddsnutval.objects.filter(
            Q(foodcode=self.foodcode) &
            (Q(nutrientcode=208) |
             Q(nutrientcode=203) |
             Q(nutrientcode=204) |
             Q(nutrientcode=205))
        )


class Foodportiondesc(models.Model):
    portioncode = models.IntegerField(db_column='PortionCode', primary_key=True)
    portiondescription = models.CharField(db_column='PortionDesc', max_length=120)
    startdate = models.DateTimeField(db_column='StartDate')
    enddate = models.DateTimeField(db_column='EndDate')

    # Foodportiondesc related_name='portionweights'
    # Fnddsingred related_name='portion_ingredients'

    class Meta:
        managed = False
        db_table = 'fndds_FoodPortionDesc'

    def __str__(self):
        return self.portiondescription


class Nutdesc(models.Model):
    nutrientcode = models.SmallIntegerField(db_column='Nutrientcode', primary_key=True)
    nutrientdescription = models.CharField(db_column='NutrientDesc', max_length=45)
    tagname = models.CharField(db_column='Tagname', max_length=15, blank=True, null=True)
    unit = models.CharField(db_column='Unit', max_length=10)
    decimals = models.SmallIntegerField(db_column='Decimals')

    # Foodweights related_name='portionweights'
    # Fnddsnutval related_name='nutrientdescriptions'

    class Meta:
        managed = False
        db_table = 'fndds_NutDesc'

    def __str__(self):
        return self.nutrient_description


class Subcodedesc(models.Model):
    subcode = models.IntegerField(db_column='Subcode', primary_key=True)
    subcode_description = models.CharField(db_column='SubcodeDescn', max_length=80)
    start_date = models.DateTimeField(db_column='StartDate')
    end_date = models.DateTimeField(db_column='EndDate')

    class Meta:
        managed = False
        db_table = 'SubcodeDesc'

    def __str__(self):
        return self.subcode_description


class Fnddsingred(models.Model):
    foodcode = models.ForeignKey('Mainfooddesc',
                                 on_delete=models.DO_NOTHING,
                                 db_column='FoodCode',
                                 related_name='foodcode_ingredients')
    seqnum = models.SmallIntegerField(db_column='SeqNum')
    ingredientcode = models.IntegerField(db_column='IngredCode')
    ingredientdescription = models.CharField(db_column='IngredDesc', max_length=240)
    amount = models.FloatField(db_column='Amount')
    measure = models.CharField(db_column='Measure', max_length=3, blank=True, null=True)
    portioncode = models.ForeignKey('Foodportiondesc',
                                    on_delete=models.DO_NOTHING,
                                    db_column='PortionCode',
                                    related_name='portion_ingredients')
    retentioncode = models.SmallIntegerField(db_column='RetentionCode')
    ingredientweight = models.FloatField(db_column='IngredientWeight')
    startdate = models.DateTimeField(db_column='StartDate')
    enddate = models.DateTimeField(db_column='EndDate')

    class Meta:
        managed = False
        db_table = 'fndds_Ingred'
        unique_together = (('foodcode', 'seqnum', 'ingredientcode'),)

    def __str__(self):
        return self.ingredientdescription


class Addfooddesc(models.Model):
    foodcode = models.ForeignKey('Mainfooddesc',
                                 on_delete=models.DO_NOTHING,
                                 db_column='FoodCode',
                                 related_name='additionalDescriptions')
    seqnum = models.SmallIntegerField(db_column='SeqNum')
    additionalfooddescription = models.CharField(db_column='AddFoodDesc', max_length=80)
    startdate = models.DateTimeField(db_column='StartDate')
    enddate = models.DateTimeField(db_column='EndDate')

    # id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fndds_AddFoodDesc'
        unique_together = (('foodcode', 'seqnum'),)

    def __str__(self):
        return self.additionalfooddescription


class Fnddsnutval(models.Model):
    foodcode = models.ForeignKey('Mainfooddesc',
                                 on_delete=models.DO_NOTHING,
                                 db_column='FoodCode',
                                 related_name='nutrientvalues')
    nutrientcode = models.ForeignKey(Nutdesc,
                                     on_delete=models.DO_NOTHING,
                                     db_column='NutrientCode',
                                     related_name='nutrientdescriptions')
    nutrientvalue = models.FloatField(db_column='NutrientValue')
    startdate = models.DateTimeField(db_column='StartDate')
    enddate = models.DateTimeField(db_column='EndDate')

    class Meta:
        managed = False
        db_table = 'FNDDSNutVal'
        unique_together = (('foodcode', 'nutrientcode'),)


class Foodweights(models.Model):
    foodcode = models.ForeignKey('Mainfooddesc',
                                 on_delete=models.DO_NOTHING,
                                 db_column='FoodCode',
                                 related_name='foodweights')
    subcode = models.IntegerField(db_column='Subcode', blank=True, null=True)
    seqnum = models.SmallIntegerField(db_column='SeqNum')
    portioncode = models.ForeignKey(Foodportiondesc,
                                    on_delete=models.DO_NOTHING,
                                    db_column='PortionCode',
                                    related_name='portionweights')
    portionweight = models.FloatField(db_column='PortionWeight')
    startdate = models.DateTimeField(db_column='StartDate')
    enddate = models.DateTimeField(db_column='EndDate')

    # id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'fndds_FoodWeights'

    def __str__(self):
        return self.portioncode.portiondescription + ": " + str(self.portionweight)


class T1Deximeal(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    subjectid = models.TextField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    mealtypedesc = models.TextField(db_column='MealTypeDesc', blank=True, null=True)  # Field name made lowercase.
    mealdescription = models.TextField(db_column='MealDescription', blank=True, null=True)  # Field name made lowercase.
    mealid = models.TextField(db_column='MealId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T1Deximeal'

    def __str__(self):
        return self.mealid


class T1Dexiimages(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    imageid = models.TextField(db_column='ImageId', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.TextField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    mealid = models.TextField(db_column='MealId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T1DexiImages'


class T1Dexiimages_NEW(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    imageid = models.TextField(db_column='ImageId', blank=True, null=True)  # Field name made lowercase.
    image = models.ImageField(upload_to='study_pics/T1Dexi', blank=True, null=True)
    subjectid = models.TextField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    mealid = models.ForeignKey('T1Deximeal', on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'T1DexiImages_NEW'

