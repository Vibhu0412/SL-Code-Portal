from django import forms
from .models import Coupon


class CouponForm(forms.ModelForm):

    confirm_coupon = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Confirm Coupon',
        'class': 'form-control'
    }))

    class Meta:
        model = Coupon
        fields = ['coupon_code']

    def __init__(self, *args, **kwargs):
        super(CouponForm, self).__init__(*args, **kwargs)
        self.fields['coupon_code'].widget.attrs['placeholder'] = 'Enter Coupon'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(CouponForm, self).clean()
        coupon_code = cleaned_data.get('coupon_code')
        confirm_coupon = cleaned_data.get('confirm_coupon')

        if coupon_code != confirm_coupon:
            raise forms.ValidationError("Coupons does not match!")
