from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Группа',
        help_text='Заполните название группы')
    slug = models.SlugField(
        unique=True, verbose_name='Идентификатор',
        help_text='Строка или число')
    description = models.TextField(
        default='', verbose_name='Описание группы',
        help_text='Заполните описание группы')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст записи',
        help_text='Введите текст')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        help_text='Укажите дату',
        db_index=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts', verbose_name='Автор записи',
        help_text='Укажите автора')

    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True, null=True, verbose_name='Группа',
        help_text='Выберите группу'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        help_text='Выберите картинку',
        upload_to='posts/',
        blank=True
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Запись',
        help_text='Выберите запись'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',

    )
    text = models.TextField(
        verbose_name='Текст нового комментария',
        help_text='Введите текст',

    )
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:15]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        related_name='follower',
        on_delete=models.CASCADE,
        verbose_name='Подписчик'
    )

    following = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE,
        verbose_name='Избранный автор',
        help_text='Выберите пользователя'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            ),
        )

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
