from rest_framework import serializers
from kis.models import (Cadet, Rank, PassportIssueAuthority, Speciality, Subdivision, Group,
                        Punishment, PunishmentKind, EncouragementKind, Encouragement, RankHistory)


class CadetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadet
        fields = '__all__'


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
