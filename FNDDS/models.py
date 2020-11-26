# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime
from django.db import models
from django.db.models import Q


class Mainfooddesc(models.Model):
    foodCode = models.IntegerField(db_column='FoodCode', primary_key=True)
    mainFoodDesc = models.CharField(db_column='MainFoodDesc', max_length=200)
    wweiaCategoryNumber = models.IntegerField(db_column='WWEIACategoryNumber')
    wweiaCategoryDesc = models.CharField(db_column='WWEIACategoryDesc', max_length=80)
    startDate = models.DateTimeField(db_column='StartDate')
    endDate = models.DateTimeField(db_column='EndDate')

    # Addfooddesc related_name = 'addDescs'
    # Fnddsnutval related_name='nutrientvalues'
    # Foodweights related_name='foodweights'
    # Fnddsingred related_name='foodcodeIngreds'

    class Meta:
        ordering = ['foodcode']
        managed = False
        db_table = 'fndds_MainFoodDesc'

    def __str__(self):
        return self.mainFoodDesc

    def abbNutVal(self):
        return Nutval.objects.filter(
            Q(foodcode=self.foodCode) &
            (Q(nutrientcode=208) |
             Q(nutrientcode=203) |
             Q(nutrientcode=204) |
             Q(nutrientcode=205))
        )


class Foodportiondesc(models.Model):
    portionCode = models.IntegerField(db_column='PortionCode', primary_key=True)
    portionDesc = models.CharField(db_column='PortionDesc', max_length=120)
    startDate = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    endDate = models.DateTimeField(db_column='EndDate', blank=True, null=True)

    # Foodportiondesc related_name='portionWeights'
    # Fnddsingred related_name='portionIngreds'

    class Meta:
        managed = False
        db_table = 'fndds_FoodPortionDesc'

    def __str__(self):
        return self.portionDesc


class Nutdesc(models.Model):
    nutrientCode = models.SmallIntegerField(db_column='NutrientCode', primary_key=True)
    nutrientDesc = models.CharField(db_column='NutrientDesc', max_length=45)
    tagName = models.CharField(db_column='Tagname', max_length=15)
    unit = models.CharField(db_column='Unit', max_length=10)
    decimals = models.SmallIntegerField(db_column='Decimals', blank=True, null=True)

    # Foodweights related_name='portionWeights'
    # Fnddsnutval related_name='nutrientDescs'

    class Meta:
        managed = False
        db_table = 'fndds_NutDesc'

    def __str__(self):
        return self.nutrientDesc


