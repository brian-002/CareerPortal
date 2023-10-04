from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from django.db.models import Q

from .forms import NewItemForm, EditItemForm

from .models import Item, Department

def items(request):
    query = request.GET.get('query', '')
    department_id = request.GET.get('department', 0)
    departments = Department.objects.all()
    items = Item.objects.filter(available = True)

    if department_id:
        items = items.filter(department_id = department_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains = query))

    return render(request, 'item/items.html', {
        'items':items,
        'query':query,
        'departments':departments,
        'department_id':int(department_id)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'item/detail.html', {
        'item':item,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form =NewItemForm()

    form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by = request.user)


    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance = item)

    form = EditItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by = request.user)
    item.delete()

    return render(request, 'Controlpanel/index.html')
