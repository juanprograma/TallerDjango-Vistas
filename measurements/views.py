
from .logic import measurements_logic as mr
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measure_dto = mr.get_measurement(id)
            measure = serializers.serialize('json', [measure_dto,])
            return HttpResponse(measure, 'application/json')
        else:
            measure_dto = mr.get_measurements()
            measure = serializers.serialize('json', measure_dto)
            return HttpResponse(measure, 'application/json')

    if request.method == 'POST':
        measure_dto = mr.create_measurement(json.loads(request.body))
        measure = serializers.serialize('json', [measure_dto,])
        return HttpResponse(measure, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measure_dto = mr.get_measurement(pk)
        measure = serializers.serialize('json', [measure_dto,])
        return HttpResponse(measure , 'application/json')

    if request.method == 'PUT':
        measure_dto = mr.update_measurement(pk, json.loads(request.body))
        measure = serializers.serialize('json', [measure_dto,])
        return HttpResponse(measure, 'application/json')
    
    if request.method == 'DELETE':
        measure_dto = mr.delete_measurement(pk)
        measure = serializers.serialize('json', [measure_dto,])
        return HttpResponse(measure, 'application/json')
