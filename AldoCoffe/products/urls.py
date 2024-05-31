from django.urls import path
from .views import product_list, product_list_by_category, feedback, send_feedback_email

urlpatterns = [
    path('', product_list, name='home'),
    path('category/<str:category_name>/', product_list_by_category, name='product_list_by_category'),
    path('feedback/', feedback, name='feedback'),
    path('send-feedback/', send_feedback_email, name='send_feedback_email'),
]
