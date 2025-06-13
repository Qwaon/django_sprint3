from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(
        _('Заголовок'),
        max_length=256
    )
    description = models.TextField(
        _('Описание')
    )
    slug = models.SlugField(
        _('Идентификатор'),
        unique=True,
        help_text=_('Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.')
    )
    is_published = models.BooleanField(
        _('Опубликовано'),
        default=True,
        help_text=_('Снимите галочку, чтобы скрыть публикацию.')
    )
    created_at = models.DateTimeField(
        _('Добавлено'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('категория')
        verbose_name_plural = _('Категории')
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(
        _('Название места'),
        max_length=256
    )
    is_published = models.BooleanField(
        _('Опубликовано'),
        default=True,
        help_text=_('Снимите галочку, чтобы скрыть публикацию.')
    )
    created_at = models.DateTimeField(
        _('Добавлено'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('местоположение')
        verbose_name_plural = _('Местоположения')
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(
        _('Заголовок'),
        max_length=256
    )
    text = models.TextField(
        _('Текст')
    )
    pub_date = models.DateTimeField(
        _('Дата и время публикации'),
        help_text=_('Если установить дату и время в будущем — можно делать отложенные публикации.')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Автор публикации')
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        verbose_name=_('Местоположение'),
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name=_('Категория'),
        null=True,
        blank=True
    )
    is_published = models.BooleanField(
        _('Опубликовано'),
        default=True,
        help_text=_('Снимите галочку, чтобы скрыть публикацию.')
    )
    created_at = models.DateTimeField(
        _('Добавлено'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('публикация')
        verbose_name_plural = _('Публикации')
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
