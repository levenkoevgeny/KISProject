from django.db import models


class Rank(models.Model):
    rank = models.CharField(verbose_name="Rank", max_length=20, unique=True)

    def __str__(self):
        return self.rank

    class Meta:
        ordering = ('id',)
        verbose_name = 'Звание'
        verbose_name_plural = 'Звания'


class PassportIssueAuthority(models.Model):
    passport_issue_authority = models.TextField(verbose_name="Passport issue authority", unique=True)

    def __str__(self):
        return self.passport_issue_authority

    class Meta:
        ordering = ('id',)
        verbose_name = 'Орган выдачи паспорта'
        verbose_name_plural = 'Органы выдачи паспорта'


class Speciality(models.Model):
    speciality_name = models.TextField(verbose_name="Speciality", unique=True)

    def __str__(self):
        return self.speciality_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Subdivision(models.Model):
    subdivision_name = models.CharField(max_length=255, verbose_name="Subdivision name")
    subdivision_short_name = models.CharField(max_length=30, verbose_name="Subdivision short name")
    parent_subdivision = models.ForeignKey("self", verbose_name="Parent subdivision", on_delete=models.CASCADE,
                                           blank=True, null=True)

    def __str__(self):
        return self.subdivision_short_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Group(models.Model):
    group_name = models.CharField(max_length=255, verbose_name="Group name", unique=True)

    def __str__(self):
        return self.group_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Cadet(models.Model):
    # personal data
    last_name_rus = models.CharField(max_length=30, verbose_name="Last name rus")
    first_name_rus = models.CharField(max_length=30, verbose_name="First name rus")
    patronymic_rus = models.CharField(max_length=30, verbose_name="Patronymic rus", blank=True, null=True)
    last_name_bel = models.CharField(max_length=30, verbose_name="Last name bel", blank=True, null=True)
    first_name_bel = models.CharField(max_length=30, verbose_name="First name bel", blank=True, null=True)
    patronymic_bel = models.CharField(max_length=30, verbose_name="Patronymic bel", blank=True, null=True)
    last_name_en = models.CharField(max_length=30, verbose_name="Last name en", blank=True, null=True)
    first_name_en = models.CharField(max_length=30, verbose_name="First name en", blank=True, null=True)
    patronymic_en = models.CharField(max_length=30, verbose_name="Patronymic en", blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Date of birth", blank=True, null=True)
    photo = models.ImageField(upload_to='media/cadets/', verbose_name="Photo", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Address", blank=True, null=True)
    # passport
    passport_number = models.CharField(max_length=100, verbose_name="Passport number", blank=True, null=True)
    passport_issue_date = models.DateField(verbose_name="Passport issue date", blank=True, null=True)
    passport_validity_period = models.DateField(verbose_name="Passport validity period", blank=True, null=True)
    passport_issue_authority = models.ForeignKey(PassportIssueAuthority, verbose_name="Passport issue authority",
                                                 on_delete=models.SET_NULL, blank=True, null=True)
    # parents
    father_last_name = models.CharField(max_length=30, verbose_name="Father last name", blank=True, null=True)
    father_first_name = models.CharField(max_length=30, verbose_name="Father first name", blank=True, null=True)
    father_patronymic = models.CharField(max_length=30, verbose_name="Father patronymic", blank=True, null=True)
    father_date_of_birth = models.DateField(verbose_name="Date of birth", blank=True, null=True)
    father_place_of_work = models.TextField(verbose_name="Father place of work", blank=True, null=True)
    father_phone_number = models.CharField(max_length=30, verbose_name="Father phone number", blank=True, null=True)

    mother_last_name = models.CharField(max_length=30, verbose_name="Father last name", blank=True, null=True)
    mother_first_name = models.CharField(max_length=30, verbose_name="Father first name", blank=True, null=True)
    mother_patronymic = models.CharField(max_length=30, verbose_name="Father patronymic", blank=True, null=True)
    mother_date_of_birth = models.DateField(verbose_name="Date of birth", blank=True, null=True)
    mother_place_of_work = models.TextField(verbose_name="Father place of work", blank=True, null=True)
    mother_phone_number = models.CharField(max_length=30, verbose_name="Father phone number", blank=True, null=True)
    # education
    school_graduated = models.TextField(verbose_name="School graduated", blank=True, null=True)
    school_graduating_date = models.DateField(verbose_name="School graduating date", blank=True, null=True)
    school_average_score = models.FloatField(verbose_name="School average score", blank=True, null=True)
    # academy
    speciality = models.ForeignKey(Speciality, on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    academy_start_year = models.IntegerField(verbose_name="Academy start year", blank=True, null=True)
    academy_end_year = models.IntegerField(verbose_name="Academy graduating year", blank=True, null=True)

    # encouragement

    def __str__(self):
        return self.last_name_rus

    class Meta:
        ordering = ('id',)
        verbose_name = 'Курсант'
        verbose_name_plural = 'Курсанты'


class EncouragementKind(models.Model):
    encouragement_kind = models.CharField(max_length=255, verbose_name="Encouragement kind")

    def __str__(self):
        return self.encouragement_kind

    class Meta:
        ordering = ('id',)
        verbose_name = 'Вид поощрения'
        verbose_name_plural = 'Виды поощрений'


class Encouragement(models.Model):
    encouragement_cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="Encouragement cadet")
    encouragement_kind = models.ForeignKey(EncouragementKind, on_delete=models.CASCADE,
                                           verbose_name="Encouragement kind")
    encouragement_date = models.DateField(verbose_name="Encouragement date", blank=True, null=True)
    encouragement_extra_data = models.TextField(verbose_name="Encouragement extra data", blank=True, null=True)

    def __str__(self):
        return str(self.encouragement_cadet)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Поощрение'
        verbose_name_plural = 'Поощрения'


class PunishmentKind(models.Model):
    punishment_kind = models.CharField(max_length=255, verbose_name="Punishment kind")

    def __str__(self):
        return self.punishment_kind

    class Meta:
        ordering = ('id',)
        verbose_name = 'Вид взыскания'
        verbose_name_plural = 'Виды взысканий'


class Punishment(models.Model):
    punishment_cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="Punishment cadet")
    punishment_kind = models.ForeignKey(EncouragementKind, on_delete=models.CASCADE, verbose_name="Punishment kind")
    punishment_start_date = models.DateField(verbose_name="Punishment start date", blank=True, null=True)
    punishment_expiration_date = models.DateField(verbose_name="Punishment expiration date", blank=True, null=True)
    punishment_extra_data = models.TextField(verbose_name="Punishment extra data", blank=True, null=True)

    def __str__(self):
        return str(self.punishment_cadet)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Поощрение'
        verbose_name_plural = 'Поощрения'


class RankHistory(models.Model):
    cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="Cadet")
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, verbose_name="Rank")
    rank_date = models.DateField(verbose_name="Rank date", blank=True, null=True)
    extra_data = models.TextField(verbose_name="Extra data", blank=True, null=True)

    def __str__(self):
        return str(self.cadet)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Присвоение звания'
        verbose_name_plural = 'Присвоение званий'
