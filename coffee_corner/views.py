"""
Views for Coffee Corner
"""

from django.shortcuts import (
    render, redirect, reverse)
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def coffee_corner(request):
    """
    A view to return the coffee_corner page
    """
    if not request.user.is_authenticated:
        messages.error(
            request, 'You must be logged in to see the Coffee Corner')
        return redirect(reverse('login'))
    return render(request, 'coffee_corner/coffee_corner.html')
