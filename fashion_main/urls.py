from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from carts import views as CartViews
from accounts import views as AccountViews
from newsletters import views as NewsletterViews
from products import views as ProductViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),

    # Business
    path('business/', include('business.urls')),

    # Users
    path('userLogin/', AccountViews.userLogin, name='userLogin'),
    path('userDashboard/', AccountViews.userDashboard, name='userDashboard'),
    path('userRegister/', AccountViews.userRegister, name='userRegister'),
    path('logout/', AccountViews.logout, name='logout'),
    path('activate/<uidb64>/<token>/', AccountViews.activate, name='activate'),
    path('forgotPassword/', AccountViews.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', AccountViews.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', AccountViews.resetPassword, name='resetPassword'),

    # Smart select field
    path('chaining/', include('smart_selects.urls')),

    # Shop
    path('shop/', include('products.urls')),

    # Cart
    path('cart/', include('carts.urls')),
    path('shopcart/', CartViews.shopcart, name='shopcart'),

    # Ajax color
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),

    # Newsletters
    path('subscribe/', NewsletterViews.email_list_subscribe, name='subscribe'),

    # Wishlist
    path('my-wishlist/', ProductViews.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>', ProductViews.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist_addtoshopcart/<int:product_id>/', ProductViews.wishlist_addtoshopcart, name='wishlist_addtoshopcart'),
    path('wishlist_delete/<int:id>/', ProductViews.wishlist_delete, name='wishlist_delete'),

    # Search
    path('search/', ProductViews.search, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
