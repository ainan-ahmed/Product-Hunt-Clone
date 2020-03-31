from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category,Product
from django.utils import timezone
from .forms import ProductCreateForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
# Create your views here.
class Home (ListView):
    context_object_name  = 'products'
    template_name = 'products/home.html'
    model = Product
    
class Show (DetailView):
    model = Product
    template_name = 'products/show.html'
    
class Create(CreateView):
    template_name = 'products/create.html'
    form_class = ProductCreateForm
    
    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.publication_date = timezone.datetime.now()
        self.object.hunter = self.request.user
        
# @login_required
# def create(request):
#     if request.method=='POST':
#         form = ProductCreateForm(request.POST,request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.publication_date = timezone.datetime.now() 
#             product.hunter = request.user
#             product.save()
#             return redirect('/products/'+ str(product.id))
#     else:
#         form = ProductCreateForm()
#         return render(request,'products/create.html',{'form':form})

@login_required
def upvote(request,product_id):
    product = Product.objects.get(id = product_id)
    if product.hunter == request.user:
        messages.error(request,"You can't upvote your own product")
        return redirect('/products/'+ str(product_id))
    product.total_votes +=1
    product.save()
    return redirect('/products/'+ str(product_id))

@login_required
def edit(request,product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product,pk = product_id)
        form = ProductCreateForm(instance=product)
        return render(request,'products/edit.html',{'form':form,'product':product})
    else:
        form = ProductCreateForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            product = Product.objects.get(id = product_id)
            form.save()
            return redirect('/products/'+ str(product_id))

@login_required
def delete(request,product_id):
    print('adsf')