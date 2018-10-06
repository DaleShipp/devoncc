import datetime

from django.test import TestCase

# Create your tests here.

from django.utils import timezone

from .models import Rally


class RallyModelTests(TestCase):

    def test_start_date_after_end_date(self):
        """
        returns False if it is possible to set a rally end_date before the start date
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_rally = Rally(start_date=time, end_date=timezone.now())
        self.assertIs(future_rally, object)