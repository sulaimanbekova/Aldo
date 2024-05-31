from .models import Product, Category
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

def product_list(request, category_name=None):
    if category_name:
        category = Category.objects.get(name=category_name)
        products = Product.objects.filter(category=category)
        category_name = category.name
    else:
        products = Product.objects.all()
        category_name = "Все товары"
    categories = Category.objects.all()
    return render(request, 'items/index.html', {'products': products, 'categories': categories, 'category_name': category_name})



def product_list_by_category(request, category_name):
    category = Category.objects.get(name=category_name)
    products = Product.objects.filter(category=category)
    return render(request, 'items/index.html', {'products': products})

@require_POST
def send_feedback_email(request):
    message = request.POST.get('message', '')
    phone = request.POST.get('phone', '')
    email = request.POST.get('email', '')
    name = request.POST.get('name', '')

    subject = 'Feedback from website'
    # from_email = ''
    # to_email = ''
    body = f'Message: {message}\nPhone: {phone}\nEmail: {email}\nName: {name}'


    # send_mail(subject, body, from_email, [to_email])

    return redirect('home')

def feedback(request):
    return render(request, 'items/feedback.html')