from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from kis.models import Cadet
from django.contrib.auth.decorators import login_required
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cadet, Punishment, Encouragement, RankHistory, Rank, EncouragementKind, PunishmentKind, \
    Speciality, Subdivision, Position, PositionHistory, OrderOwner, SpecialityHistory, EducationHistory, Reward, \
    RewardHistory, JobHistory, ArmyService, MVDService, CadetCategory
from .filters import CadetFilter, PunishmentFilter
from .serializers import CadetSerializer, RankSerializer, RankHistorySerializer, PunishmentSerializer, \
    PunishmentKindSerializer, EncouragementSerializer, EncouragementKindSerializer, SpecialitySerializer, \
    SubdivisionSerializer, OrderOwnerSerializer, PositionSerializer, PositionHistorySerializer, \
    SpecialityHistorySerializer, EducationHistorySerializer, JobHistorySerializer, RewardSerializer, \
    RewardHistorySerializer, ArmyServiceSerializer, MVDServiceSerializer, CadetCategorySerializer

from .forms import CadetForm
from docxtpl import DocxTemplate
from io import BytesIO
from django.http import FileResponse


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
        'address_residence': ['icontains'],
        'address_registration': ['icontains'],
        'personal_number_mvd': ['icontains'],
        'marital_status': ['exact'],
        'passport_number': ['exact'],
        'passport_issue_date': ['gte', 'lte'],
        'passport_validity_period': ['gte', 'lte'],
        'passport_issue_authority': ['exact'],
        'father_date_of_birth': ['gte', 'lte'],
        'mother_date_of_birth': ['gte', 'lte'],
        'subdivision': ['exact'],
        'group': ['exact'],
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
    filterset_fields = {'cadet': ['exact'],
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
    filterset_fields = {'cadet': ['exact'],
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


class EducationHistoryViewSet(APIBaseViewSet):
    queryset = EducationHistory.objects.all()
    serializer_class = EducationHistorySerializer
    filterset_fields = {
        'cadet': ['exact'],
        'education_kind': ['exact'],
        'education_level': ['exact'],
        'education_graduated': ['icontains'],
        'education_graduating_start_year': ['gte', 'lte'],
        'education_graduating_end_year': ['gte', 'lte'],
        'education_average_score': ['gte', 'lte'],
    }


class JobHistoryViewSet(APIBaseViewSet):
    queryset = JobHistory.objects.all()
    serializer_class = JobHistorySerializer
    filterset_fields = {
        'cadet': ['exact'],
        'job_position': ['icontains'],
        'job_start_year': ['gte', 'lte'],
        'job_end_year': ['gte', 'lte'],
        'organisation_name': ['icontains'],
    }


class RewardViewSet(APIBaseViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    filterset_fields = {
        'reward_title': ['icontains'],
    }


class RewardHistoryViewSet(APIBaseViewSet):
    queryset = RewardHistory.objects.all()
    serializer_class = RewardHistorySerializer
    filterset_fields = {
        'cadet': ['exact'],
        'reward': ['exact'],
        'reward_date': ['gte', 'lte'],
        'reason': ['icontains'],
        'order_owner': ['exact'],
        'order_number': ['icontains']
    }


class ArmyServiceViewSet(APIBaseViewSet):
    queryset = ArmyService.objects.all()
    serializer_class = ArmyServiceSerializer
    filterset_fields = {
        'cadet': ['exact'],
        'military_organization': ['icontains'],
        'military_service_start': ['gte', 'lte'],
        'military_service_end': ['gte', 'lte'],
        'position': ['icontains'],
        'order_owner': ['exact'],
        'order_date': ['gte', 'lte'],
        'order_number': ['icontains']
    }


class MVDServiceViewSet(APIBaseViewSet):
    queryset = MVDService.objects.all()
    serializer_class = MVDServiceSerializer
    filterset_fields = {
        'cadet': ['exact'],
        'mvd_organization': ['icontains'],
        'mvd_service_start': ['gte', 'lte'],
        'mvd_service_end': ['gte', 'lte'],
        'position': ['icontains'],
        'order_owner': ['exact'],
        'order_date': ['gte', 'lte'],
        'order_number': ['icontains']
    }


class CadetCategoryViewSet(APIBaseViewSet):
    queryset = CadetCategory.objects.all()
    serializer_class = CadetCategorySerializer
    filterset_fields = {
        'category': ['icontains'],
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


def get_document():
    doc = DocxTemplate("my_word_template.docx")
    context = {'company_name': "World company"}
    doc.render(context)
    byte_buffer = BytesIO()
    doc.save(byte_buffer)
    return byte_buffer, "ok_file.docx"


@api_view(['GET'])
def docx_test(request):
    byte_buffer, file_name = get_document()
    byte_buffer.seek(0)
    return FileResponse(byte_buffer, filename="ok.docx", as_attachment=True)
