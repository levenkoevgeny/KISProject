from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from kis.models import Cadet
from django.contrib.auth.decorators import login_required
from .models import Cadet, Punishment, Encouragement, RankHistory
from .filters import CadetFilter, PunishmentFilter, EncouragementFilter, RankHistoryFilter


def main(request):
    return render(request, 'kis/main.html')


def cadet_list(request):
    request.session['back_path'] = '/kis/cadets?' + request.META.get('QUERY_STRING')
    qs = Cadet.objects.all()
    if 'o' in request.GET:
        order_query = request.GET['o'].split('.')
        qs = qs.order_by(*order_query)
    f = CadetFilter(request.GET, queryset=qs)
    paginator = Paginator(f.qs, 20)
    page = request.GET.get('page')
    cad_list = paginator.get_page(page)
    return render(request, 'kis/cadet/cadet-list.html',
                  {'cadet_list': cad_list, 'filter': f})


def add_cadet(request):
    return render(request, 'kis/cadet/cadet-input-form.html')


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
        punishments = Punishment.objects.filter(punishment_cadet=obj)
        encouragements = Encouragement.objects.filter(encouragement_cadet=obj)
        rank_history = RankHistory.objects.filter(cadet=obj).order_by('-rank_date')
        # form = ApplicantForm(instance=obj)
        return render(request, 'kis/cadet/cadet-update-form.html',
                      {'obj': obj, 'punishments': punishments, 'encouragements': encouragements,
                       'rank_history': rank_history})


def punishment_list(request):
    request.session['back_path'] = '/kis/punishments?' + request.META.get('QUERY_STRING')
    qs = Punishment.objects.all()
    if 'o' in request.GET:
        order_query = request.GET['o'].split('.')
        qs = qs.order_by(*order_query)
    f = PunishmentFilter(request.GET, queryset=qs)
    paginator = Paginator(f.qs, 20)
    page = request.GET.get('page')
    punish_list = paginator.get_page(page)
    cad_list = Cadet.objects.all()
    return render(request, 'kis/punishment/punishment-list.html',
                  {
                      'punishment_list': punish_list,
                      'cadet_list': cad_list, 'filter': f
                  })
