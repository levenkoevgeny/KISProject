from django.contrib import admin
from kis.models import (Cadet, Rank, PassportIssueAuthority, Speciality, Subdivision, Group,
                        Punishment, PunishmentKind, EncouragementKind, Encouragement, RankHistory)

admin.site.register(Cadet)
admin.site.register(Rank)
admin.site.register(PassportIssueAuthority)
admin.site.register(Speciality)
admin.site.register(Subdivision)
admin.site.register(Group)
admin.site.register(Punishment)
admin.site.register(PunishmentKind)
admin.site.register(EncouragementKind)
admin.site.register(Encouragement)
admin.site.register(RankHistory)