class Subcodedesc(models.Model):
    subCode = models.IntegerField(db_column='Subcode', primary_key=True)
    subCodeDesc = models.CharField(db_column='SubcodeDesc', max_length=80)
    startDate = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    endDate = models.DateTimeField(db_column='EndDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fndds_SubcodeDesc'

    def __str__(self):
        return self.subCodeDesc


class Ingred(models.Model):
    foodCode = models.ForeignKey('Mainfooddesc', models.DO_NOTHING, db_column='FoodCode',
                                 related_name='foodcodeIngreds')
    seqNum = models.SmallIntegerField(db_column='SeqNum')
    ingredCode = models.IntegerField(db_column='IngredCode')
    ingredDesc = models.CharField(db_column='IngredDesc', max_length=240)
    amount = models.FloatField(db_column='Amount')
    measure = models.CharField(db_column='Measure', max_length=3, blank=True, null=True)
    portionCode = models.ForeignKey('Foodportiondesc', models.DO_NOTHING, db_column='PortionCode',
                                    related_name='portionIngreds')
    retentionCode = models.SmallIntegerField(db_column='RetentionCode')
    ingredientWeight = models.FloatField(db_column='IngredientWeight')
    startDate = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    endDate = models.DateTimeField(db_column='EndDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fndds_Ingred'
        unique_together = (('foodCode', 'seqNum'),)

    def __str__(self):
        return self.IngredDesc


class Addfooddesc(models.Model):
    foodCode = models.ForeignKey('Mainfooddesc', models.DO_NOTHING, db_column='FoodCode', related_name='AddDescs')
    seqNum = models.SmallIntegerField(db_column='SeqNum')
    addFoodDesc = models.CharField(db_column='AddFoodDesc', max_length=80)
    startDate = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    endDate = models.DateTimeField(db_column='EndDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fndds_AddFoodDesc'
        unique_together = (('foodCode', 'seqNum'),)

    def __str__(self):
        return self.addFoodDesc


class Nutval(models.Model):
    foodCode = models.ForeignKey(Mainfooddesc, models.DO_NOTHING, db_column='FoodCode', related_name='nutrientValues')
    nutrientCode = models.SmallIntegerField(Nutdesc,
                                            on_delete=models.DO_NOTHING,
                                            db_column='NutrientCode',
                                            related_name='nutrientdescriptions')
    nutrientValue = models.FloatField(db_column='NutrientValue')
    startDate = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    endDate = models.DateTimeField(db_column='EndDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fndds_NutVal'
        unique_together = (('foodCode', 'nutrientCode'),)


class Foodweights(models.Model):
    foodCode = models.ForeignKey('Mainfooddesc',
                                 on_delete=models.DO_NOTHING,
                                 db_column='FoodCode',
                                 related_name='foodWeights')
    subCode = models.IntegerField(db_column='Subcode', blank=True, null=True)
    seqNum = models.SmallIntegerField(db_column='SeqNum', blank=True, null=True)
    portionCode = models.ForeignKey(Foodportiondesc,
                                    on_delete=models.DO_NOTHING,
                                    db_column='PortionCode',
                                    related_name='portionWeights')
    portionWeight = models.FloatField(db_column='PortionWeight', blank=True, null=True)
    startDate = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    endDate = models.DateTimeField(db_column='EndDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fndds_FoodWeights'

    def __str__(self):
        return self.portionCode.portionDesc + ": " + str(self.portionWeight)


class Derivdesc(models.Model):
    derivationCode = models.CharField(db_column='DerivationCode', primary_key=True, max_length=4)
    derivationDescription = models.CharField(db_column='DerivationDescription', max_length=120)

    class Meta:
        managed = False
        db_table = 'fndds_DerivDesc'


class Foodsubcodelinks(models.Model):
    foodCode = models.IntegerField(db_column='FoodCode')
    subCode = models.IntegerField(db_column='Subcode')
    startDate = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    endDate = models.DateTimeField(db_column='EndDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fndds_FoodSubcodeLinks'
        unique_together = (('foodCode', 'subCode'),)


class Ingrednutval(models.Model):
    ingredientCode = models.IntegerField(db_column='IngredientCode')
    ingredDesc = models.CharField(db_column='IngredDesc', max_length=200)
    nutrientCode = models.IntegerField(db_column='NutrientCode')
    nutrientValue = models.FloatField(db_column='Nutrient value')
    nutrientValueSource = models.CharField(db_column='NutrientValueSource', max_length=80)
    fdcId = models.FloatField(db_column='FDC_ID', blank=True, null=True)
    derivationCode = models.CharField(db_column='DerivationCode', max_length=4, blank=True, null=True)
    srAddmodYear = models.SmallIntegerField(db_column='SR_AddMod_year', blank=True, null=True)
    foundationYearAcquired = models.SmallIntegerField(db_column='Foundation_year_acquired', blank=True, null=True)
    startDate = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    endDate = models.DateTimeField(db_column='EndDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fndds_IngredNutVal'
        unique_together = (('ingredientCode', 'nutrientCode'),)


class Moistadjust(models.Model):
    foodCode = models.OneToOneField(Mainfooddesc, models.DO_NOTHING, db_column='FoodCode', primary_key=True)
    moistureChange = models.FloatField(db_column='MoistureChange', blank=True, null=True)
    startDate = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    endDate = models.DateTimeField(db_column='EndDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fndds_MoistAdjust'


class Reccount(models.Model):
    fullfilename = models.CharField(db_column='FullFileName', max_length=50)
    no_of_records = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fndds_RecCount'


class Fped1718(models.Model):
    foodcode = models.OneToOneField('Mainfooddesc', models.DO_NOTHING, db_column='FoodCode', primary_key=True)
    description = models.CharField(db_column='DESCRIPTION', max_length=255)
    f_total = models.FloatField(db_column='F_TOTAL')
    f_citmlb = models.FloatField(db_column='F_CITMLB')
    f_other = models.FloatField(db_column='F_OTHER')
    f_juice = models.FloatField(db_column='F_JUICE')
    v_total = models.FloatField(db_column='V_TOTAL')
    v_drkgr = models.FloatField(db_column='V_DRKGR')
    v_redor_total = models.FloatField(db_column='V_REDOR_TOTAL')
    v_redor_tomato = models.FloatField(db_column='V_REDOR_TOMATO')
    v_redor_other = models.FloatField(db_column='V_REDOR_OTHER')
    v_starchy_total = models.FloatField(db_column='V_STARCHY_TOTAL')
    v_starchy_potato = models.FloatField(db_column='V_STARCHY_POTATO')
    v_starchy_other = models.FloatField(db_column='V_STARCHY_OTHER')
    v_other = models.FloatField(db_column='V_OTHER')
    v_legumes = models.FloatField(db_column='V_LEGUMES')
    g_total = models.FloatField(db_column='G_TOTAL')
    g_whole = models.FloatField(db_column='G_WHOLE')
    g_refined = models.FloatField(db_column='G_REFINED')
    pf_total = models.FloatField(db_column='PF_TOTAL')
    pf_mps_total = models.FloatField(db_column='PF_MPS_TOTAL')
    pf_meat = models.FloatField(db_column='PF_MEAT')
    pf_curedmeat = models.FloatField(db_column='PF_CUREDMEAT')
    pf_organ = models.FloatField(db_column='PF_ORGAN')
    pf_poult = models.FloatField(db_column='PF_POULT')
    pf_seafd_hi = models.FloatField(db_column='PF_SEAFD_HI')
    pf_seafd_low = models.FloatField(db_column='PF_SEAFD_LOW')
    pf_eggs = models.FloatField(db_column='PF_EGGS')
    pf_soy = models.FloatField(db_column='PF_SOY')
    pf_nutsds = models.FloatField(db_column='PF_NUTSDS')
    pf_legumes = models.FloatField(db_column='PF_LEGUMES')
    d_total = models.FloatField(db_column='D_TOTAL')
    d_milk = models.FloatField(db_column='D_MILK')
    d_yogurt = models.FloatField(db_column='D_YOGURT')
    d_cheese = models.FloatField(db_column='D_CHEESE')
    oils = models.FloatField(db_column='OILS')
    solid_fats = models.FloatField(db_column='SOLID_FATS')
    add_sugars = models.FloatField(db_column='ADD_SUGARS')
    a_drinks = models.FloatField(db_column='A_DRINKS')

    class Meta:
        managed = False
        db_table = 'fndds_FPED_1718'
