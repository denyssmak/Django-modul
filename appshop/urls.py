from django.urls import include, path
from .views import ProductView, MyloginView, RegisterUserView, MyUserlogout, CreateProductView, UpdateProductView, ReturnProductView, ProductListView, BuyProductView


urlpatterns = [
    path('', ProductView.as_view(), name='index'),
    path('login/', MyloginView.as_view(), name='login_page'),
    path('register/', RegisterUserView.as_view(), name='register_page'),
    path('logout/', MyUserlogout.as_view(), name='logout_page'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
    path('return_product/', ReturnProductView.as_view(), name='return_product'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_buy/<int:pk>/', BuyProductView.as_view(), name='product_buy'),
]