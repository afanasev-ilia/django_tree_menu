from django.db import models


class Menu(models.Model):
    title = models.CharField(
        'название меню',
        max_length=200,
        help_text='укажите название меню',
    )
    slug = models.SlugField(
        'текстовый идентификатор меню',
        unique=True,
        help_text='укажите текстовый идентификатор меню',
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self) -> str:
        return self.title


class ItemMenu(models.Model):
    title = models.CharField(
        'название пункта меню',
        max_length=200,
        help_text='укажите название пункта меню',
    )
    slug = models.SlugField(
        'текстовый идентификатор пункта меню',
        unique=True,
        help_text='укажите текстовый идентификатор пункта меню',
    )
    menu = models.ForeignKey(
        Menu,
        related_name='items',
        on_delete=models.CASCADE,
        help_text='выберите меню',
        )
    parent = models.ForeignKey(
        'self',
        related_name='childrens',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='выберите родительский пункт меню',
        )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return self.slug