from django.db import models
from datetime import datetime


class Rank(models.Model):
    rank = models.CharField(verbose_name="Звание", max_length=20, unique=True)
    deadline = models.IntegerField(verbose_name="Срок в месяцах до следующего звания", blank=True, null=True)

    def __str__(self):
        return self.rank

    class Meta:
        ordering = ('id',)
        verbose_name = 'Звание'
        verbose_name_plural = 'Звания'


class PassportIssueAuthority(models.Model):
    passport_issue_authority = models.TextField(verbose_name="Орган выдачи паспорта", unique=True)

    def __str__(self):
        return self.passport_issue_authority

    class Meta:
        ordering = ('id',)
        verbose_name = 'Орган выдачи паспорта'
        verbose_name_plural = 'Органы выдачи паспорта'


class Speciality(models.Model):
    speciality_name = models.TextField(verbose_name="Специальность", unique=True)

    def __str__(self):
        return self.speciality_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Subdivision(models.Model):
    subdivision_name = models.CharField(max_length=255, verbose_name="Название подразделения")
    subdivision_short_name = models.CharField(max_length=30, verbose_name="Название подразделения (короткое)")
    parent_subdivision = models.ForeignKey("self", verbose_name="Родительское подразделение", on_delete=models.CASCADE,
                                           blank=True, null=True)

    def __str__(self):
        return self.subdivision_short_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Group(models.Model):
    group_name = models.CharField(max_length=255, verbose_name="Название подразделения")

    def __str__(self):
        return self.group_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class ComponentOrgan(models.Model):
    component_name = models.CharField(max_length=255, verbose_name="Комплектующий орган")
    component_short_name = models.CharField(max_length=50, verbose_name="Комплектующий орган (короткое название)",
                                            blank=True, null=True)

    def __str__(self):
        return self.component_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Комплектующий орган'
        verbose_name_plural = 'Комплектующие органы'


class EntranceCategory(models.Model):
    entrance_category_name = models.CharField(max_length=255, verbose_name="Категория поступающего")

    def __str__(self):
        return self.entrance_category_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Категория поступающих'
        verbose_name_plural = 'Категории поступающих'


class GO_ROVD(models.Model):
    go_rovd_name = models.CharField(max_length=255, verbose_name="ГО-РОВД")

    def __str__(self):
        return self.go_rovd_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'ГО-РОВД'
        verbose_name_plural = 'ГО-РОВД'


class SocialStatus(models.Model):
    social_status = models.CharField(max_length=255, verbose_name="Социальный статус")

    def __str__(self):
        return self.social_status

    class Meta:
        ordering = ('id',)
        verbose_name = 'Социальный статус'
        verbose_name_plural = 'Социальные статусы'


class CountryRegion(models.Model):
    country_region = models.CharField(max_length=255, verbose_name="Область (страны)")

    def __str__(self):
        return self.country_region

    class Meta:
        ordering = ('id',)
        verbose_name = 'Область'
        verbose_name_plural = 'Области'


class MilitaryOffice(models.Model):
    military_office = models.CharField(max_length=255, verbose_name="Военкомат")

    def __str__(self):
        return self.military_office

    class Meta:
        ordering = ('id',)
        verbose_name = 'Военкомат'
        verbose_name_plural = 'Военкоматы'


class Education(models.Model):
    education = models.CharField(max_length=255, verbose_name="Вид учреждения образования")

    def __str__(self):
        return self.education

    class Meta:
        ordering = ('id',)
        verbose_name = 'Вид учреждения образования'
        verbose_name_plural = 'Виды учреждения образования'


class EducationLevel(models.Model):
    education_level = models.CharField(max_length=255, verbose_name="Уровень образования")

    def __str__(self):
        return self.education_level

    class Meta:
        ordering = ('id',)
        verbose_name = 'Уровень образования'
        verbose_name_plural = 'Уровни образования'


class EducationLocalityKind(models.Model):
    education_location_kind = models.CharField(max_length=255,
                                               verbose_name="Вид населенного пункта при получения среднейго образования")

    def __str__(self):
        return self.education_location_kind

    class Meta:
        ordering = ('id',)
        verbose_name = 'Вид населенного пункта при получения среднейго образования'
        verbose_name_plural = 'Виды населенного пункта при получения среднейго образования'


