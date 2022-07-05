# 참고
# https://hae-ong.tistory.com/25


from django.db import models

# Create your models here.

class MapStore(models.Model):
    addr = models.CharField(max_length=255, blank=True, null=True)
    storename = models.CharField(max_length=255, blank=True, null=True)
    storetype = models.CharField(max_length=255, blank=True, null=True)
    callnum = models.CharField(max_length=255, blank=True, null=True)
    menu1 = models.CharField(max_length=255, blank=True, null=True)
    menu2 = models.CharField(max_length=255, blank=True, null=True)
    menu3 = models.CharField(max_length=255, blank=True, null=True)
    menu1_price = models.IntegerField(blank=True, null=True)
    menu2_price = models.IntegerField(blank=True, null=True)
    menu3_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Map_store'
