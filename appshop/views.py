from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, UpdateView
from .models import MyUser, Product, Purchase
from django.contrib.auth import authenticate, login
from .forms import AutUserForm, RegisterUserView, CreateProductViewForm, UpdateProductViewForm, ReturnProductForm, BuyProductForm


def index(request):
	return render(request, 'index.html')


class RegisterUserView(CreateView):
	models = MyUser
	form_class = RegisterUserView
	template_name = 'register.html'
	success_url = '/'
	def get_success_url(self):
		return self.success_url
	def post(self, request, *args, **kwargs):
		print(request.POST)
		return super().post(self, request, *args, **kwargs)
	def form_valid(self, form):
		form_valid = super().form_valid(form)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		aut_user = authenticate(username=username, password=password)
		login(self.request, aut_user)
		return form_valid

class MyloginView(LoginView):
	template_name = 'login.html'
	form_class = AutUserForm
	success_url = '/'
	def get_success_url(self):
		return self.success_url


class MyUserlogout(LogoutView):
	next_page = '/'


class ProductView(ListView):
	model = Product
	template_name = 'index.html'


class ProductListView(ListView):
	model = Product
	template_name = 'product_list.html'
	content_object_name = 'pl'


class CreateProductView(CreateView):
	model = Product
	form_class = CreateProductViewForm
	template_name = 'create_product.html'
	success_url = '/'

class UpdateProductView(UpdateView):
	model = Product
	template_name = 'update_product.html'
	success_url = '/'
	form_class = UpdateProductViewForm


class ReturnProductView(ListView):
	model = Product
	template_name = 'return_product.html'
	form_class = ReturnProductForm


class BuyProductView(CreateView):
	model = Purchase
	template_name = 'product_buy.html'
	form_class = BuyProductForm
	success_url = '/'
	def form_valid(self, form):
		object = form.save(commit=False)
		object.user = self.request.user
		object.product = Product.objects.get(id=self.request.POST['product_pk'])
		print(self.request.POST['product_pk'])
		# object.save()
		return super().form_valid(form=form)
