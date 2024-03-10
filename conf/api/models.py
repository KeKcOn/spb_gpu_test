from django.db import models
from django.utils import timezone


class EventAbstractModel(models.Model):
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Organization(EventAbstractModel):
    address = models.CharField('Адрес', max_length=150)
    postcode = models.CharField('Индекс', max_length=150)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ('title',)


class Event(EventAbstractModel):
    organizations = models.ManyToManyField(
        Organization,
        through='EventOrganization',
        verbose_name='Организация',
    )
    image = models.ImageField(
        'Изображение',
        upload_to='events/images/',
        null=True,
        default=None,
        blank=True,
    )
    date = models.DateTimeField('Дата')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ('title',)


class EventOrganization(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='event_organizations',
        verbose_name='Мероприятие',
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='organization_events',
        verbose_name='Организация',
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('event', 'organization',),
                name='unique_event_organization'
            ),
        )
        verbose_name = 'Мероприятие организации'
        verbose_name_plural = 'Мероприятия организаций'
        ordering = ('event', 'organization')

    def __str__(self):
        return self.organization.title
