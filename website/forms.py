from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from .models import TranRec
from .models import TranSacRec
from .models import Product
from .models import Customer

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	date = forms.DateField(required=True, input_formats=['%d-%m-%Y'])
	material = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Material", "class":"form-control"}), label="")
	quantity = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Quantity", "class":"form-control"}), label="")
	price = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Price", "class":"form-control"}), label="")

	class Meta:
		model = TranRec
		exclude = ("user",)

class DateRangeForm(forms.Form):
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type': 'date'}))







# Create Add Record Form
class AddTranRecordForm(forms.ModelForm):

	class Meta:
		model = TranSacRec
		fields = '__all__'
		

# Create Add Record Form
class AddCustomerForm(forms.ModelForm):
	customer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Customer Code", "class":"form-control"}), label="")
	cusdes   = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Customer Description", "class":"form-control"}), label="")
	class Meta:
		model = Customer
		exclude = ("user",)

# Create Add Record Form
class AddProductForm(forms.ModelForm):
	product = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Product Code", "class":"form-control"}), label="")
	prodes   = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Product Description", "class":"form-control"}), label="")

	class Meta:
		model = Product
		exclude = ("user",)