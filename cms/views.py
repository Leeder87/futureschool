from django.shortcuts import render, redirect
from .forms import UnitForm
# Create your views here.


def unit_new(request):
    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.content = form.cleaned_data['name'] + ' ' + form.cleaned_data['url']
            post.save()
            return redirect('admin/cms/')
    else:
        form = UnitForm()
        return render(request, 'unit/unit_edit.html', {'form': form})
