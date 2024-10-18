from rest_framework import serializers
from kis.models import (Cadet, Rank, PassportIssueAuthority, Speciality, SpecialityHistory, Subdivision,
                        Punishment, PunishmentKind, EncouragementKind, Encouragement, RankHistory,
                        OrderOwner, Position, PositionHistory, EducationHistory, JobHistory, RewardHistory, Reward,
                        ArmyService, MVDService, CadetCategory)


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
            'category',
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
            'place_of_birth',
            'photo',
            'address_residence',
            'address_registration',
            'phone_number',
            'personal_number_mvd',
            'marital_status',
            'passport_number',
            'passport_issue_date',
            'passport_validity_period',
            'passport_issue_authority',
            'identification_number',
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
            'foreign_language_was',
            'foreign_language_will_be',
            'subdivision',
            'group',
            'academy_start_year',
            'academy_end_year',
            'component_organ',
            'entrance_category',
            'arrived_from_go_rovd',
            'social_status',
            'region_for_medical_examination',
            'military_office',
            'extra_data',
            'vpk',
            'vpk_data',
            'aims_to_graduate_with_honors',
            'is_class_vpn',
            'is_class_pn',
            'is_class_other',
            'has_achievements_in_sports',
            'is_olympiad_winner',
            'health_group',
            'ppfl_test',
            'medical_age_group',
            'needs_increased_attention',
            'needs_psychological_support',
            'is_risk_group',
            'has_conviction',
            'has_dactocard',
            'has_gusb_check',
            'has_employee_in_family',
            'is_orphan',
            'passed_medical_examination',
            'passed_medical_examination_extra_data',
            'has_certificate_ideas_for_Belarus',
            'has_certificate_kind_heart',
            'is_employee',
            'get_full_name',
            'get_age',
            'get_rank',
            'get_father_full_name',
            'get_mother_full_name'
        ]


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
                  'cadet',
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
                  'get_cadet_str',
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
                  'cadet',
                  'encouragement_kind',
                  'encouragement_date',
                  'encouragement_order_date',
                  'encouragement_order_number',
                  'encouragement_order_owner',
                  'encouragement_extra_data',
                  'get_encouragement_kind_str',
                  'get_cadet_str',
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


class EducationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationHistory
        fields = [
            "id",
            "cadet",
            "education_kind",
            "education_level",
            "education_graduated",
            "education_graduating_start_year",
            "education_graduating_end_year",
            "education_average_score",
            "education_location_kind",
            "get_education_kind_str",
            "get_education_level_str",
            "get_education_location_kind_str",
            "get_cadet_str",
        ]


class JobHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobHistory
        fields = [
            "id",
            "cadet",
            "job_position",
            "job_start_year",
            "job_end_year",
            "organisation_name",
            "get_cadet_str"
        ]


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = [
            "id",
            "reward_title"
        ]


class RewardHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardHistory
        fields = [
            "id",
            "cadet",
            "reward_date",
            "reason",
            "order_owner",
            "order_number",
            "get_cadet_str",
            "get_reward_str"
        ]


class ArmyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmyService
        fields = [
            "id",
            "cadet",
            "military_organization",
            "military_service_start",
            "military_service_end",
            "position",
            "order_owner",
            "order_date",
            "order_number",
            "get_cadet_str",
            "get_order_owner_str",
        ]


class MVDServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MVDService
        fields = [
            "id",
            "cadet",
            "mvd_organization",
            "mvd_service_start",
            "mvd_service_end",
            "position",
            "order_owner",
            "order_date",
            "order_number",
            "get_cadet_str",
            "get_order_owner_str",
        ]


class CadetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CadetCategory
        fields = [
            "id",
            "category",
        ]
