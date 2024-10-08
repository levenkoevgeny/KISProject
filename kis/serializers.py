from rest_framework import serializers
from kis.models import (Cadet, Rank, PassportIssueAuthority, Speciality, Subdivision, Group,
                        Punishment, PunishmentKind, EncouragementKind, Encouragement, RankHistory)


class CadetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadet
        fields = [
            'id',
            'last_name_rus',
            'first_name_rus',
            'patronymic_rus',
            'last_name_bel',
            'first_name_bel',
            'patronymic_bel',
            'last_name_en',
            'first_name_en',
            'patronymic_en',
            'date_of_birth',
            'photo',
            'address',
            'passport_number',
            'passport_issue_date',
            'passport_validity_period',
            'passport_issue_authority',
            'father_last_name',
            'father_first_name',
            'father_patronymic',
            'father_date_of_birth',
            'father_place_of_work',
            'father_phone_number',
            'mother_last_name',
            'mother_first_name',
            'mother_patronymic',
            'mother_date_of_birth',
            'mother_place_of_work',
            'mother_phone_number',
            'school_graduated',
            'school_graduating_date',
            'school_average_score',
            'speciality',
            'group',
            'academy_start_year',
            'academy_end_year',
            'get_full_name'
        ]


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = '__all__'


class PassportIssueAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportIssueAuthority
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'


class SubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PunishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punishment
        fields = ['id', 'punishment_cadet', 'punishment_kind', 'punishment_start_date', 'punishment_expiration_date',
                  'punishment_extra_data', 'get_punishment_kind_str']


class PunishmentKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = PunishmentKind
        fields = '__all__'


class EncouragementKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncouragementKind
        fields = '__all__'


class EncouragementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encouragement
        fields = ['id', 'encouragement_cadet', 'encouragement_kind', 'encouragement_date',
                  'encouragement_extra_data', 'get_encouragement_kind_str', 'get_encouragement_cadet_str']


class RankHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RankHistory
        fields = ['id', 'cadet', 'rank', 'rank_date',
                  'extra_data', 'get_rank_str']
