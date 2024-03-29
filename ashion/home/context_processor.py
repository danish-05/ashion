from manage_category.models import Category
from logintohome.models import Customer
from manage_cart.models import Cart
from .models import Wishlist
from django.shortcuts import redirect


def category_nav(request):
    category = Category.objects.filter(is_listed=True)
    return {"cat": category}


def count_of_cart(request):
    cart_count = 0
    try:
        if "email" in request.session:
            email = request.session.get("email")
            user = Customer.objects.get(email=email)
            cart_count = Cart.objects.filter(user_id=user).count()

    except Customer.DoesNotExist:
        return redirect("login")     

    return {"cart_count": cart_count}


def wishlist_of_cart(request):
    wishlist_count = 0
    try:
        if "email" in request.session:
            email = request.session.get("email")
            user = Customer.objects.get(email=email)
            wishlist_count = Wishlist.objects.filter(user_id=user).count()

    except Customer.DoesNotExist:
        return redirect("login")

    return {"wishlist_count": wishlist_count}
