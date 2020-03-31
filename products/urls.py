from django.urls import path

from . import views

urlpatterns = [
   path('create',views.Create.as_view(),name='product.create'),
   path('<int:pk>',views.Show.as_view(),name='product.show'),
   path('<int:product_id>/upvote',views.upvote,name='product.upvote'),
   path('<int:product_id>/edit',views.edit,name='product.edit'),
   path('<int:product_id>/delte',views.delete,name='product.delete')
   
]