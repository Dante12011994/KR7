from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    INTERVAL = [('day', 'каждый день'), ('week', 'раз в неделю'), ('month', 'раз в месяц')]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')
    location = models.CharField(max_length=250, verbose_name='Место')
    time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Время, когда')
    move = models.TextField(verbose_name='Действие')
    sign_good_habit = models.BooleanField(default=True, verbose_name='Признак приятной привычки')
    habit_binding = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Связанная привычка')
    interval = models.CharField(max_length=5, choices=INTERVAL, default='day', verbose_name='Периодичность')
    reward = models.CharField(max_length=100, **NULLABLE, verbose_name='Вознаграждение')
    time_to_complete = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=True, verbose_name='Признак публичности')

    class Meta:
        verbose_name = 'Приятная привычка'
        verbose_name_plural = 'Приятные привычки'

    def __str__(self):
        return f'Я буду {self.move} в {self.location} в {self.time}'
