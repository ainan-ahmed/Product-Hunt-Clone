from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category
# Create your views here.
def home (request):
    return render(request,'products/home.html')

@login_required
def create(request):
    # add url in the product model
    categories = Category.objects.all()
    return render(request,'products/create.html',{'categories':categories})