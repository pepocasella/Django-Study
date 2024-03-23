from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

# Create your views here.
def listing_list(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, "listings.html", context)


def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        'listing': listing
    }
    return render(request, "listing.html", context)


def linsting_create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add-listing')

    context = {
        'form': form
    }   
    return render(request, "listing_create.html", context)


def linsting_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add-listing')

    context = {
        'form': form
    }   
    return render(request, "listing_update.html", context)


def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/listings')