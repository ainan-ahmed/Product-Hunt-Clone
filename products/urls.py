from django.urls import path

from . import views

urlpatterns = [
   path('create',views.Create.as_view(),name='product.create'),
   path('<int:pk>',views.Show.as_view(),name='product.show'),
   path('<int:product_id>/upvote',views.upvote,name='product.upvote'),
   path('<int:pk>/edit',views.Edit.as_view(),name='product.edit'),
   path('<int:pk>/delete',views.Delete.as_view(),name='product.delete')  
   
]