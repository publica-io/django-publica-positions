import random
import string
import factory

from models import Position

class PositionFactory(factory.Factory):
    class Meta:
        model = Position

    title = factory.Sequence(lambda n: 'Position Title %d' % n)
    short_title = factory.Sequence(lambda n: 'Position Short Title %d' % n)
    enabled = random.random < 0.3
