from django.db import models


class Post(models.Model):
    '''данные о посте'''
    title = models.CharField(  max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Текст записи')
    author = models.CharField(max_length=50, verbose_name='Автор')
    date = models.DateField('Дата публикации')
    img = models.ImageField(upload_to='image/%Y', verbose_name='Изображение')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
class Comments(models.Model):
    '''комментарии'''
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    text_comments = models.TextField(verbose_name='Текст комментария', max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Запись')

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'