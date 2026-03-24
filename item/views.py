from django.shortcuts import render, get_object_or_404, redirect
from .models import Items
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm


def detail(request, pk):
    item =get_object_or_404(Items, pk=pk)
    related_item = Items.objects.filter(Category=item.Category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html',{
        'item': item,
        'related_items': related_item
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail',pk=item.id)

    else:        
        form = NewItemForm()

    return render(request, 'item/form.html',{
        'form': form,
        'title': 'New item'
    })


@login_required
def delect(request, pk):
    item = get_object_or_404(Items, pk=pk, created_by=request.user)
    item.delete()


    return redirect('dashboard:index')