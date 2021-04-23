from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addwishlist/", views.WishlistCreate.as_view(), name="add_wishlist"),
    path("delete/<int:wishlist_id>/", views.delete_wishlist, name="delete_wishlist")
]