class CadetCategory(models.Model):
    category = models.CharField(max_length=255, verbose_name="Категория")

    def __str__(self):
        return self.category

    class Meta:
        ordering = ('id',)
        verbose_name = 'Категория (для курсанта)'
        verbose_name_plural = 'Категории (для курсанта)'


class VPKCategory(models.Model):
    category = models.CharField(max_length=255, verbose_name="Вид ВПК")

    def __str__(self):
        return self.category

    class Meta:
        ordering = ('id',)
        verbose_name = 'Вид ВПК'
        verbose_name_plural = 'Виды ВПК'


class GraduateWithHonorsCategory(models.Model):
    category = models.CharField(max_length=255, verbose_name="Вид отличия")

    def __str__(self):
        return self.category

    class Meta:
        ordering = ('id',)
        verbose_name = 'Вид отличий при окончании УО'
        verbose_name_plural = 'Виды отличий при окончании УО'


class PPFLCategory(models.Model):
    category = models.CharField(max_length=255, verbose_name="ППФЛ категория")

    def __str__(self):
        return self.category

    class Meta:
        ordering = ('id',)
        verbose_name = 'ППФЛ категория'
        verbose_name_plural = 'ППФЛ категории'


class MaritalStatus(models.Model):
    marital_status = models.CharField(max_length=255, verbose_name="Семейное положение")

    def __str__(self):
        return self.marital_status

    class Meta:
        ordering = ('id',)
        verbose_name = 'Семейное положение'
        verbose_name_plural = 'Семейные положения'


class ForeignLanguage(models.Model):
    foreign_language = models.CharField(max_length=255, verbose_name="Иностранный язык")

    def __str__(self):
        return self.foreign_language

    class Meta:
        ordering = ('id',)
        verbose_name = 'Иностранный язык'
        verbose_name_plural = 'Иностранные языки'


