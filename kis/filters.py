import django_filters
from django import forms

from .models import Cadet, Punishment, PunishmentKind, Encouragement, EncouragementKind, RankHistory, Rank, Speciality, Group

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})


class CadetFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(field_name='last_name_rus', lookup_expr='icontains')
    address = django_filters.CharFilter(field_name='address', lookup_expr='icontains')
    school_graduating_year_gte = django_filters.NumberFilter(field_name='school_graduating_date__year', lookup_expr='gte')
    school_graduating_year_lte = django_filters.NumberFilter(field_name='school_graduating_date__year', lookup_expr='lte')
    school_average_score_gte = django_filters.NumberFilter(field_name='school_average_score', lookup_expr='gte')
    school_average_score_lte = django_filters.NumberFilter(field_name='school_average_score', lookup_expr='lte')
    speciality = django_filters.ModelMultipleChoiceFilter(field_name='speciality',
                                                        queryset=Speciality.objects.all())
    group = django_filters.ModelMultipleChoiceFilter(field_name='group',
                                                        queryset=Group.objects.all())



    class Meta:
        model = Cadet
        fields = []


class PunishmentFilter(django_filters.FilterSet):
    punishment_cadet = django_filters.ModelChoiceFilter(field_name='punishment_cadet',
                                                        queryset=Cadet.objects.all())
    punishment_kind = django_filters.ModelMultipleChoiceFilter(field_name='punishment_kind',
                                                               queryset=PunishmentKind.objects.all())
    punishment_start_date_gte = django_filters.DateFilter(field_name='punishment_start_date', lookup_expr='gte',
                                                          widget=myDateInput)
    punishment_start_date_lte = django_filters.DateFilter(field_name='punishment_start_date', lookup_expr='lte',
                                                          widget=myDateInput)
    punishment_expiration_date_gte = django_filters.DateFilter(field_name='punishment_expiration_date',
                                                               lookup_expr='gte', widget=myDateInput)
    punishment_expiration_date_lte = django_filters.DateFilter(field_name='punishment_expiration_date',
                                                               lookup_expr='lte', widget=myDateInput)

    class Meta:
        model = Punishment
        fields = []


class EncouragementFilter(django_filters.FilterSet):
    encouragement_cadet = django_filters.ModelChoiceFilter(field_name='punishment_cadet',
                                                           queryset=Cadet.objects.all())
    encouragement_kind = django_filters.ModelMultipleChoiceFilter(field_name='punishment_kind',
                                                                  queryset=EncouragementKind.objects.all())
    encouragement_date_gte = django_filters.DateFilter(field_name='encouragement_date', lookup_expr='gte',
                                                       widget=myDateInput)
    encouragement_date_lte = django_filters.DateFilter(field_name='encouragement_date', lookup_expr='lte',
                                                       widget=myDateInput)

    class Meta:
        model = Encouragement
        fields = []


class RankHistoryFilter(django_filters.FilterSet):
    cadet = django_filters.ModelChoiceFilter(field_name='cadet',
                                             queryset=Cadet.objects.all())
    rank = django_filters.ModelMultipleChoiceFilter(field_name='rank',
                                                    queryset=Rank.objects.all())
    rank_date_gte = django_filters.DateFilter(field_name='rank_date', lookup_expr='gte',
                                                       widget=myDateInput)
    rank_date_lte = django_filters.DateFilter(field_name='rank_date', lookup_expr='lte',
                                              widget=myDateInput)

    class Meta:
        model = RankHistory
        fields = []
