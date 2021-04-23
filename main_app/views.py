from django.shortcuts import render, redirect
from .models import Wishlist
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    wishlists = Wishlist.objects.all()
    return render(request, 'index.html', { 'wishlists': wishlists })

class WishlistCreate(CreateView):
    model = Wishlist
    fields = "__all__"

def delete_wishlist(request, wishlist_id):
    Wishlist.objects.get(id=wishlist_id).delete()
    return redirect("/")