class Cadet(models.Model):
    category = models.ForeignKey(CadetCategory, on_delete=models.SET_NULL, verbose_name="Категория", blank=True,
                                 null=True)
    # personal data
    last_name_rus = models.CharField(max_length=30, verbose_name="Фамилия (рус)", blank=True, null=True)
    first_name_rus = models.CharField(max_length=30, verbose_name="Имя (рус)", blank=True, null=True)
    patronymic_rus = models.CharField(max_length=30, verbose_name="Отчество (рус)", blank=True, null=True)
    last_name_bel = models.CharField(max_length=30, verbose_name="Фамилия (бел)", blank=True, null=True)
    first_name_bel = models.CharField(max_length=30, verbose_name="Имя (бел)", blank=True, null=True)
    patronymic_bel = models.CharField(max_length=30, verbose_name="Отчество (бел)", blank=True, null=True)
    last_name_en = models.CharField(max_length=30, verbose_name="Фамилия (англ)", blank=True, null=True)
    first_name_en = models.CharField(max_length=30, verbose_name="Имя (англ)", blank=True, null=True)
    patronymic_en = models.CharField(max_length=30, verbose_name="Отчество (англ)", blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    place_of_birth = models.TextField(verbose_name="Место рождения", blank=True, null=True)
    photo = models.ImageField(upload_to='media/cadets/', verbose_name="Фото", blank=True, null=True)
    address_residence = models.TextField(verbose_name="Место жительства (проживания)", blank=True, null=True)
    address_registration = models.TextField(verbose_name="Место жительства (регистрация)", blank=True, null=True)
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона", blank=True, null=True)
    personal_number_mvd = models.CharField(max_length=50, verbose_name="Личный номер", blank=True, null=True)
    marital_status = models.ForeignKey(MaritalStatus, verbose_name="Семейное положение", on_delete=models.SET_NULL,
                                       blank=True, null=True)
    # passport
    passport_number = models.CharField(max_length=100, verbose_name="Номер паспорта", blank=True, null=True)
    passport_issue_date = models.DateField(verbose_name="Дата выдачи паспорта", blank=True, null=True)
    passport_validity_period = models.DateField(verbose_name="Срок окончания действия паспорта", blank=True, null=True)
    passport_issue_authority = models.ForeignKey(PassportIssueAuthority, verbose_name="Орган выдачи паспорта",
                                                 on_delete=models.SET_NULL, blank=True, null=True)
    identification_number = models.CharField(max_length=100, verbose_name="Идентификационный номер", blank=True,
                                             null=True)
    # parents
    father_last_name = models.CharField(max_length=30, verbose_name="Отец - фамилия", blank=True, null=True)
    father_first_name = models.CharField(max_length=30, verbose_name="Отец - имя", blank=True, null=True)
    father_patronymic = models.CharField(max_length=30, verbose_name="Отец - отчество", blank=True, null=True)
    father_date_of_birth = models.DateField(verbose_name="Отец - дата рождения", blank=True, null=True)
    father_place_of_work = models.TextField(verbose_name="Отец - место работы", blank=True, null=True)
    father_phone_number = models.CharField(max_length=30, verbose_name="Отец - номер телефона", blank=True, null=True)

    mother_last_name = models.CharField(max_length=30, verbose_name="Мать - фамилия", blank=True, null=True)
    mother_first_name = models.CharField(max_length=30, verbose_name="Мать - имя", blank=True, null=True)
    mother_patronymic = models.CharField(max_length=30, verbose_name="Мать - отчество", blank=True, null=True)
    mother_date_of_birth = models.DateField(verbose_name="Мать - дата рождения", blank=True, null=True)
    mother_place_of_work = models.TextField(verbose_name="Мать - место работы", blank=True, null=True)
    mother_phone_number = models.CharField(max_length=30, verbose_name="Мать - номер телефона", blank=True, null=True)
    # education
    foreign_language_was = models.ForeignKey(ForeignLanguage, on_delete=models.SET_NULL,
                                             verbose_name="Иностранный язык (изучаемый в школе)",
                                             blank=True, null=True)
    foreign_language_will_be = models.ForeignKey(ForeignLanguage, on_delete=models.SET_NULL,
                                                 verbose_name="Иностранный язык (изучаемый в школе)",
                                                 blank=True, null=True, related_name='foreign_language_will_be')

    # academy
    subdivision = models.ForeignKey(Subdivision, verbose_name="Подразделение", on_delete=models.SET_NULL, blank=True,
                                    null=True)
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.SET_NULL, blank=True,
                                    null=True)
    academy_start_year = models.IntegerField(verbose_name="Год поступления", blank=True, null=True)
    academy_end_year = models.IntegerField(verbose_name="Год окончания", blank=True, null=True)

    # entrance campaign
    component_organ = models.ForeignKey(ComponentOrgan, on_delete=models.SET_NULL, verbose_name="Комплектующий орган",
                                        blank=True, null=True)
    entrance_category = models.ForeignKey(EntranceCategory, on_delete=models.SET_NULL,
                                          verbose_name="Категория поступающего",
                                          blank=True, null=True)
    arrived_from_go_rovd = models.ForeignKey(GO_ROVD, on_delete=models.SET_NULL,
                                             verbose_name="Прибыл из ГО-РОВД", blank=True, null=True)
    social_status = models.ForeignKey(SocialStatus, on_delete=models.SET_NULL,
                                      verbose_name="Социальный статус", blank=True, null=True)
    region_for_medical_examination = models.ForeignKey(CountryRegion, on_delete=models.SET_NULL,
                                                       verbose_name="Область (для прохождения мед. комиссии)",
                                                       blank=True, null=True)
    military_office = models.ForeignKey(MilitaryOffice, on_delete=models.SET_NULL,
                                        verbose_name="Военкомат", blank=True, null=True)
    extra_data = models.TextField(verbose_name="Дополнительные данные", blank=True, null=True)

    # questionnaire

    vpk = models.ForeignKey(VPKCategory, on_delete=models.SET_NULL, verbose_name="Военно-патриотический класс",
                            blank=True, null=True)
    vpk_data = models.TextField(verbose_name="Данные о ВПК", blank=True, null=True)
    aims_to_graduate_with_honors = models.ForeignKey(GraduateWithHonorsCategory,
                                                     verbose_name="Претендует на диплом с отличием",
                                                     on_delete=models.SET_NULL, blank=True, null=True)
    is_class_vpn = models.BooleanField(verbose_name="Класс военно-патриотической направленности", default=False)
    is_class_pn = models.BooleanField(verbose_name="Класс правовой направленности", default=False)
    is_class_other = models.BooleanField(verbose_name="Класс иной направленности", default=False)
    has_achievements_in_sports = models.BooleanField(verbose_name="Достижения в спорте", default=False)
    is_olympiad_winner = models.BooleanField(verbose_name="Победитель республиканских или регионалоных олимпиад",
                                             default=False)

    # army
    health_group = models.IntegerField(verbose_name="Группа здоровья", blank=True, null=True)
    ppfl_test = models.ForeignKey(PPFLCategory, verbose_name="ППФЛ категория", on_delete=models.SET_NULL, blank=True,
                                  null=True)
    medical_age_group = models.IntegerField(verbose_name="Медико-возрастная группа", blank=True, null=True)

    # extra
    needs_increased_attention = models.BooleanField(verbose_name="Требует повышенного внимания", default=False)
    needs_psychological_support = models.BooleanField(verbose_name="Требует психологического сопровождения",
                                                      default=False)
    is_risk_group = models.BooleanField(verbose_name="Группа риска", default=False)
    has_conviction = models.BooleanField(verbose_name="Имеет судимость", default=False)
    has_dactocard = models.BooleanField(verbose_name="Имеет дактокарту", default=False)
    has_gusb_check = models.BooleanField(verbose_name="Имеет проверку ГУСБ", default=False)
    has_employee_in_family = models.BooleanField(verbose_name="Имеет сотрудников в семье", default=False)
    is_orphan = models.BooleanField(verbose_name="Сирота", default=False)
    passed_medical_examination = models.BooleanField(verbose_name="Прошел медицинскую комиссию", default=False)
    passed_medical_examination_extra_data = models.TextField(verbose_name="Медицинская комиссия (доп. данные)",
                                                             blank=True, null=True)

    # certificate
    has_certificate_ideas_for_Belarus = models.BooleanField(verbose_name="Сертификат 100 идей для Беларуси",
                                                            default=False)
    has_certificate_kind_heart = models.BooleanField(verbose_name="Сертификат Доброе сердце", default=False)
    is_employee = models.BooleanField(verbose_name="Является сотрудником", default=False)

    # exams and certificates

    def __str__(self):
        return self.last_name_rus

    @property
    def get_full_name(self):
        patronymic_rus = self.patronymic_rus[0] if self.patronymic_rus else ""
        return f"{self.last_name_rus} {self.first_name_rus[0]}. {patronymic_rus}."

    @property
    def get_father_full_name(self):
        last_name = self.father_last_name if self.father_last_name else "Нет данных"
        first_name = self.father_first_name if self.father_first_name else ""
        patronymic = self.father_patronymic if self.father_patronymic else ""
        return f"{last_name} {first_name} {patronymic}"

    @property
    def get_mother_full_name(self):
        last_name = self.mother_last_name if self.mother_last_name else "Нет данных"
        first_name = self.mother_first_name if self.mother_first_name else ""
        patronymic = self.mother_patronymic if self.mother_patronymic else ""
        return f"{last_name} {first_name} {patronymic}"

    @property
    def get_age(self):
        today = datetime.now().date()
        return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    @property
    def get_rank(self):
        rank_last_record = RankHistory.objects.filter(cadet=self).order_by('-rank_date').first()
        return rank_last_record.rank if rank_last_record else None

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Курсант'
        verbose_name_plural = 'Курсанты'


