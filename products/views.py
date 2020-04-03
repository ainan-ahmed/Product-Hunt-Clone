from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category,Product
from django.utils import timezone
from .forms import ProductCreateForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
# Create your views here.
class Home (ListView):
    context_object_name  = 'products'
    template_name = 'products/home.html'
    model = Product
    
class Show (DetailView):
    model = Product
    template_name = 'products/show.html'
    
class Create(LoginRequiredMixin,CreateView):
    model = Product
    template_name = 'products/create.html'
    form_class = ProductCreateForm
    
    def form_valid(self, form):
        form.instance.publication_date = timezone.datetime.now()
        form.instance.hunter = self.request.user
        return super().form_valid(form)

class Edit(LoginRequiredMixin,UpdateView):
    model = Product
    template_name = 'products/edit.html'
    form_class = ProductCreateForm

class Delete(LoginRequiredMixin,DeleteView):
    model = Product
    form_class = ProductCreateForm
    success_url = reverse_lazy("home")
    

@login_required
def upvote(request,product_id):
    product = Product.objects.get(id = product_id)
    if product.hunter == request.user:
        messages.error(request,"You can't upvote your own product")
        return redirect('/products/'+ str(product_id))
    product.total_votes +=1
    product.save()
    return redirect('/products/'+ str(product_id))

