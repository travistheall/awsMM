# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime
from django.db import models


class SrAbbrev(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', max_length=5, blank=True, null=True)
    shrt_desc = models.CharField(db_column='Shrt_Desc', max_length=60, blank=True, null=True)
    water_g_field = models.FloatField(db_column='Water_(g)', blank=True, null=True)
    energ_kcal = models.IntegerField(db_column='Energ_Kcal', blank=True, null=True)
    protein_g_field = models.FloatField(db_column='Protein_(g)', blank=True, null=True)
    lipid_tot_g_field = models.FloatField(db_column='Lipid_Tot_(g)', blank=True, null=True)
    ash_g_field = models.FloatField(db_column='Ash_(g)', blank=True, null=True)
    carbohydrt_g_field = models.FloatField(db_column='Carbohydrt_(g)', blank=True, null=True)
    fiber_td_g_field = models.FloatField(db_column='Fiber_TD_(g)', blank=True, null=True)
    sugar_tot_g_field = models.FloatField(db_column='Sugar_Tot_(g)', blank=True, null=True)
    calcium_mg_field = models.IntegerField(db_column='Calcium_(mg)', blank=True, null=True)
    iron_mg_field = models.FloatField(db_column='Iron_(mg)', blank=True, null=True)
    magnesium_mg_field = models.FloatField(db_column='Magnesium_(mg)', blank=True, null=True)
    phosphorus_mg_field = models.IntegerField(db_column='Phosphorus_(mg)', blank=True, null=True)
    potassium_mg_field = models.IntegerField(db_column='Potassium_(mg)', blank=True, null=True)
    sodium_mg_field = models.IntegerField(db_column='Sodium_(mg)', blank=True, null=True)
    zinc_mg_field = models.FloatField(db_column='Zinc_(mg)', blank=True, null=True)
    copper_mg_field = models.FloatField(db_column='Copper_mg)', blank=True, null=True)
    manganese_mg_field = models.FloatField(db_column='Manganese_(mg)', blank=True, null=True)
    selenium_g_field = models.FloatField(db_column='Selenium_(�g)', blank=True, null=True)
    vit_c_mg_field = models.FloatField(db_column='Vit_C_(mg)', blank=True, null=True)
    thiamin_mg_field = models.FloatField(db_column='Thiamin_(mg)', blank=True, null=True)
    riboflavin_mg_field = models.FloatField(db_column='Riboflavin_(mg)', blank=True, null=True)
    niacin_mg_field = models.FloatField(db_column='Niacin_(mg)', blank=True, null=True)
    panto_acid_mg_field = models.FloatField(db_column='Panto_Acid_mg)', blank=True, null=True)
    vit_b6_mg_field = models.FloatField(db_column='Vit_B6_(mg)', blank=True, null=True)
    folate_tot_g_field = models.FloatField(db_column='Folate_Tot_(�g)', blank=True, null=True)
    folic_acid_g_field = models.FloatField(db_column='Folic_Acid_(�g)', blank=True, null=True)
    food_folate_g_field = models.FloatField(db_column='Food_Folate_(�g)', blank=True, null=True)
    folate_dfe_g_field = models.FloatField(db_column='Folate_DFE_(�g)', blank=True, null=True)
    choline_tot_mg_field = models.FloatField(db_column='Choline_Tot_ (mg)', blank=True, null=True)
    vit_b12_g_field = models.FloatField(db_column='Vit_B12_(�g)', blank=True, null=True)
    vit_a_iu = models.IntegerField(db_column='Vit_A_IU', blank=True, null=True)
    vit_a_rae = models.FloatField(db_column='Vit_A_RAE', blank=True, null=True)
    retinol_g_field = models.FloatField(db_column='Retinol_(�g)', blank=True, null=True)
    alpha_carot_g_field = models.FloatField(db_column='Alpha_Carot_(�g)', blank=True, null=True)
    beta_carot_g_field = models.FloatField(db_column='Beta_Carot_(�g)', blank=True, null=True)
    beta_crypt_g_field = models.FloatField(db_column='Beta_Crypt_(�g)', blank=True, null=True)
    lycopene_g_field = models.FloatField(db_column='Lycopene_(�g)', blank=True, null=True)
    lut_zea_g_field = models.FloatField(db_column='Lut+Zea_ (�g)', blank=True, null=True)
    vit_e_mg_field = models.FloatField(db_column='Vit_E_(mg)', blank=True, null=True)
    vit_d_g = models.FloatField(db_column='Vit_D_�g', blank=True, null=True)
    vit_d_iu = models.FloatField(db_column='Vit_D_IU', blank=True, null=True)
    vit_k_g_field = models.FloatField(db_column='Vit_K_(�g)', blank=True, null=True)
    fa_sat_g_field = models.FloatField(db_column='FA_Sat_(g)', blank=True, null=True)
    fa_mono_g_field = models.FloatField(db_column='FA_Mono_(g)', blank=True, null=True)
    fa_poly_g_field = models.FloatField(db_column='FA_Poly_(g)', blank=True, null=True)
    cholestrl_mg_field = models.IntegerField(db_column='Cholestrl_(mg)', blank=True, null=True)
    gmwt_1 = models.FloatField(db_column='GmWt_1', blank=True, null=True)
    gmwt_desc1 = models.CharField(db_column='GmWt_Desc1', max_length=120, blank=True, null=True)
    gmwt_2 = models.FloatField(db_column='GmWt_2', blank=True, null=True)
    gmwt_desc2 = models.CharField(db_column='GmWt_Desc2', max_length=120, blank=True, null=True)
    refuse_pct = models.IntegerField(db_column='Refuse_Pct', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_Abbrev'


class Datasrc(models.Model):
    datasrc_id = models.CharField(db_column='DataSrc_ID', max_length=6, blank=True, null=True)
    authors = models.CharField(db_column='Authors', max_length=255, blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)
    year = models.CharField(db_column='Year', max_length=4, blank=True, null=True)
    journal = models.CharField(db_column='Journal', max_length=135, blank=True, null=True)
    vol_city = models.CharField(db_column='Vol_City', max_length=16, blank=True, null=True)
    issue_state = models.CharField(db_column='Issue_State', max_length=5, blank=True, null=True)
    start_page = models.CharField(db_column='Start_Page', max_length=5, blank=True, null=True)
    end_page = models.CharField(db_column='End_Page', max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_DataSrc'


class Datsrcln(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', max_length=5, blank=True, null=True)
    nutr_no = models.CharField(db_column='Nutr_No', max_length=3, blank=True, null=True)
    datasrc_id = models.CharField(db_column='DataSrc_ID', max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_Datsrcln'


class Derivcd(models.Model):
    deriv_cd = models.CharField(db_column='Deriv_CD', max_length=4, blank=True, null=True)
    deriv_desc = models.CharField(db_column='Deriv_Desc', max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_DerivCd'


class Fdgroup(models.Model):
    fdgrp_cd = models.CharField(db_column='FdGrp_CD', max_length=4, blank=True, null=True)
    fdgrp_desc = models.CharField(db_column='FdGrp_Desc', max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_FdGroup'


class Fooddes(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', primary_key=True, max_length=5)
    fdgrp_cd = models.CharField(db_column='FdGrp_Cd', max_length=4)
    long_desc = models.CharField(db_column='Long_Desc', max_length=200, blank=True, null=True)
    shrt_desc = models.CharField(db_column='Shrt_Desc', max_length=60, blank=True, null=True)
    comname = models.CharField(db_column='ComName', max_length=100, blank=True, null=True)
    manufacname = models.CharField(db_column='ManufacName', max_length=65, blank=True, null=True)
    survey = models.CharField(db_column='Survey', max_length=1, blank=True, null=True)
    ref_desc = models.CharField(db_column='Ref_Desc', max_length=135, blank=True, null=True)
    refuse = models.SmallIntegerField(db_column='Refuse', blank=True, null=True)
    sciname = models.CharField(db_column='SciName', max_length=65, blank=True, null=True)
    n_factor = models.FloatField(db_column='N_Factor', blank=True, null=True)
    pro_factor = models.FloatField(db_column='Pro_Factor', blank=True, null=True)
    fat_factor = models.FloatField(db_column='Fat_Factor', blank=True, null=True)
    cho_factor = models.FloatField(db_column='CHO_Factor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_FoodDes'


class Footnote(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', max_length=5, blank=True, null=True)
    footnt_no = models.CharField(db_column='Footnt_No', max_length=4, blank=True, null=True)
    footnot_typ = models.CharField(db_column='Footnot_Typ', max_length=1, blank=True, null=True)
    nutr_no = models.CharField(db_column='Nutr_No', max_length=3, blank=True, null=True)
    footnot_txt = models.CharField(db_column='Footnot_Txt', max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_Footnote'


class Langdesc(models.Model):
    factor = models.CharField(db_column='Factor', max_length=6, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_LangDesc'


class Langual(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', max_length=5, blank=True, null=True)
    factor = models.CharField(db_column='Factor', max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_Langual'


class Nutdata(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', max_length=5, blank=True, null=True)
    nutr_no = models.CharField(db_column='Nutr_No', max_length=3, blank=True, null=True)
    nutr_val = models.FloatField(db_column='Nutr_Val', blank=True, null=True)
    num_data_pts = models.IntegerField(db_column='Num_Data_Pts', blank=True, null=True)
    std_error = models.FloatField(db_column='Std_Error', blank=True, null=True)
    src_cd = models.CharField(db_column='Src_Cd', max_length=2, blank=True, null=True)
    deriv_cd = models.CharField(db_column='Deriv_Cd', max_length=4, blank=True, null=True)
    ref_ndb_no = models.CharField(db_column='Ref_NDB_No', max_length=5, blank=True, null=True)
    add_nutr_mark = models.CharField(db_column='Add_Nutr_Mark', max_length=1, blank=True, null=True)
    num_studies = models.SmallIntegerField(db_column='Num_Studies', blank=True, null=True)
    min = models.FloatField(db_column='Min', blank=True, null=True)
    max = models.FloatField(db_column='Max', blank=True, null=True)
    df = models.FloatField(db_column='DF', blank=True, null=True)
    low_eb = models.FloatField(db_column='Low_EB', blank=True, null=True)
    up_eb = models.FloatField(db_column='Up_EB', blank=True, null=True)
    stat_cmt = models.CharField(db_column='Stat_Cmt', max_length=10, blank=True, null=True)
    addmod_date = models.CharField(db_column='AddMod_Date', max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_NutData'


class Nutrdef(models.Model):
    nutr_no = models.CharField(db_column='Nutr_No', max_length=3, blank=True, null=True)
    units = models.CharField(db_column='Units', max_length=7, blank=True, null=True)
    tagname = models.CharField(db_column='Tagname', max_length=20, blank=True, null=True)
    nutrdesc = models.CharField(db_column='NutrDesc', max_length=60, blank=True, null=True)
    num_dec = models.CharField(db_column='Num_Dec', max_length=1, blank=True, null=True)
    sr_order = models.FloatField(db_column='SR_Order', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_NutrDef'


class Srccd(models.Model):
    src_cd = models.CharField(db_column='Src_Cd', max_length=2, blank=True, null=True)
    srccd_desc = models.CharField(db_column='SrcCd_Desc', max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_SrcCd'


class Weight(models.Model):
    ndb_no = models.CharField(db_column='NDB_No', max_length=5, blank=True, null=True)
    seq = models.CharField(db_column='Seq', max_length=2, blank=True, null=True)
    amount = models.FloatField(db_column='Amount', blank=True, null=True)
    msre_desc = models.CharField(db_column='Msre_Desc', max_length=84, blank=True, null=True)
    gm_wgt = models.FloatField(db_column='Gm_Wgt', blank=True, null=True)
    num_data_pts = models.SmallIntegerField(db_column='Num_Data_Pts', blank=True, null=True)
    std_dev = models.FloatField(db_column='Std_Dev', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sr_Weight'
