from django.urls import path
from .views import send_mail_view, set_date, test_tags, MyFormView, products

urlpatterns = [
    path('send-mail/', send_mail_view, name='send_mail'),
    path('test-tags/', test_tags, name='test_tags'),
    path('create-task/', set_date, name='send_mail'),
    path('form-view/', MyFormView.as_view(), name='form_view'),
    path('products/', products, name="products")
]