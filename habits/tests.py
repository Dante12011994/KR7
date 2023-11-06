from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from user.models import User


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.ru',
                                        first_name='Test',
                                        last_name='Test',
                                        password='12345',
                                        is_staff=True,
                                        is_superuser=True,
                                        is_active=True)
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(location="Ванная комната",
                                          time="08:00:00",
                                          move="Чистить зубы",
                                          sign_good_habit=True,
                                          interval=1,
                                          reward=None,
                                          time_to_complete="00:02:00",
                                          is_public=True,
                                          habit_binding=None)

    def test_create_habit(self):
        data = {
            "location": "Ванная комната",
            "time": "08:00:00",
            "move": "умываться",
            "sign_good_habit": False,
            "interval": 1,
            "time_to_complete": "00:02:00",
            "is_public": True,
            "habit_binding": 1
        }

        response = self.client.post(
            '/habit/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {
                "id": 2,
                "location": "Ванная комната",
                "time": "08:00:00",
                "move": "умываться",
                "sign_good_habit": False,
                "interval": 1,
                "reward": None,
                "time_to_complete": "00:02:00",
                "is_public": True,
                "owner": 1,
                "habit_binding": 1
            }
        )

    def test_list_habit(self):

        response = self.client.get('/habit/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)

        self.assertEqual(len(response.data), 4)

    def test_update_habit(self):
        data = {
            "location": "Ванная комната",
            "time": "08:00:00",
            "move": "сходить в душ",
            "sign_good_habit": True,
            "interval": 1,
            "time_to_complete": "00:02:00",
            "is_public": True
        }

        response = self.client.patch(
            f'/habit/update/{self.habit.id}/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.habit.refresh_from_db()
        self.assertEquals(
            self.habit.move,
            data['move']
        )

    def test_delete_lesson(self):

        response = self.client.delete(
            f'/habit/delete/{self.habit.id}/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())
