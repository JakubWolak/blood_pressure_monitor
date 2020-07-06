from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .decorators import userdata_does_not_exists
from measurements.models import Measurement
from your_health.models import UserData


@login_required
@userdata_does_not_exists
def get_data_for_charts(request, *args, **kwargs):
    """
    it returns JsonResponse object to generate charts in the homepage
    """
    try:
        userdata = UserData.objects.get(user=request.user)
    except UserData.DoesNotExist as e:
        print(e)
        userdata = []

    try:
        # gets 7 latest measurements
        measurements = Measurement.objects.filter(userdata=userdata)[:7]
    except Measurement.DoesNotExist as e:
        print(e)
        measurements = []
    
    systolic_pressure = []
    diastolic_pressure = []
    pulse = []

    for measurement in measurements:
        systolic_pressure.append(measurement.systolic_pressure)
        diastolic_pressure.append(measurement.diastolic_pressure)
        pulse.append(measurement.pulse)

    data = {
        'systolic_pressure': systolic_pressure,
        'diastolic_pressure': diastolic_pressure,
        'pulse': pulse
    }
    return JsonResponse(data)