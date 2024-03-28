from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, DateRangeForm, AddCustomerForm, AddProductForm, AddTranRecordForm
from .models import Record
from .models import TranRec
from .models import TranSacRec
from .models import Customer
from .models import Product
from django.db import models



def home(request):
	records = Record.objects.all()

	

	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records})



def ad(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            # Filter records based on the date range
            filtered_records = TranSacRec.objects.filter(date__range=[start_date, end_date])
			   
            # Pass the filtered records to the template as context
            return render(request, 'ad.html', {'form': form, 'records': filtered_records, 'tot_amt' : filtered_records.aggregate(total=models.Sum('price'))['total'] })
    else:
            form = DateRangeForm()
    return render(request, 'ad.html', {'form': form})


            
		    

    



def login_user(request):
	pass

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
	
def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_record(request):

	form = AddTranRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":

			if form.is_valid():
				form.save()

				messages.success(request, "Record Added...")
				return redirect('home')
			
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")

		return redirect('home')
	



def add_product(request):
	form = AddProductForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_product = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_product.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	
def add_customer(request):
	form = AddCustomerForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_customer = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_customer.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	
	




def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	
def listcust(request):
    cus = Customer.objects.all()
    return render(request, 'cus_list.html', {'records': cus})

def listpro(request):
    product = Product.objects.all()
    return render(request, 'pro_list.html', {'records': product})