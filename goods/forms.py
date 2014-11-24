from django.forms import ModelForm
from goods.models import Goods

class GoodForm(ModelForm):
	class Meta:
		model = Goods
		fields	= ['id_good', 'name', 'price', 'image', 'stock', 'description']

class EditProductForm(ModelForm):
	class Meta:
		model = Goods
		fields = ['name', 'price', 'image', 'stock', 'description']
		
	
