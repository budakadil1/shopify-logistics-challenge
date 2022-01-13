from django.shortcuts import render, redirect
from django.urls import reverse
from .models import inventory, wareHouse
from inventory.forms import WareHouseForm, InventoryForm
def index(request):
    try:
        inventory_query = inventory.objects.all()
        inv_count = inventory.objects.count()
    except:
        return render(request, 'main.html', {'no_objects':'No Objects Found! Add Some!'})
    return render(request, 'main.html', {'inventories': inventory_query, 'inv_count':inv_count})

def add_inventory(request):
    if request.method == 'GET':
        form = InventoryForm()
        return render(request, 'add_inventory.html', {'form' : form})
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'add_inventory.html', {'exception':True})

def add_warehouse(request):
    if request.method == 'GET':
        form = WareHouseForm()
        return render(request, 'add_warehouse.html', {'form' : form})
    if request.method == 'POST':
        form = WareHouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'add_warehouse.html')

def edit_inventory(request, id):
    if request.method == 'GET':
        # if object
        try:
            instance = inventory.objects.get(id=id)
            form = InventoryForm(instance=instance)
        except: #includes validationerror for uuid and DoesNotExist
            return render(request, 'add_inventory.html', {'notfound' : True})
        
        return render(request, 'add_inventory.html', {'form' : form})
    if request.method == 'POST':
        # if object is deleted somehow before edit goes through
        try:
            instance = inventory.objects.get(id=id)
            form = InventoryForm(request.POST, instance=instance)
        except:
            return render(request, 'add_inventory.html', {'exception' : True})
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            # if form fails (i.e warehouse is deleted while tab is open)
            return render(request, 'add_inventory.html', {'exception':True})

def delete_inventory(request, id):
    try:
        instance = inventory.objects.get(id=id)
        instance.delete()
        return redirect(reverse('index'))
    except:
        return redirect(reverse('index'))