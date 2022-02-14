from ..models import Measurement
from ..models import Variable

def get_measurements():
    medir = Measurement.objects.all()
    return medir

def get_measurement(mer_pk):
    medir = Measurement.objects.get(pk=mer_pk)
    return medir

def update_measurement(mer_pk, new_mer):
    medir = get_measurement(mer_pk)
    medir.value = new_mer["value"]
    medir.save()
    return medir

def create_measurement(mer):
    variable = Variable(name=mer["variable"])
    variable.save()
    medir = Measurement(variable=variable,value=mer["value"], unit=mer["unit"], place=mer["place"])
    medir.save()
    return medir

def delete_measurement(mer_pk):
    medir = Measurement.objects.get(pk=mer_pk)
    medir.delete()
    return  medir