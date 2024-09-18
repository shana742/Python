
from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductMst, ProductSubCat
from .forms import ProductForm, ProductSubCatForm

# Admin view to display all products
def admin_product_list(request):
    products = ProductSubCat.objects.all()
    return render(request, 'admin_product_list.html', {'products': products})

# Admin view to add a new product
def admin_add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductForm()
    return render(request, 'admin_add_product.html', {'form': form})

# Admin view to add a product subcategory
def admin_add_subcat(request):
    if request.method == 'POST':
        form = ProductSubCatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductSubCatForm()
    return render(request, 'admin_add_subcat.html', {'form': form})

# Admin view to edit product
def admin_edit_product(request, pk):
    product = get_object_or_404(ProductSubCat, pk=pk)
    if request.method == 'POST':
        form = ProductSubCatForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductSubCatForm(instance=product)
    return render(request, 'admin_edit_product.html', {'form': form})

# Admin view to delete product
def admin_delete_product(request, pk):
    product = get_object_or_404(ProductSubCat, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_product_list')
    return render(request, 'admin_delete_product.html', {'product': product})



from django.db.models import Q

# Product Manager search view
def product_search(request):
    query = request.GET.get('q')
    products = []
    if query:
        products = ProductSubCat.objects.filter(
            Q(product__product_name__icontains=query) |
            Q(model__icontains=query)
        )
    return render(request, 'product_search.html', {'products': products})


def home(request):
    return render(request, 'home.html')

