from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='lesson-create'),
    path('habit/', HabitListAPIView.as_view(), name='lesson-list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='lesson-get'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='lesson-update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='lesson-delete'),
]
