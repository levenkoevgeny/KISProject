from rest_framework import serializers
from kis.models import (Cadet, Rank, PassportIssueAuthority, Speciality, SpecialityHistory, Subdivision,
                        Punishment, PunishmentKind, EncouragementKind, Encouragement, RankHistory,
                        OrderOwner, Position, PositionHistory)


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = '__all__'


class CadetSerializer(serializers.ModelSerializer):
    get_rank = RankSerializer(read_only=True)

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
            'phone_number',
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
            'education_level',
            'education_graduated',
            'education_graduating_year',
            'education_average_score',
            'education_kind',
            'education_location_kind',
            'subdivision',
            'academy_start_year',
            'academy_end_year',
            'component_organ',
            'entrance_category',
            'arrived_from_go_rovd',
            'social_status',
            'region_for_medical_examination',
            'military_office',
            'extra_data',
            'get_full_name',
            'get_age',
            'get_rank',
            'get_father_full_name',
            'get_mother_full_name'
        ]
        depth = 2


class PassportIssueAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportIssueAuthority
        fields = '__all__'


class SubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = '__all__'


class PunishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punishment
        fields = ['id',
                  'punishment_cadet',
                  'punishment_kind',
                  'punishment_start_date',
                  'punishment_start_order_date',
                  'punishment_start_order_number',
                  'punishment_start_order_owner',
                  'punishment_start_extra_data',
                  'punishment_expiration_date',
                  'punishment_expiration_order_date',
                  'punishment_expiration_order_number',
                  'punishment_expiration_order_owner',
                  'punishment_expiration_extra_data',
                  'get_punishment_kind_str',
                  'get_punishment_cadet_str',
                  'get_punishment_start_order_owner',
                  'get_punishment_expiration_order_owner'
                  ]


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
        fields = ['id',
                  'encouragement_cadet',
                  'encouragement_kind',
                  'encouragement_date',
                  'encouragement_order_date',
                  'encouragement_order_number',
                  'encouragement_order_owner',
                  'encouragement_extra_data',
                  'get_encouragement_kind_str',
                  'get_encouragement_cadet_str',
                  'get_encouragement_order_owner'
                  ]


class RankHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RankHistory
        fields = [
            'id',
            'cadet',
            'rank',
            'rank_date',
            'rank_order_date',
            'rank_order_number',
            'rank_order_owner',
            'rank_extra_data',
            'get_cadet_str',
            'get_rank_str',
            'get_rank_order_owner_str',
        ]


class OrderOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderOwner
        fields = ['id', 'order_owner']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'id',
            'position'
        ]


class PositionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionHistory
        fields = [
            'id',
            'cadet',
            'position',
            'position_date',
            'position_order_date',
            'position_order_number',
            'position_order_owner',
            'position_extra_data',
            'get_position_str',
            'get_cadet_str',
            'get_position_order_owner_str',
        ]


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'speciality_name']


class SpecialityHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialityHistory
        fields = [
            'id',
            'cadet',
            'speciality',
            'speciality_order_date',
            'speciality_order_number',
            'speciality_order_owner',
            'speciality_extra_data',
            'get_speciality_str',
            'get_cadet_str',
            'get_position_order_owner_str'
        ]
