from annoying.decorators import render_to
from .models import Coin


@render_to()
def coins(request, template):
    coins = Coin.objects.all()
    return {'coins': coins, 'TEMPLATE': template}
