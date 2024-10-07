from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from kis.models import Cadet
from django.contrib.auth.decorators import login_required
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .models import Cadet, Punishment, Encouragement, RankHistory, Rank, EncouragementKind, PunishmentKind, Group, \
    Speciality, Subdivision
from .filters import CadetFilter, PunishmentFilter, EncouragementFilter, RankHistoryFilter
from .serializers import CadetSerializer, RankSerializer, RankHistorySerializer, PunishmentSerializer, \
    PunishmentKindSerializer, EncouragementSerializer, EncouragementKindSerializer, SpecialitySerializer, \
    GroupSerializer, SubdivisionSerializer


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


# REST
class CadetViewSet(viewsets.ModelViewSet):
    queryset = Cadet.objects.all()
    serializer_class = CadetSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RankViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RankHistoryViewSet(viewsets.ModelViewSet):
    queryset = RankHistory.objects.all()
    serializer_class = RankHistorySerializer
    filterset_fields = {'cadet': ['exact'],
                        'rank': ['exact'],
                        'rank_date': ['gte', 'lte'],
                        'extra_data': ['icontains'],
                        }

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EncouragementKindViewSet(viewsets.ModelViewSet):
    queryset = EncouragementKind.objects.all()
    serializer_class = EncouragementKindSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EncouragementViewSet(viewsets.ModelViewSet):
    queryset = Encouragement.objects.all()
    serializer_class = EncouragementSerializer
    filterset_fields = {'encouragement_cadet': ['exact'],
                        'encouragement_kind': ['exact'],
                        'encouragement_date': ['gte', 'lte'],
                        'encouragement_extra_data': ['icontains'],
                        }

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PunishmentViewSet(viewsets.ModelViewSet):
    queryset = Punishment.objects.all()
    serializer_class = PunishmentSerializer
    filterset_fields = {'punishment_cadet': ['exact'],
                        'punishment_kind': ['exact'],
                        'punishment_start_date': ['gte', 'lte'],
                        'punishment_expiration_date': ['gte', 'lte'],
                        'punishment_extra_data': ['icontains'],
                        }

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PunishmentKindViewSet(viewsets.ModelViewSet):
    queryset = PunishmentKind.objects.all()
    serializer_class = PunishmentKindSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubdivisionViewSet(viewsets.ModelViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
