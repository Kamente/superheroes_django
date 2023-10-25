from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Hero, Power, HeroPower


def get_powers(request):
    powers = Power.objects.all()
    data = [{'id': power.id, 'name': power.name,
             'description': power.description} for power in powers]
    return JsonResponse(data, safe=False)


def get_power_by_id(request, id):
    power = get_object_or_404(Power, pk=id)
    data = {'id': power.id, 'name': power.name,
            'description': power.description}
    return JsonResponse(data)
