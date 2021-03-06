import factory
import pytz
from django.contrib.gis.geos import Point

from parkings.models import Parking

from .faker import fake
from .operator import OperatorFactory

CAPITAL_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ'


def generate_registration_number():
    letters = ''.join(fake.random.choice(CAPITAL_LETTERS) for _ in range(3))
    numbers = ''.join(fake.random.choice('0123456789') for _ in range(3))
    return '%s-%s' % (letters, numbers)


class ParkingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Parking

    location = factory.LazyFunction(lambda: Point(24.9392813 + fake.random.uniform(0.001, 0.01),
                                                  60.1631665 + fake.random.uniform(0.001, 0.01)))
    operator = factory.SubFactory(OperatorFactory)
    registration_number = factory.LazyFunction(generate_registration_number)
    time_start = factory.LazyFunction(lambda: fake.date_time_between(start_date='-2h', end_date='-1h', tzinfo=pytz.utc))
    time_end = factory.LazyFunction(lambda: fake.date_time_between(start_date='+1h', end_date='+2h', tzinfo=pytz.utc))
    zone = factory.LazyFunction(lambda: fake.random.randint(1, 3))
