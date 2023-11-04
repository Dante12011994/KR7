from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitsCreateValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [HabitsCreateValidator()]
