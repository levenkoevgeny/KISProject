from django.core.management.base import BaseCommand, CommandError
from kis.models import Cadet, Rank, PassportIssueAuthority, Speciality, Subdivision, Group, RankHistory


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            Rank.objects.all().delete()
            Rank.objects.create(rank='рядовой милиции')
            Rank.objects.create(rank='мл. сержант милиции')
            Rank.objects.create(rank='сержант милиции')
            Rank.objects.create(rank='ст. сержант милиции')
            Rank.objects.create(rank='прапорщик милиции')
            Rank.objects.create(rank='ст. прапорщик милиции')

            PassportIssueAuthority.objects.all().delete()
            PassportIssueAuthority.objects.create(passport_issue_authority='Ленинский РУВД г.Минска')
            PassportIssueAuthority.objects.create(passport_issue_authority='Партизанский РУВД г.Минска')
            PassportIssueAuthority.objects.create(passport_issue_authority='Первомайский РУВД г.Минска')
            PassportIssueAuthority.objects.create(passport_issue_authority='Советский РУВД г.Минска')
            PassportIssueAuthority.objects.create(passport_issue_authority='Заводской РУВД г.Минска')
            PassportIssueAuthority.objects.create(passport_issue_authority='Фрунзенский РУВД г.Минска')

            Speciality.objects.all().delete()
            Speciality.objects.create(speciality_name="Специальность 1")
            Speciality.objects.create(speciality_name="Специальность 2")
            Speciality.objects.create(speciality_name="Специальность 3")
            Speciality.objects.create(speciality_name="Специальность 4")
            Speciality.objects.create(speciality_name="Специальность 5")
            Speciality.objects.create(speciality_name="Специальность 6")
            Speciality.objects.create(speciality_name="Специальность 7")

            Subdivision.objects.all().delete()
            Subdivision.objects.create(subdivision_name="Подразделение 1", subdivision_short_name="П1")
            Subdivision.objects.create(subdivision_name="Подразделение 2", subdivision_short_name="П2")
            Subdivision.objects.create(subdivision_name="Подразделение 3", subdivision_short_name="П3")
            Subdivision.objects.create(subdivision_name="Подразделение 4", subdivision_short_name="П4")
            Subdivision.objects.create(subdivision_name="Подразделение 5", subdivision_short_name="П5")
            Subdivision.objects.create(subdivision_name="Подразделение 6", subdivision_short_name="П6")

            Group.objects.all().delete()
            Group.objects.create(group_name='1111')
            Group.objects.create(group_name='2222')
            Group.objects.create(group_name='3333')

            Cadet.objects.all().delete()
            Cadet.objects.create(
                last_name_rus="Иванов",
                first_name_rus="Иван",
                patronymic_rus="Иванович",
                address="г.Минск",
                group=Group.objects.get(group_name='1111'),
                speciality=Speciality.objects.get(speciality_name='Специальность 1')
            )
            Cadet.objects.create(
                last_name_rus="Петров",
                first_name_rus="Петр",
                patronymic_rus="Петрович",
                address="г.Минск",
                group=Group.objects.get(group_name='2222'),
                speciality=Speciality.objects.get(speciality_name='Специальность 2')
            )
            Cadet.objects.create(
                last_name_rus="Сидоров",
                first_name_rus="Николай",
                patronymic_rus="Петрович",
                address="г.Минск",
                group=Group.objects.get(group_name='3333'),
                speciality=Speciality.objects.get(speciality_name='Специальность 3')
            )
            Cadet.objects.create(
                last_name_rus="Долганов",
                first_name_rus="Владислав",
                patronymic_rus="Александрович",
                address="г.п.Дрыбин",
                group=Group.objects.get(group_name='1111'),
                speciality=Speciality.objects.get(speciality_name='Специальность 2')
            )

            RankHistory.objects.all().delete()
            RankHistory.objects.create(cadet=Cadet.objects.get(last_name_rus="Иванов"), rank=Rank.objects.get(rank='рядовой милиции'), rank_date='2024-09-12')
            RankHistory.objects.create(cadet=Cadet.objects.get(last_name_rus="Петров"), rank=Rank.objects.get(rank='рядовой милиции'), rank_date='2024-09-12')
            RankHistory.objects.create(cadet=Cadet.objects.get(last_name_rus="Сидоров"), rank=Rank.objects.get(rank='рядовой милиции'), rank_date='2024-09-12')
            RankHistory.objects.create(cadet=Cadet.objects.get(last_name_rus="Долганов"), rank=Rank.objects.get(rank='рядовой милиции'), rank_date='2024-09-12')

        except Exception as error:
            print(error)
            raise CommandError('init db error')

        self.stdout.write(
            self.style.SUCCESS('Init DB has done successfully')
        )