# pylint: disable=missing-module-docstring
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    Display the user's profile, default information and past orders
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update Failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Display the users past oder in detail.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        'This is a past order.'
    ))

    template = 'checkout/order_history.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