class OrderOwner(models.Model):
    order_owner = models.CharField(max_length=255, verbose_name="Чей приказ")

    def __str__(self):
        return self.order_owner

    class Meta:
        ordering = ('id',)
        verbose_name = 'Чей приказ'
        verbose_name_plural = 'Чьи приказы'


class EducationHistory(models.Model):
    cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="Курсант")
    education_kind = models.ForeignKey(Education, on_delete=models.SET_NULL,
                                       verbose_name="Вид учреждения образования",
                                       blank=True, null=True)
    education_level = models.ForeignKey(EducationLevel, on_delete=models.SET_NULL,
                                        verbose_name="Уровень образования",
                                        blank=True, null=True)
    education_graduated = models.TextField(verbose_name="Наименование учебного заведения", blank=True, null=True)
    education_graduating_start_year = models.IntegerField(verbose_name="Год поступления", blank=True, null=True)
    education_graduating_end_year = models.IntegerField(verbose_name="Год окончания", blank=True, null=True)
    education_average_score = models.FloatField(verbose_name="Средний бал", blank=True, null=True)
    education_location_kind = models.ForeignKey(EducationLocalityKind, on_delete=models.SET_NULL,
                                                verbose_name="Вид населенного пункта",
                                                blank=True, null=True)

    def __str__(self):
        return self.cadet.get_full_name

    @property
    def get_education_kind_str(self):
        return self.education_kind.education

    @property
    def get_education_level_str(self):
        return self.education_level.education_level

    @property
    def get_education_location_kind_str(self):
        return self.education_location_kind.education_location_kind

    @property
    def get_cadet_str(self):
        return self.cadet.get_full_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'


