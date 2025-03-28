from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor

from listings.choices import price_choices, state_choices, bedroom_choices

def index(request):
    latest_listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'latest_listings': latest_listings,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    team = Realtor.objects.order_by('-hire_date')
    mvp = Realtor.objects.get(is_mvp=True)

    context = {
        'team': team,
        'mvp': mvp,
    }

    return render(request, 'pages/about.html', context)
