from django.db import models


# Create your models here.
class Coupon(models.Model):
    coupon_code = models.CharField(max_length=50)
    coupon_count = models.SmallIntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Generate Coupon'
        verbose_name_plural = 'Generate Coupon'

    # SL_2223_001
    def clean(self):
        self.coupon_code = self.coupon_code.strip()

    def __str__(self):
        return self.coupon_code
