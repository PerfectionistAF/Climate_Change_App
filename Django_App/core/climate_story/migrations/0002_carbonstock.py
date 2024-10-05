# Generated by Django 5.0.6 on 2024-10-05 03:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("climate_story", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarbonStock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("alpha_code", models.CharField(max_length=100)),
                ("year", models.CharField(max_length=100)),
                ("is_dC_loss", models.FloatField()),
                ("is_dC_loss_unc", models.FloatField()),
                ("lnlg_dC_loss", models.FloatField()),
                ("lnlg_dC_loss_unc", models.FloatField()),
                ("lnlgis_dC_loss", models.FloatField()),
                ("lnlgis_dC_loss_unc", models.FloatField()),
                ("lnlgogis_dC_loss", models.FloatField()),
                ("lnlgogis_dC_loss_unc", models.FloatField()),
                ("is_nbe", models.FloatField()),
                ("is_nbe_unc", models.FloatField()),
                ("lnlg_nbe", models.FloatField()),
                ("lnlg_nbe_unc", models.FloatField()),
                ("lnlgis_nbe", models.FloatField()),
                ("lnlgis_nbe_unc", models.FloatField()),
                ("lnlgogis_nbe", models.FloatField()),
                ("lnlgogis_nbe_unc", models.FloatField()),
                ("is_nce", models.FloatField()),
                ("is_nce_unc", models.FloatField()),
                ("lnlg_nce", models.FloatField()),
                ("lnlg_nce_unc", models.FloatField()),
                ("lnlgis_nce", models.FloatField()),
                ("lnlgis_nce_unc", models.FloatField()),
                ("lnlgogis_nce", models.FloatField()),
                ("lnlgogis_nce_unc", models.FloatField()),
                ("rivers", models.FloatField()),
                ("river_unc", models.FloatField()),
                ("wood_crop", models.FloatField()),
                ("wood_crop_unc", models.FloatField()),
                ("ff", models.FloatField()),
                ("ff_unc", models.FloatField()),
                ("z_statistic", models.FloatField()),
                ("fur_is", models.FloatField()),
                ("fur_lnlg", models.FloatField()),
                ("fur_lnlgis", models.FloatField()),
                ("fur_lnlgogis", models.FloatField()),
            ],
        ),
    ]