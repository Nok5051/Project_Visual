# 참고
# https://hae-ong.tistory.com/25


from django.db import models

# Create your models here.

class MapStore(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    storeaddr = models.CharField(max_length=255, blank=True, null=True)
    newstoreadd = models.CharField(max_length=255, blank=True, null=True)
    addr = models.CharField(max_length=255, blank=True, null=True)
    storename = models.CharField(max_length=255, blank=True, null=True)
    storetype = models.CharField(max_length=255, blank=True, null=True)
    callnum = models.CharField(max_length=255, blank=True, null=True)
    menu1 = models.CharField(max_length=255, blank=True, null=True)
    menu2 = models.CharField(max_length=255, blank=True, null=True)
    menu3 = models.CharField(max_length=255, blank=True, null=True)
    menu1_price = models.CharField(max_length=255, blank=True, null=True)
    menu2_price = models.CharField(max_length=255, blank=True, null=True)
    menu3_price = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Map_store'