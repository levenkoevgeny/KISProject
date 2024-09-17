from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from kis.models import Cadet
from django.contrib.auth.decorators import login_required
from .models import Cadet


def main(request):
    return render(request, 'kis/main.html')


def cadet_list(request):
    cadet_list = Cadet.objects.all()
    return render(request, 'kis/cadet/list.html', {'cadet_list': cadet_list})


def add_cadet(request):
    return render(request, 'kis/cadet/add-form.html')


def update_cadet(request, cadet_pk):
    if request.method == 'POST':
        obj = get_object_or_404(Cadet, pk=cadet_pk)

        # form = ApplicantForm(request.POST, instance=obj)
        # if form.is_valid():
        #     form.save()
        #     back_path = request.session.get('back_path', '/')
        #     return HttpResponseRedirect(back_path)
        # else:
        #     return render(request, 'applicant/update_form.html', {'applicant_form': form,
        #                                                           'obj': obj,
        #                                                           })
    else:
        obj = get_object_or_404(Cadet, pk=cadet_pk)
        # form = ApplicantForm(instance=obj)
        return render(request, 'kis/cadet/update-form.html', {
            'obj': obj})
