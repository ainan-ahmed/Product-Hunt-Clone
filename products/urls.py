from django.urls import path

from . import views

urlpatterns = [
   path('create',views.create,name='product.create'),
   path('<int:product_id>',views.show,name='product.show'),
   path('<int:product_id>/upvote',views.upvote,name='product.upvote'),
   path('<int:product_id>/edit',views.edit,name='product.edit'),
   path('<int:product_id>/delte',views.delete,name='product.delete')
   
]