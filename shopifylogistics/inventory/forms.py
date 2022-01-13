from django import forms
from django.forms import ModelForm
from .models import inventory, wareHouse

# form for adding inventory
class InventoryForm(ModelForm):
    class Meta:
        model = inventory
        fields = ['name', 'SKU', 'warehouse']
    
    warehouse = forms.ModelChoiceField(wareHouse.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(InventoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Inventory Name:"
        self.fields['SKU'].label = "Inventory SKU (optional):"
        self.fields['warehouse'].label = "Warehouse (optional):"

    
class WareHouseForm(ModelForm):
    class Meta:
        model = wareHouse
        fields = ['name', 'address']
    
    def __init__(self, *args, **kwargs):
        super(WareHouseForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Warehouse Name:"
        self.fields['address'].label = "Warehouse Address (optional):"
        self.fields['address'].required = False

class EditInventoryForm(ModelForm):
    class Meta:
        model = inventory
        fields = ['name', 'SKU', 'warehouse']
    
    def __init__(self, *args, **kwargs):
        super(EditInventoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Inventory Name:"
        self.fields['SKU'].label = "Inventory SKU (optional):"
        self.fields['warehouse'].label = "Warehouse (optional):"