class JobHistory(models.Model):
    cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="Курсант")
    job_position = models.TextField(verbose_name="Должность", blank=True, null=True)
    job_start_year = models.IntegerField(verbose_name="Год начала работы", blank=True, null=True)
    job_end_year = models.IntegerField(verbose_name="Год увольнения работы", blank=True, null=True)
    organisation_name = models.TextField(verbose_name="Организация, где работал", blank=True, null=True)

    def __str__(self):
        return self.cadet.get_full_name

    @property
    def get_cadet_str(self):
        return self.cadet.get_full_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class ArmyService(models.Model):
    cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="Курсант")
    military_organization = models.TextField(verbose_name="Место службы", blank=True, null=True)
    military_service_start = models.DateField(verbose_name="Служба в армии (начало)", blank=True, null=True)
    military_service_end = models.DateField(verbose_name="Служба в армии (окончание)", blank=True, null=True)
    position = models.TextField(verbose_name="Должность (без сокращений)", blank=True, null=True)
    order_owner = models.ForeignKey(OrderOwner, on_delete=models.SET_NULL, verbose_name="Чей приказ",
                                    blank=True, null=True)
    order_date = models.DateField(verbose_name="Дата приказа", blank=True,
                                  null=True)
    order_number = models.CharField(max_length=255, verbose_name="Номер приказа",
                                    blank=True, null=True)

    def __str__(self):
        return self.cadet.get_full_name

    @property
    def get_cadet_str(self):
        return self.cadet.get_full_name

    @property
    def get_order_owner_str(self):
        return self.order_owner.order_owner

    class Meta:
        ordering = ('id',)
        verbose_name = 'Служба в армии'
        verbose_name_plural = 'Службы в армии'


class MVDService(models.Model):
    cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="Курсант")
    mvd_organization = models.TextField(verbose_name="Место службы", blank=True, null=True)
    mvd_service_start = models.DateField(verbose_name="Служба в армии (начало)", blank=True, null=True)
    mvd_service_end = models.DateField(verbose_name="Служба в армии (окончание)", blank=True, null=True)
    position = models.TextField(verbose_name="Должность (без сокращений)", blank=True, null=True)
    order_owner = models.ForeignKey(OrderOwner, on_delete=models.SET_NULL, verbose_name="Чей приказ",
                                    blank=True, null=True)
    order_date = models.DateField(verbose_name="Дата приказа", blank=True,
                                  null=True)
    order_number = models.CharField(max_length=255, verbose_name="Номер приказа",
                                    blank=True, null=True)

    def __str__(self):
        return self.cadet.get_full_name

    @property
    def get_cadet_str(self):
        return self.cadet.get_full_name

    @property
    def get_order_owner_str(self):
        return self.order_owner.order_owner

    class Meta:
        ordering = ('id',)
        verbose_name = 'Служба в МВД'
        verbose_name_plural = 'Службы в МВД'


