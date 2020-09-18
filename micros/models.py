from django.db import models


class Mainfooddesc(models.Model):
    foodcode = models.IntegerField(db_column='FoodCode', primary_key=True)
    mainfooddescription = models.CharField(db_column='MainFoodDescription', max_length=200)
    wweia_categorynumber = models.IntegerField(db_column='WWEIA_CategoryNumber')
    wweia_categorydescription = models.CharField(db_column='WWEIA_CategoryDescription', max_length=80)
    startdate = models.DateTimeField(db_column='StartDate')
    enddate = models.DateTimeField(db_column='EndDate')

    class Meta:
        managed = False
        db_table = 'MainFoodDesc'

    def __str__(self):
        return self.mainfooddescription


class Foodportiondesc(models.Model):
    portioncode = models.IntegerField(db_column='PortionCode', primary_key=True)
    portiondescription = models.CharField(db_column='PortionDescription', max_length=120)
    startdate = models.DateTimeField(db_column='StartDate')
    enddate = models.DateTimeField(db_column='EndDate')

    class Meta:
        managed = False
        db_table = 'FoodPortionDesc'

    def __str__(self):
        return self.portiondescription


class Nutdesc(models.Model):
    nutrientcode = models.SmallIntegerField(db_column='Nutrientcode', primary_key=True)
    nutrientdescription = models.CharField(db_column='NutrientDescription', max_length=45)
    tagname = models.CharField(db_column='Tagname', max_length=15, blank=True, null=True)
    unit = models.CharField(db_column='Unit', max_length=10)
    decimals = models.SmallIntegerField(db_column='Decimals')

    class Meta:
        managed = False
        db_table = 'NutDesc'

    def __str__(self):
        return self.nutrient_description


class Subcodedesc(models.Model):
    subcode = models.IntegerField(db_column='Subcode', primary_key=True)
    subcode_description = models.CharField(db_column='Subcode description', max_length=80)
    start_date = models.DateTimeField(db_column='Start date')
    end_date = models.DateTimeField(db_column='End date')

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
    ingredientcode = models.IntegerField(db_column='IngredientCode')
    ingredientdescription = models.CharField(db_column='IngredientDescription', max_length=240)
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
        db_table = 'FNDDSIngred'
        unique_together = (('foodcode', 'seqnum', 'ingredientcode'),)

    def __str__(self):
        return self.ingredientdescription


class Addfooddesc(models.Model):
    foodcode = models.ForeignKey('Mainfooddesc',
                                 on_delete=models.DO_NOTHING,
                                 db_column='FoodCode',
                                 related_name='additionalDescriptions')
    seqnum = models.SmallIntegerField(db_column='SeqNum')
    additionalfooddescription = models.CharField(db_column='AdditionalFoodDescription', max_length=80)
    startdate = models.DateTimeField(db_column='StartDate')
    enddate = models.DateTimeField(db_column='EndDate')
    #id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AddFoodDesc'
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
    #id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FoodWeights'
        unique_together = (('foodcode', 'subcode', 'seqnum', 'portioncode'),)
