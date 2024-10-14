from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from kis.models import Cadet
from django.contrib.auth.decorators import login_required
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cadet, Punishment, Encouragement, RankHistory, Rank, EncouragementKind, PunishmentKind, \
    Speciality, Subdivision, Position, PositionHistory, OrderOwner, SpecialityHistory
from .filters import CadetFilter, PunishmentFilter
from .serializers import CadetSerializer, RankSerializer, RankHistorySerializer, PunishmentSerializer, \
    PunishmentKindSerializer, EncouragementSerializer, EncouragementKindSerializer, SpecialitySerializer, \
    SubdivisionSerializer, OrderOwnerSerializer, PositionSerializer, PositionHistorySerializer, \
    SpecialityHistorySerializer

from .forms import CadetForm


class APIBaseViewSet(viewsets.ModelViewSet):
    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


def main(request):
    cadet_form = CadetForm()
    return render(request, 'kis/main.html', {'form': cadet_form})


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
class CadetViewSet(APIBaseViewSet):
    queryset = Cadet.objects.all()
    serializer_class = CadetSerializer
    filterset_fields = {
        'last_name_rus': ['icontains'],
        'first_name_rus': ['icontains'],
        'last_name_bel': ['icontains'],
        'first_name_bel': ['icontains'],
        'last_name_en': ['icontains'],
        'first_name_en': ['icontains'],
        'date_of_birth': ['gte', 'lte'],
        'address': ['icontains'],
        'passport_number': ['exact'],
        'passport_issue_date': ['gte', 'lte'],
        'passport_validity_period': ['gte', 'lte'],
        'passport_issue_authority': ['exact'],
        'father_date_of_birth': ['gte', 'lte'],
        'mother_date_of_birth': ['gte', 'lte'],
        'education_level': ['exact'],
        'education_graduated': ['icontains'],
        'education_graduating_year': ['gte', 'lte'],
        'education_average_score': ['gte', 'lte'],
        'education_kind': ['exact'],
        'education_location_kind': ['exact'],
        'subdivision': ['exact'],
        'academy_start_year': ['gte', 'lte'],
        'academy_end_year': ['gte', 'lte'],
        'component_organ': ['exact'],
        'entrance_category': ['exact'],
        'arrived_from_go_rovd': ['exact'],
        'social_status': ['exact'],
        'region_for_medical_examination': ['exact'],
        'military_office': ['exact'],
        'extra_data': ['icontains'],
    }


class RankViewSet(APIBaseViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer


class RankHistoryViewSet(APIBaseViewSet):
    queryset = RankHistory.objects.all()
    serializer_class = RankHistorySerializer
    filterset_fields = {'cadet': ['exact'],
                        'rank': ['exact'],
                        'rank_date': ['gte', 'lte'],
                        'rank_order_date': ['gte', 'lte'],
                        'rank_order_number': ['icontains'],
                        'rank_order_owner': ['exact'],
                        'rank_extra_data': ['icontains'],
                        }


class EncouragementKindViewSet(APIBaseViewSet):
    queryset = EncouragementKind.objects.all()
    serializer_class = EncouragementKindSerializer


class EncouragementViewSet(APIBaseViewSet):
    queryset = Encouragement.objects.all()
    serializer_class = EncouragementSerializer
    filterset_fields = {'encouragement_cadet': ['exact'],
                        'encouragement_kind': ['exact'],
                        'encouragement_date': ['gte', 'lte'],
                        'encouragement_order_date': ['gte', 'lte'],
                        'encouragement_order_number': ['icontains', ],
                        'encouragement_order_owner': ['exact', ],
                        'encouragement_extra_data': ['icontains'],
                        }


class PunishmentViewSet(APIBaseViewSet):
    queryset = Punishment.objects.all()
    serializer_class = PunishmentSerializer
    filterset_fields = {'punishment_cadet': ['exact'],
                        'punishment_kind': ['exact'],
                        'punishment_start_date': ['gte', 'lte'],
                        'punishment_start_order_date': ['gte', 'lte'],
                        'punishment_start_order_number': ['icontains'],
                        'punishment_start_order_owner': ['exact'],
                        'punishment_start_extra_data': ['icontains'],
                        'punishment_expiration_date': ['gte', 'lte'],
                        'punishment_expiration_order_date': ['gte', 'lte'],
                        'punishment_expiration_order_number': ['icontains'],
                        'punishment_expiration_order_owner': ['exact'],
                        'punishment_expiration_extra_data': ['icontains'],
                        }


class PunishmentKindViewSet(APIBaseViewSet):
    queryset = PunishmentKind.objects.all()
    serializer_class = PunishmentKindSerializer


class SpecialityViewSet(APIBaseViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class SubdivisionViewSet(APIBaseViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer


class OrderOwnerViewSet(APIBaseViewSet):
    queryset = OrderOwner.objects.all()
    serializer_class = OrderOwnerSerializer


class PositionViewSet(APIBaseViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionHistoryViewSet(APIBaseViewSet):
    queryset = PositionHistory.objects.all()
    serializer_class = PositionHistorySerializer
    filterset_fields = {'cadet': ['exact'],
                        'position': ['exact'],
                        'position_date': ['gte', 'lte'],
                        'position_order_date': ['gte', 'lte'],
                        'position_order_number': ['icontains'],
                        'position_order_owner': ['exact'],
                        'position_extra_data': ['icontains'],
                        }


class SpecialityHistoryViewSet(APIBaseViewSet):
    queryset = SpecialityHistory.objects.all()
    serializer_class = SpecialityHistorySerializer
    filterset_fields = {
        'cadet': ['exact'],
        'speciality': ['exact'],
        'speciality_order_date': ['gte', 'lte'],
        'speciality_order_number': ['icontains'],
        'speciality_order_owner': ['exact'],
        'speciality_extra_data': ['icontains'],
    }


@api_view(['GET'])
def models_fields_list(request):
    models_fields = {}
    import django.apps
    for model in django.apps.apps.get_models():
        fields = [f.name for f in model._meta.fields + model._meta.many_to_many]
        models_fields[model.__name__] = fields
    return Response(models_fields, status=status.HTTP_200_OK)


@api_view(['GET'])
def connection_test(request):
    return Response('Connection is Ok!!!', status=status.HTTP_200_OK)
