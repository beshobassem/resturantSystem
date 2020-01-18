from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns= [
    path('signin/', signin, name='sign'),
    path('signinback/', signinBack, name='signback'),
    path('log/',  log, name='login'),
    path('logback/', logBack, name='logback'),
    path('home/', home, name='home'),
    path('home2/', home2, name='home2'),
    path('logoutback/', logoutBack, name='logoutback'),
    path('foodORdrink/', menu, name='foodORdrink'),
    path('food/', food, name='food'),
    path('drink/', drink, name='drink'),
    path('services/', ser, name='ser'),
    path('order/', order, name='order'),
    path('orderform/', orderform, name='orderform'),
    path('cart/', cart, name='cart'),
    path('cartupdate/<int:id>/', cartupdate, name='cartupdate'),
    path('update/<int:id>/' , update , name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('order2/',order2 , name='order2'),
    path('orderform2/', orderform2, name='orderform2'),
    path('cart2/', cart2, name='cart2'),
    path('cartupdate2/<int:id>/', cartupdate2, name='cartupdate2'),
    path('update2/<int:id>/' , update2 , name='update2'),
    path('delete2/<int:id>/', delete2, name='delete2'),
    path('table/',table , name='table'),
    path('tableform/', tableform, name='tableform'),
    path('tablecart/', tablecart, name='tablecart'),
    path('tableupdate/<int:id>/', tableupdate, name='tableupdate'),
    path('update3/<int:id>/' , update3 , name='update3'),
    path('tabledelete/<int:id>/', tabledelete, name='tabledelete'),
    path('birthday/',birthday , name='birthday'),
    path('birthdayform/', birthdayform, name='birthdayform'),
    path('birthdaycart/', birthdaycart, name='birthdaycart'),
    path('birthdayupdate/<int:id>/', birthdayupdate, name='birthdayupdate'),
    path('update4/<int:id>/' , update4 , name='update4'),
    path('birthdaydelete/<int:id>/', birthdaydelete, name='birthdaydelete'),
]
