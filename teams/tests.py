from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime

from .models import Team

class TeamTests(TestCase):
    @classmethod
    def setUpTestData(cls):

        testuser1 = get_user_model().objects.create_user(
            username="some user", 
            password="somepassword123")
        testuser1.save()


        test_team = Team.objects.create(
            author=testuser1, 
            name="some team", 
            manager = "some manager",
            short_name = "sn",
            year_founded = datetime.strptime("11/22/21", '%m/%d/%y'),
            country="some country",
        )
        test_team.save()

    def test_team_content(self):
        team = Team.objects.get(id=1)
        expected_author = f"{team.author}"
        expected_name = f"{team.name}"
        expected_short_name = f"{team.short_name}"
        expected_manager = f"{team.manager}"
        expected_year_founded = datetime.strptime("11/22/21", '%m/%d/%y')
        expected_country = f"{team.country}"
        self.assertEqual(expected_author, "some user")
        self.assertEqual(expected_name, "some team")
        self.assertEqual(expected_short_name, "sn")
        self.assertEqual(expected_manager, "some manager") 
        self.assertEqual(expected_year_founded, datetime(2021, 11, 22, 0, 0)) 
        self.assertEqual(expected_country, "some country") 

