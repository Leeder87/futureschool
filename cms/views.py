from django.shortcuts import render, redirect
from .forms import UnitForm
import json
# Create your views here.
from .models import Unit


def unit_new(request):
    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            content = {}
            for data in form.cleaned_data:
                if form.cleaned_data[data] != '' and form.cleaned_data[data] is not None:
                    if type(form.cleaned_data[data]) is Unit:
                        content.update({data: form.cleaned_data[data].pk})
                    else:
                        content.update({data: form.cleaned_data[data]})

            post.content = json.dumps(content)
            post.save()
            return redirect('admin/cms/')
        #{'text': 'Сколько будет 2 + 2 = 4?', 'url': '', 'answer': 'True', 'right_comment': '', 'wrong_comment': 'Обрати внимание на логику!', 'right_extra': None, 'wrong_extra': <Unit: Unit object (6)>, 'unit_type': 'at'}
    else:
        form = UnitForm()
        return render(request, 'unit/unit_edit.html', {'form': form})
