from datetime import time

from rest_framework.serializers import ValidationError

from habits.models import Habit


class HabitsCreateValidator:
    def __call__(self, value):

        if value.get('habit_binding') and value.get('reward'):
            raise ValidationError('Нельзя одновременно указывать связанную привычку и вознаграждение')
        if value.get('time_to_complete') > time(00, 2):
            raise ValidationError('Время выполнения должно быть не больше 120 секунд.')
        if value.get('habit_binding') is not None:
            if not Habit.objects.filter(pk=value.get('habit_binding').pk).get().sign_good_habit:
                raise ValidationError(
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки')
        if value.get('sign_good_habit') and (value.get('habit_binding') or value.get('reward')):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')
        if value.get('interval') > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