class Reward(models.Model):
    reward_title = models.TextField(verbose_name="Название награды", blank=True, null=True)

    def __str__(self):
        return self.reward_title

    class Meta:
        ordering = ('id',)
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'


class RewardHistory(models.Model):
    cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="Курсант")
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, verbose_name="Награда", blank=True, null=True)
    reward_date = models.DateField(verbose_name="Дата награды", blank=True, null=True)
    reason = models.TextField(verbose_name="За что награжден", blank=True, null=True)
    order_owner = models.ForeignKey(OrderOwner, on_delete=models.SET_NULL, verbose_name="Чей приказ",
                                    blank=True, null=True)
    order_number = models.CharField(max_length=255, verbose_name="Номер приказа",
                                    blank=True, null=True)

    def __str__(self):
        return self.cadet.get_full_name

    @property
    def get_cadet_str(self):
        return self.cadet.get_full_name

    @property
    def get_reward_str(self):
        return self.reward.reward_title

    class Meta:
        ordering = ('id',)
        verbose_name = 'Награда присвоение'
        verbose_name_plural = 'Награда присвоения'


class EncouragementKind(models.Model):
    encouragement_kind = models.CharField(max_length=255, verbose_name="Вид поощрения")

    def __str__(self):
        return self.encouragement_kind

    class Meta:
        ordering = ('id',)
        verbose_name = 'Вид поощрения'
        verbose_name_plural = 'Виды поощрений'


class Encouragement(models.Model):
    cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="На кого")
    encouragement_kind = models.ForeignKey(EncouragementKind, on_delete=models.CASCADE,
                                           verbose_name="Вид поощрения")
    encouragement_date = models.DateField(verbose_name="Дата поощрения", blank=True, null=True)
    encouragement_order_date = models.DateField(verbose_name="Дата приказа", blank=True,
                                                null=True)
    encouragement_order_number = models.CharField(max_length=255, verbose_name="Номер приказа",
                                                  blank=True, null=True)
    encouragement_order_owner = models.ForeignKey(OrderOwner, on_delete=models.SET_NULL, verbose_name="Чей приказ",
                                                  blank=True, null=True)
    encouragement_extra_data = models.TextField(verbose_name="Фабула", blank=True, null=True)

    def __str__(self):
        return str(self.cadet)

    @property
    def get_encouragement_kind_str(self):
        return self.encouragement_kind.encouragement_kind

    @property
    def get_encouragement_order_owner(self):
        return self.encouragement_order_owner.order_owner

    @property
    def get_cadet_str(self):
        return self.cadet.get_full_name

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
    cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="На кого")
    punishment_kind = models.ForeignKey(PunishmentKind, on_delete=models.CASCADE, verbose_name="Вид взыскания")
    punishment_start_date = models.DateField(verbose_name="Дата начала действия взыскания", blank=True, null=True)
    punishment_start_order_date = models.DateField(verbose_name="Дата приказа наложения взыскания", blank=True,
                                                   null=True)
    punishment_start_order_number = models.CharField(max_length=255, verbose_name="Номер приказа наложения взыскания",
                                                     blank=True, null=True)
    punishment_start_order_owner = models.ForeignKey(OrderOwner, on_delete=models.SET_NULL, verbose_name="Чей приказ",
                                                     blank=True, null=True)
    punishment_start_extra_data = models.TextField(verbose_name="Фабула о наложении", blank=True, null=True)
    punishment_expiration_date = models.DateField(verbose_name="Дата окончания действия взыскания", blank=True,
                                                  null=True)
    punishment_expiration_order_date = models.DateField(verbose_name="Дата приказа окончания взыскания", blank=True,
                                                        null=True)
    punishment_expiration_order_number = models.CharField(max_length=255,
                                                          verbose_name="Номер приказа окончания взыскания", blank=True,
                                                          null=True)
    punishment_expiration_order_owner = models.ForeignKey(OrderOwner, on_delete=models.SET_NULL,
                                                          related_name="punishment_expiration_order_owner",
                                                          verbose_name="Чей приказ",
                                                          blank=True, null=True)
    punishment_expiration_extra_data = models.TextField(verbose_name="Фабула о снятии", blank=True, null=True)

    def __str__(self):
        return str(self.cadet)

    @property
    def get_punishment_kind_str(self):
        return self.punishment_kind.punishment_kind

    @property
    def get_punishment_start_order_owner(self):
        return self.punishment_start_order_owner.order_owner

    @property
    def get_punishment_expiration_order_owner(self):
        return self.punishment_expiration_order_owner.order_owner

    @property
    def get_cadet_str(self):
        return self.cadet.get_full_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Взыскание'
        verbose_name_plural = 'Взыскания'


