from django.shortcuts import render, redirect
from .models import Coupon
from .forms import CouponForm
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == "POST":
        coupon_code_input = request.POST['code']
        coupon_code_input = str(coupon_code_input).strip()

        try:
            coupon_list = Coupon.objects.values_list('coupon_code', flat=True)
            # print(coupon_list)
            if coupon_code_input in coupon_list:
                coupon_obj = Coupon.objects.get(coupon_code=coupon_code_input)
                if coupon_obj.coupon_count == 6:
                    messages.error(request, f"This coupon is expired")
                    return redirect('home')

                messages.info(request, f"This coupon is redeemed {coupon_obj.coupon_count} times")
                return redirect('home')
            else:
                messages.error(request, "This code is not registered!")
                return redirect('home')

        except:
            pass

    return render(request, 'home.html')


def redeem(request):
    if request.method == "POST":
        redeem_code_input = request.POST['redeem_code']
        redeem_code_input = str(redeem_code_input).strip()

        try:
            coupon_list = Coupon.objects.values_list('coupon_code', flat=True)
            # print(coupon_list)
            if redeem_code_input in coupon_list:
                coupon_obj = Coupon.objects.get(coupon_code=redeem_code_input)
                if coupon_obj.coupon_count == 6:
                    messages.error(request, f"Can't redeem! This coupon is expired")
                    return redirect('home')
                coupon_obj.coupon_count += 1
                coupon_obj.save()

                messages.success(request, f"{redeem_code_input} is redeemed {coupon_obj.coupon_count} times.")
                return redirect('home')
            else:
                messages.error(request, "This code is not registered")
                return redirect('redeem')

        except:
            pass
    return render(request, 'redeem.html')


def add_coupon(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            coupon_code = form.cleaned_data['coupon_code']
            print(coupon_code)

            coupon = Coupon.objects.create(coupon_code= coupon_code)
            coupon.save()

            messages.success(request, f"{coupon_code} created successfully")
            return redirect('home')
    else:
        form = CouponForm()

    context = {
        'form': form,
    }
    return render(request, 'add_coupon.html', context)
