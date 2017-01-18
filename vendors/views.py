from django.shortcuts import render
from django.urls import reverse


def vendor_profile(request, vendor_id):
    return render(request, 'vendors/vendor-profile.html', {})