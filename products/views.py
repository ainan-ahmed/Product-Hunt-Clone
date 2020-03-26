from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category,Product
from django.utils import timezone
# Create your views here.
def home (request):
    products = Product.objects.all()
    return render(request,'products/home.html',{'products':products})

@login_required
def create(request):
    if request.method=='POST':
        category  = Category.objects.get(name = request.POST['category'])
        product = Product()
        product.title = request.POST['title']
        product.body = request.POST['body']
        product.category = category
        product.icon = request.FILES['icon']
        product.image = request.FILES['image']
        product.publication_date = timezone.datetime.now()
        product.hunter = request.user 
        product.save()
        return redirect('home')
    else:
        categories = Category.objects.all()
        return render(request,'products/create.html',{'categories':categories})
    
def show(request,product_id):
    product = get_object_or_404(Product,pk = product_id)
    return render(request,'products/show.html',{'product':product})
@login_required
def upvote(request,product_id):
    product = Product.objects.get(id = product_id)
    if product.hunter == request.user:
        upvote_error = "You can't upvote your own product"
        return redirect('/products/'+ str(product_id))
    product.total_votes +=1
    product.save()
    return redirect('/products/'+ str(product_id))
@login_required
def edit(request,product_id):
    print('adsf')
@login_required
def delete(request,product_id):
    print('adsf')