from django.db import models

# Create your models here.
class Emissions(models.Model):
    entity = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()#####for visualization
    year = models.IntegerField()
    electricity_access = models.FloatField()
    cooking_fuel_access = models.FloatField()
    renewable_electricity_capacity = models.FloatField()
    fossil_fuel_electricity = models.FloatField()
    nuclear_electricity = models.FloatField()
    renewable_electricity = models.FloatField()
    low_carbon_electricity = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.entity} id: {self.id}"  ##return a string

class CarbonStock(models.Model):
    alpha_code = models.TextField(max_length=100)
    year = models.TextField(max_length=100)
    is_dC_loss = models.FloatField()
    is_dC_loss_unc = models.FloatField()
    lnlg_dC_loss = models.FloatField()
    lnlg_dC_loss_unc = models.FloatField()
    lnlgis_dC_loss = models.FloatField()
    lnlgis_dC_loss_unc = models.FloatField()
    lnlgogis_dC_loss = models.FloatField()
    lnlgogis_dC_loss_unc = models.FloatField()
    is_nbe = models.FloatField()
    is_nbe_unc = models.FloatField()
    lnlg_nbe = models.FloatField()
    lnlg_nbe_unc = models.FloatField()
    lnlgis_nbe = models.FloatField()
    lnlgis_nbe_unc = models.FloatField()
    lnlgogis_nbe = models.FloatField()
    lnlgogis_nbe_unc = models.FloatField()
    is_nce = models.FloatField()
    is_nce_unc = models.FloatField()
    lnlg_nce = models.FloatField()
    lnlg_nce_unc = models.FloatField()
    lnlgis_nce = models.FloatField()
    lnlgis_nce_unc = models.FloatField()
    lnlgogis_nce = models.FloatField()
    lnlgogis_nce_unc = models.FloatField()
    rivers = models.FloatField()
    river_unc = models.FloatField()
    wood_crop = models.FloatField()
    wood_crop_unc = models.FloatField()
    ff = models.FloatField()
    ff_unc = models.FloatField()
    z_statistic = models.FloatField()
    fur_is = models.FloatField()
    fur_lnlg = models.FloatField()
    fur_lnlgis = models.FloatField()
    fur_lnlgogis = models.FloatField()

