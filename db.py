# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class T1Dexiimages(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    imageid = models.TextField(db_column='ImageId', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.TextField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    mealid = models.TextField(db_column='MealId', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'T1DexiImages'


class T1DexiimagesNew(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    imageid = models.TextField(db_column='ImageId', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(max_length=100, blank=True, null=True)
    subjectid = models.TextField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    mealid = models.TextField(db_column='MealId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T1DexiImages_NEW'





class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FnddsAddfooddesc(models.Model):
    foodcode = models.ForeignKey('FnddsMainfooddesc', models.DO_NOTHING, db_column='FoodCode')  # Field name made lowercase.
    seqnum = models.SmallIntegerField(db_column='SeqNum')  # Field name made lowercase.
    addfooddesc = models.CharField(db_column='AddFoodDesc', max_length=80)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_AddFoodDesc'
        unique_together = (('foodcode', 'seqnum'),)


class FnddsDerivdesc(models.Model):
    derivationcode = models.CharField(db_column='DerivationCode', primary_key=True, max_length=4)  # Field name made lowercase.
    derivationdescription = models.CharField(db_column='DerivationDescription', max_length=120)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_DerivDesc'


class FnddsFped1718(models.Model):
    foodcode = models.OneToOneField('FnddsMainfooddesc', models.DO_NOTHING, db_column='FoodCode', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255)  # Field name made lowercase.
    f_total = models.FloatField(db_column='F_TOTAL')  # Field name made lowercase.
    f_citmlb = models.FloatField(db_column='F_CITMLB')  # Field name made lowercase.
    f_other = models.FloatField(db_column='F_OTHER')  # Field name made lowercase.
    f_juice = models.FloatField(db_column='F_JUICE')  # Field name made lowercase.
    v_total = models.FloatField(db_column='V_TOTAL')  # Field name made lowercase.
    v_drkgr = models.FloatField(db_column='V_DRKGR')  # Field name made lowercase.
    v_redor_total = models.FloatField(db_column='V_REDOR_TOTAL')  # Field name made lowercase.
    v_redor_tomato = models.FloatField(db_column='V_REDOR_TOMATO')  # Field name made lowercase.
    v_redor_other = models.FloatField(db_column='V_REDOR_OTHER')  # Field name made lowercase.
    v_starchy_total = models.FloatField(db_column='V_STARCHY_TOTAL')  # Field name made lowercase.
    v_starchy_potato = models.FloatField(db_column='V_STARCHY_POTATO')  # Field name made lowercase.
    v_starchy_other = models.FloatField(db_column='V_STARCHY_OTHER')  # Field name made lowercase.
    v_other = models.FloatField(db_column='V_OTHER')  # Field name made lowercase.
    v_legumes = models.FloatField(db_column='V_LEGUMES')  # Field name made lowercase.
    g_total = models.FloatField(db_column='G_TOTAL')  # Field name made lowercase.
    g_whole = models.FloatField(db_column='G_WHOLE')  # Field name made lowercase.
    g_refined = models.FloatField(db_column='G_REFINED')  # Field name made lowercase.
    pf_total = models.FloatField(db_column='PF_TOTAL')  # Field name made lowercase.
    pf_mps_total = models.FloatField(db_column='PF_MPS_TOTAL')  # Field name made lowercase.
    pf_meat = models.FloatField(db_column='PF_MEAT')  # Field name made lowercase.
    pf_curedmeat = models.FloatField(db_column='PF_CUREDMEAT')  # Field name made lowercase.
    pf_organ = models.FloatField(db_column='PF_ORGAN')  # Field name made lowercase.
    pf_poult = models.FloatField(db_column='PF_POULT')  # Field name made lowercase.
    pf_seafd_hi = models.FloatField(db_column='PF_SEAFD_HI')  # Field name made lowercase.
    pf_seafd_low = models.FloatField(db_column='PF_SEAFD_LOW')  # Field name made lowercase.
    pf_eggs = models.FloatField(db_column='PF_EGGS')  # Field name made lowercase.
    pf_soy = models.FloatField(db_column='PF_SOY')  # Field name made lowercase.
    pf_nutsds = models.FloatField(db_column='PF_NUTSDS')  # Field name made lowercase.
    pf_legumes = models.FloatField(db_column='PF_LEGUMES')  # Field name made lowercase.
    d_total = models.FloatField(db_column='D_TOTAL')  # Field name made lowercase.
    d_milk = models.FloatField(db_column='D_MILK')  # Field name made lowercase.
    d_yogurt = models.FloatField(db_column='D_YOGURT')  # Field name made lowercase.
    d_cheese = models.FloatField(db_column='D_CHEESE')  # Field name made lowercase.
    oils = models.FloatField(db_column='OILS')  # Field name made lowercase.
    solid_fats = models.FloatField(db_column='SOLID_FATS')  # Field name made lowercase.
    add_sugars = models.FloatField(db_column='ADD_SUGARS')  # Field name made lowercase.
    a_drinks = models.FloatField(db_column='A_DRINKS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_FPED_1718'


class FnddsFoodportiondesc(models.Model):
    portioncode = models.IntegerField(db_column='PortionCode', primary_key=True)  # Field name made lowercase.
    portiondesc = models.CharField(db_column='PortionDesc', max_length=120)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_FoodPortionDesc'


class FnddsFoodsubcodelinks(models.Model):
    foodcode = models.IntegerField(db_column='FoodCode')  # Field name made lowercase.
    subcode = models.IntegerField(db_column='Subcode')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_FoodSubcodeLinks'
        unique_together = (('foodcode', 'subcode'),)


class FnddsFoodweights(models.Model):
    foodcode = models.IntegerField(db_column='FoodCode', blank=True, null=True)  # Field name made lowercase.
    subcode = models.IntegerField(db_column='Subcode', blank=True, null=True)  # Field name made lowercase.
    seqnum = models.SmallIntegerField(db_column='SeqNum', blank=True, null=True)  # Field name made lowercase.
    portioncode = models.IntegerField(db_column='PortionCode', blank=True, null=True)  # Field name made lowercase.
    portionweight = models.FloatField(db_column='PortionWeight', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_FoodWeights'


class FnddsIngred(models.Model):
    foodcode = models.ForeignKey('FnddsMainfooddesc', models.DO_NOTHING, db_column='FoodCode')  # Field name made lowercase.
    seqnum = models.SmallIntegerField(db_column='SeqNum')  # Field name made lowercase.
    ingredcode = models.IntegerField(db_column='IngredCode')  # Field name made lowercase.
    ingreddesc = models.CharField(db_column='IngredDesc', max_length=240)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    measure = models.CharField(db_column='Measure', max_length=3, blank=True, null=True)  # Field name made lowercase.
    portioncode = models.ForeignKey(FnddsFoodportiondesc, models.DO_NOTHING, db_column='PortionCode')  # Field name made lowercase.
    retentioncode = models.SmallIntegerField(db_column='RetentionCode')  # Field name made lowercase.
    ingredientweight = models.FloatField(db_column='IngredientWeight')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_Ingred'
        unique_together = (('foodcode', 'seqnum'),)


class FnddsIngrednutval(models.Model):
    ingredientcode = models.IntegerField(db_column='IngredientCode')  # Field name made lowercase.
    ingreddesc = models.CharField(db_column='IngredDesc', max_length=200)  # Field name made lowercase.
    nutrientcode = models.IntegerField(db_column='NutrientCode')  # Field name made lowercase.
    nutrient_value = models.FloatField(db_column='Nutrient value')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nutrientvaluesource = models.CharField(db_column='NutrientValueSource', max_length=80)  # Field name made lowercase.
    fdc_id = models.FloatField(db_column='FDC_ID', blank=True, null=True)  # Field name made lowercase.
    derivationcode = models.CharField(db_column='DerivationCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sr_addmod_year = models.SmallIntegerField(db_column='SR_AddMod_year', blank=True, null=True)  # Field name made lowercase.
    foundation_year_acquired = models.SmallIntegerField(db_column='Foundation_year_acquired', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_IngredNutVal'
        unique_together = (('ingredientcode', 'nutrientcode'),)


class FnddsMainfooddesc(models.Model):
    foodcode = models.IntegerField(db_column='FoodCode', primary_key=True)  # Field name made lowercase.
    mainfooddesc = models.CharField(db_column='MainFoodDesc', max_length=200)  # Field name made lowercase.
    wweiacategorynumber = models.IntegerField(db_column='WWEIACategoryNumber', blank=True, null=True)  # Field name made lowercase.
    wweiacategorydesc = models.CharField(db_column='WWEIACategoryDesc', max_length=80, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_MainFoodDesc'


class FnddsMoistadjust(models.Model):
    foodcode = models.OneToOneField(FnddsMainfooddesc, models.DO_NOTHING, db_column='FoodCode', primary_key=True)  # Field name made lowercase.
    moisturechange = models.FloatField(db_column='MoistureChange', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_MoistAdjust'


class FnddsNutdesc(models.Model):
    nutrientcode = models.SmallIntegerField(db_column='NutrientCode', primary_key=True)  # Field name made lowercase.
    nutrientdesc = models.CharField(db_column='NutrientDesc', max_length=45)  # Field name made lowercase.
    tagname = models.CharField(db_column='Tagname', max_length=15)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=10)  # Field name made lowercase.
    decimals = models.SmallIntegerField(db_column='Decimals', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_NutDesc'


class FnddsNutval(models.Model):
    foodcode = models.ForeignKey(FnddsMainfooddesc, models.DO_NOTHING, db_column='FoodCode')  # Field name made lowercase.
    nutrientcode = models.SmallIntegerField(db_column='NutrientCode')  # Field name made lowercase.
    nutrientvalue = models.FloatField(db_column='NutrientValue')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_NutVal'
        unique_together = (('foodcode', 'nutrientcode'),)


class FnddsReccount(models.Model):
    fullfilename = models.CharField(db_column='FullFileName', max_length=50)  # Field name made lowercase.
    no_of_records = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fndds_RecCount'


class FnddsSubcodedesc(models.Model):
    subcode = models.IntegerField(db_column='Subcode', primary_key=True)  # Field name made lowercase.
    subcodedesc = models.CharField(db_column='SubcodeDesc', max_length=80)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fndds_SubcodeDesc'


class SrAbbrev(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', max_length=5, blank=True, null=True)  # Field name made lowercase.
    shrt_desc = models.CharField(db_column='Shrt_Desc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    water_g_field = models.FloatField(db_column='Water_(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    energ_kcal = models.IntegerField(db_column='Energ_Kcal', blank=True, null=True)  # Field name made lowercase.
    protein_g_field = models.FloatField(db_column='Protein_(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lipid_tot_g_field = models.FloatField(db_column='Lipid_Tot_(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ash_g_field = models.FloatField(db_column='Ash_(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    carbohydrt_g_field = models.FloatField(db_column='Carbohydrt_(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fiber_td_g_field = models.FloatField(db_column='Fiber_TD_(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sugar_tot_g_field = models.FloatField(db_column='Sugar_Tot_(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    calcium_mg_field = models.IntegerField(db_column='Calcium_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    iron_mg_field = models.FloatField(db_column='Iron_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    magnesium_mg_field = models.FloatField(db_column='Magnesium_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    phosphorus_mg_field = models.IntegerField(db_column='Phosphorus_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    potassium_mg_field = models.IntegerField(db_column='Potassium_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sodium_mg_field = models.IntegerField(db_column='Sodium_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    zinc_mg_field = models.FloatField(db_column='Zinc_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    copper_mg_field = models.FloatField(db_column='Copper_mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    manganese_mg_field = models.FloatField(db_column='Manganese_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    selenium_�g_field = models.FloatField(db_column='Selenium_(�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vit_c_mg_field = models.FloatField(db_column='Vit_C_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    thiamin_mg_field = models.FloatField(db_column='Thiamin_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    riboflavin_mg_field = models.FloatField(db_column='Riboflavin_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    niacin_mg_field = models.FloatField(db_column='Niacin_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    panto_acid_mg_field = models.FloatField(db_column='Panto_Acid_mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vit_b6_mg_field = models.FloatField(db_column='Vit_B6_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    folate_tot_�g_field = models.FloatField(db_column='Folate_Tot_(�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    folic_acid_�g_field = models.FloatField(db_column='Folic_Acid_(�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    food_folate_�g_field = models.FloatField(db_column='Food_Folate_(�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    folate_dfe_�g_field = models.FloatField(db_column='Folate_DFE_(�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    choline_tot_mg_field = models.FloatField(db_column='Choline_Tot_ (mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vit_b12_�g_field = models.FloatField(db_column='Vit_B12_(�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vit_a_iu = models.IntegerField(db_column='Vit_A_IU', blank=True, null=True)  # Field name made lowercase.
    vit_a_rae = models.FloatField(db_column='Vit_A_RAE', blank=True, null=True)  # Field name made lowercase.
    retinol_�g_field = models.FloatField(db_column='Retinol_(�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    alpha_carot_�g_field = models.FloatField(db_column='Alpha_Carot_(�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    beta_carot_�g_field = models.FloatField(db_column='Beta_Carot_(�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    beta_crypt_�g_field = models.FloatField(db_column='Beta_Crypt_(�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lycopene_�g_field = models.FloatField(db_column='Lycopene_(�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lut_zea_�g_field = models.FloatField(db_column='Lut+Zea_ (�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vit_e_mg_field = models.FloatField(db_column='Vit_E_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vit_d_�g = models.FloatField(db_column='Vit_D_�g', blank=True, null=True)  # Field name made lowercase.
    vit_d_iu = models.FloatField(db_column='Vit_D_IU', blank=True, null=True)  # Field name made lowercase.
    vit_k_�g_field = models.FloatField(db_column='Vit_K_(�g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fa_sat_g_field = models.FloatField(db_column='FA_Sat_(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fa_mono_g_field = models.FloatField(db_column='FA_Mono_(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fa_poly_g_field = models.FloatField(db_column='FA_Poly_(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cholestrl_mg_field = models.IntegerField(db_column='Cholestrl_(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    gmwt_1 = models.FloatField(db_column='GmWt_1', blank=True, null=True)  # Field name made lowercase.
    gmwt_desc1 = models.CharField(db_column='GmWt_Desc1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    gmwt_2 = models.FloatField(db_column='GmWt_2', blank=True, null=True)  # Field name made lowercase.
    gmwt_desc2 = models.CharField(db_column='GmWt_Desc2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    refuse_pct = models.IntegerField(db_column='Refuse_Pct', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_Abbrev'


class SrDatasrc(models.Model):
    datasrc_id = models.CharField(db_column='DataSrc_ID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    authors = models.CharField(db_column='Authors', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=4, blank=True, null=True)  # Field name made lowercase.
    journal = models.CharField(db_column='Journal', max_length=135, blank=True, null=True)  # Field name made lowercase.
    vol_city = models.CharField(db_column='Vol_City', max_length=16, blank=True, null=True)  # Field name made lowercase.
    issue_state = models.CharField(db_column='Issue_State', max_length=5, blank=True, null=True)  # Field name made lowercase.
    start_page = models.CharField(db_column='Start_Page', max_length=5, blank=True, null=True)  # Field name made lowercase.
    end_page = models.CharField(db_column='End_Page', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_DataSrc'


class SrDatsrcln(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nutr_no = models.CharField(db_column='Nutr_No', max_length=3, blank=True, null=True)  # Field name made lowercase.
    datasrc_id = models.CharField(db_column='DataSrc_ID', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_Datsrcln'


class SrDerivcd(models.Model):
    deriv_cd = models.CharField(db_column='Deriv_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    deriv_desc = models.CharField(db_column='Deriv_Desc', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_DerivCd'


class SrFdgroup(models.Model):
    fdgrp_cd = models.CharField(db_column='FdGrp_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fdgrp_desc = models.CharField(db_column='FdGrp_Desc', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_FdGroup'


class SrFooddes(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', primary_key=True, max_length=5)  # Field name made lowercase.
    fdgrp_cd = models.CharField(db_column='FdGrp_Cd', max_length=4)  # Field name made lowercase.
    long_desc = models.CharField(db_column='Long_Desc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shrt_desc = models.CharField(db_column='Shrt_Desc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    comname = models.CharField(db_column='ComName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    manufacname = models.CharField(db_column='ManufacName', max_length=65, blank=True, null=True)  # Field name made lowercase.
    survey = models.CharField(db_column='Survey', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ref_desc = models.CharField(db_column='Ref_Desc', max_length=135, blank=True, null=True)  # Field name made lowercase.
    refuse = models.SmallIntegerField(db_column='Refuse', blank=True, null=True)  # Field name made lowercase.
    sciname = models.CharField(db_column='SciName', max_length=65, blank=True, null=True)  # Field name made lowercase.
    n_factor = models.FloatField(db_column='N_Factor', blank=True, null=True)  # Field name made lowercase.
    pro_factor = models.FloatField(db_column='Pro_Factor', blank=True, null=True)  # Field name made lowercase.
    fat_factor = models.FloatField(db_column='Fat_Factor', blank=True, null=True)  # Field name made lowercase.
    cho_factor = models.FloatField(db_column='CHO_Factor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_FoodDes'


class SrFootnote(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', max_length=5, blank=True, null=True)  # Field name made lowercase.
    footnt_no = models.CharField(db_column='Footnt_No', max_length=4, blank=True, null=True)  # Field name made lowercase.
    footnot_typ = models.CharField(db_column='Footnot_Typ', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nutr_no = models.CharField(db_column='Nutr_No', max_length=3, blank=True, null=True)  # Field name made lowercase.
    footnot_txt = models.CharField(db_column='Footnot_Txt', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_Footnote'


class SrLangdesc(models.Model):
    factor = models.CharField(db_column='Factor', max_length=6, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_LangDesc'


class SrLangual(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', max_length=5, blank=True, null=True)  # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_Langual'


class SrNutdata(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nutr_no = models.CharField(db_column='Nutr_No', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nutr_val = models.FloatField(db_column='Nutr_Val', blank=True, null=True)  # Field name made lowercase.
    num_data_pts = models.IntegerField(db_column='Num_Data_Pts', blank=True, null=True)  # Field name made lowercase.
    std_error = models.FloatField(db_column='Std_Error', blank=True, null=True)  # Field name made lowercase.
    src_cd = models.CharField(db_column='Src_Cd', max_length=2, blank=True, null=True)  # Field name made lowercase.
    deriv_cd = models.CharField(db_column='Deriv_Cd', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ref_ndb_no = models.CharField(db_column='Ref_NDB_No', max_length=5, blank=True, null=True)  # Field name made lowercase.
    add_nutr_mark = models.CharField(db_column='Add_Nutr_Mark', max_length=1, blank=True, null=True)  # Field name made lowercase.
    num_studies = models.SmallIntegerField(db_column='Num_Studies', blank=True, null=True)  # Field name made lowercase.
    min = models.FloatField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    max = models.FloatField(db_column='Max', blank=True, null=True)  # Field name made lowercase.
    df = models.FloatField(db_column='DF', blank=True, null=True)  # Field name made lowercase.
    low_eb = models.FloatField(db_column='Low_EB', blank=True, null=True)  # Field name made lowercase.
    up_eb = models.FloatField(db_column='Up_EB', blank=True, null=True)  # Field name made lowercase.
    stat_cmt = models.CharField(db_column='Stat_Cmt', max_length=10, blank=True, null=True)  # Field name made lowercase.
    addmod_date = models.CharField(db_column='AddMod_Date', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_NutData'


class SrNutrdef(models.Model):
    nutr_no = models.CharField(db_column='Nutr_No', max_length=3, blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=7, blank=True, null=True)  # Field name made lowercase.
    tagname = models.CharField(db_column='Tagname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nutrdesc = models.CharField(db_column='NutrDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    num_dec = models.CharField(db_column='Num_Dec', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sr_order = models.FloatField(db_column='SR_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_NutrDef'


class SrSrccd(models.Model):
    src_cd = models.CharField(db_column='Src_Cd', max_length=2, blank=True, null=True)  # Field name made lowercase.
    srccd_desc = models.CharField(db_column='SrcCd_Desc', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_SrcCd'


class SrWeight(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', max_length=5, blank=True, null=True)  # Field name made lowercase.
    seq = models.CharField(db_column='Seq', max_length=2, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    msre_desc = models.CharField(db_column='Msre_Desc', max_length=84, blank=True, null=True)  # Field name made lowercase.
    gm_wgt = models.FloatField(db_column='Gm_Wgt', blank=True, null=True)  # Field name made lowercase.
    num_data_pts = models.SmallIntegerField(db_column='Num_Data_Pts', blank=True, null=True)  # Field name made lowercase.
    std_dev = models.FloatField(db_column='Std_Dev', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sr_Weight'


class UsersFood(models.Model):
    taken_serving = models.FloatField(blank=True, null=True)
    returned_serving = models.FloatField(blank=True, null=True)
    food = models.ForeignKey(FnddsMainfooddesc, models.DO_NOTHING)
    meal = models.ForeignKey('UsersMeal', models.DO_NOTHING, blank=True, null=True)
    servingsize = models.ForeignKey(FnddsFoodweights, models.DO_NOTHING, db_column='servingSize_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_food'


class UsersMeal(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=1)
    image = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    profile = models.ForeignKey('UsersProfile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_meal'


class UsersProfile(models.Model):
    image = models.CharField(max_length=100)
    isdark = models.BooleanField(db_column='isDark')  # Field name made lowercase.
    sex = models.IntegerField()
    age = models.SmallIntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    heightunit = models.FloatField(db_column='heightUnit')  # Field name made lowercase.
    activitylevel = models.FloatField(db_column='activityLevel')  # Field name made lowercase.
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_profile'


class UsersWeight(models.Model):
    weight = models.FloatField(blank=True, null=True)
    weightunit = models.FloatField(db_column='weightUnit')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    profile = models.ForeignKey(UsersProfile, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_weight'