class RankHistory(models.Model):
    cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="Курсант")
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, verbose_name="Звание")
    rank_date = models.DateField(verbose_name="С какого числа присвоено звание", blank=True, null=True)
    rank_order_date = models.DateField(verbose_name="Дата приказа", blank=True,
                                       null=True)
    rank_order_number = models.CharField(max_length=255, verbose_name="Номер приказа",
                                         blank=True, null=True)
    rank_order_owner = models.ForeignKey(OrderOwner, on_delete=models.SET_NULL, verbose_name="Чей приказ",
                                         blank=True, null=True)
    rank_extra_data = models.TextField(verbose_name="Фабула", blank=True, null=True)

    # сделать проверку по срокам присвоения звания 45 - 50 дней

    def __str__(self):
        return str(self.cadet)

    @property
    def get_rank_str(self):
        return self.rank.rank

    @property
    def get_cadet_str(self):
        return self.cadet.get_full_name

    @property
    def get_rank_order_owner_str(self):
        return self.rank_order_owner.order_owner

    class Meta:
        ordering = ('rank_date',)
        verbose_name = 'Присвоение звания'
        verbose_name_plural = 'Присвоение званий'


class Position(models.Model):
    position = models.CharField(max_length=255, verbose_name="Должность")

    def __str__(self):
        return self.position

    class Meta:
        ordering = ('id',)
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class PositionHistory(models.Model):
    cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="Курсант")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Должность")
    position_date = models.DateField(verbose_name="Дата назначения на должность", blank=True, null=True)
    position_order_date = models.DateField(verbose_name="Дата приказа", blank=True,
                                           null=True)
    position_order_number = models.CharField(max_length=255, verbose_name="Номер приказа",
                                             blank=True, null=True)
    position_order_owner = models.ForeignKey(OrderOwner, on_delete=models.SET_NULL, verbose_name="Чей приказ",
                                             blank=True, null=True)
    position_extra_data = models.TextField(verbose_name="Дополнительная информация", blank=True, null=True)

    def __str__(self):
        return str(self.cadet)

    @property
    def get_position_str(self):
        return self.position.position

    @property
    def get_cadet_str(self):
        return self.cadet.get_full_name

    @property
    def get_position_order_owner_str(self):
        return self.position_order_owner.order_owner

    class Meta:
        ordering = ('id',)
        verbose_name = 'Назначение на должность'
        verbose_name_plural = 'Назначения на должность'


class SpecialityHistory(models.Model):
    cadet = models.ForeignKey(Cadet, on_delete=models.CASCADE, verbose_name="Курсант")
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name="Специальность")
    speciality_order_date = models.DateField(verbose_name="Дата приказа", blank=True,
                                             null=True)
    speciality_order_number = models.CharField(max_length=255, verbose_name="Номер приказа",
                                               blank=True, null=True)
    speciality_order_owner = models.ForeignKey(OrderOwner, on_delete=models.SET_NULL, verbose_name="Чей приказ",
                                               blank=True, null=True)
    speciality_extra_data = models.TextField(verbose_name="Дополнительная информация", blank=True, null=True)

    def __str__(self):
        return str(self.cadet)

    @property
    def get_cadet_str(self):
        return self.cadet.get_full_name

    @property
    def get_speciality_str(self):
        return self.speciality.speciality_name

    @property
    def get_position_order_owner_str(self):
        return self.speciality_order_owner.order_owner

    class Meta:
        ordering = ('id',)
        verbose_name = 'Перевод на специальность'
        verbose_name_plural = 'Переводы на специальности'
