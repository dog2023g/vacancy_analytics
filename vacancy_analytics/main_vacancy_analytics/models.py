from django.db import models


class ImageModel(models.Model):
    text = models.CharField(
        max_length=20,
        verbose_name="Text",
        db_index=True
    )
    image = models.ImageField(
        verbose_name="Image",
        upload_to="images/%Y/%m/%d/"
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Графики статистики'
        verbose_name_plural = 'Графики статистики'


# Create your models here.
class GeneralSalariesYear(models.Model):
    year = models.IntegerField(
        verbose_name="Год"
    )
    average_salary = models.IntegerField(
        verbose_name="Средняя зарплата",
        null=True
    )

    def __str__(self):
        return f"{self.year} – {self.average_salary or 'N/A'}"

    class Meta:
        verbose_name = 'Общая статистика средней зарплаты по годам'
        verbose_name_plural = 'Общая статистика средней зарплаты по годам'
        ordering = ['year']


class GeneralCountVacanciesYear(models.Model):
    year = models.IntegerField(
        verbose_name="Год"
    )
    average_salary = models.IntegerField(
        verbose_name="Количество",
        null=True
    )

    def __str__(self):
        return f"{self.year} – {self.average_salary or 'N/A'}"

    class Meta:
        verbose_name = 'Общая статистика количества вакансий по годам'
        verbose_name_plural = 'Общая статистика количества вакансий по годам'
        ordering = ['year']


class GeneralCitySalary(models.Model):
    city = models.CharField(
        max_length=100,
        verbose_name="Город"
    )
    average_salary = models.IntegerField(
        verbose_name="Средняя зарплата"
    )

    def __str__(self):
        return f"{self.city} – {self.average_salary}"

    class Meta:
        verbose_name = 'Общая статистика средней зарплаты по городам'
        verbose_name_plural = 'Общая статистика средней зарплаты по городам'
        ordering = ['city']


class GeneralCityShare(models.Model):
    city = models.CharField(
        max_length=100,
        verbose_name="Город"
    )
    share = models.FloatField(
        verbose_name="Доля"
    )

    def __str__(self):
        return f"{self.city} – {self.share}"

    class Meta:
        verbose_name = 'Общая статистика доли вакансий по городам'
        verbose_name_plural = 'Общая статистика доли вакансий по городам'
        ordering = ['city']


class GeneralSkillFrequency(models.Model):
    year = models.IntegerField(
        verbose_name="Год"
    )
    skill = models.CharField(
        max_length=100,
        verbose_name="Навык"
    )
    frequency = models.IntegerField(
        verbose_name="Частота"
    )

    def __str__(self):
        return f"{self.year} – {self.skill} – {self.frequency}"

    class Meta:
        verbose_name = 'Общая статистика топ навыков по годам'
        verbose_name_plural = 'Общая статистика топ навыков по годам'
        ordering = ['year', 'frequency']


class SalariesYear(models.Model):
    year = models.IntegerField(
        verbose_name="Год"
    )
    average_salary = models.IntegerField(
        verbose_name="Средняя зарплата",
        null=True
    )

    def __str__(self):
        return f"{self.year} – {self.average_salary or 'N/A'}"

    class Meta:
        verbose_name = 'Статистика средней зарплаты по годам для данной вакансии'
        verbose_name_plural = 'Статистика средней зарплаты по годам для данной вакансии'
        ordering = ['year']


class CountVacanciesYear(models.Model):
    year = models.IntegerField(
        verbose_name="Год"
    )
    average_salary = models.IntegerField(
        verbose_name="Количество",
        null=True
    )

    def __str__(self):
        return f"{self.year} – {self.average_salary or 'N/A'}"

    class Meta:
        verbose_name = 'Статистика количества данной вакансии по годам'
        verbose_name_plural = 'Статистика количества данной вакансии по годам'
        ordering = ['year']


class CitySalary(models.Model):
    city = models.CharField(
        max_length=100,
        verbose_name="Город"
    )
    average_salary = models.IntegerField(
        verbose_name="Средняя зарплата"
    )

    def __str__(self):
        return f"{self.city} – {self.average_salary}"

    class Meta:
        verbose_name = 'Статистика средней зарплаты по городам для данной вакансии'
        verbose_name_plural = 'Статистика средней зарплаты по городам для данной вакансии'
        ordering = ['city']


class CityShare(models.Model):
    city = models.CharField(
        max_length=100,
        verbose_name="Город"
    )
    share = models.FloatField(
        verbose_name="Доля"
    )

    def __str__(self):
        return f"{self.city} – {self.share}"

    class Meta:
        verbose_name = 'Статистика доли вакансий по городам для данной вакансии'
        verbose_name_plural = 'Статистика доли вакансий по городам для данной вакансии'
        ordering = ['city']


class SkillFrequency(models.Model):
    year = models.IntegerField(
        verbose_name="Год"
    )
    skill = models.CharField(
        max_length=100,
        verbose_name="Навык"
    )
    frequency = models.IntegerField(
        verbose_name="Частота"
    )

    def __str__(self):
        return f"{self.year} – {self.skill} – {self.frequency}"

    class Meta:
        verbose_name = 'Статистика топ навыков по годам для данной вакансии'
        verbose_name_plural = 'Статистика топ навыков по годам для данной вакансии'
        ordering = ['year', 'frequency']
