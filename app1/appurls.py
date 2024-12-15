from django.urls import path,include
from.import views
urlpatterns=[
    path('index1',views.index1,name='index1'),
    path('story',views.story,name='story'),
    path('products',views.products,name='products'),
    path('faq',views.faq,name='faq'),
    path('contact',views.contact,name='contact'),
    path('sign_in',views.sign_in,name='sign_in'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('contactpage',views.contactpage,name='contactpage'),
    path('shipping',views.shipping,name='shipping'),
    path('product_detail',views.product_detail,name='product_detail')





]