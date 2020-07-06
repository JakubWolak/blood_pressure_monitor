from rest_framework.views import APIView
from rest_framework.response import Response

from measurements.models import Measurement
from your_health.models import UserData


class ChartData(APIView):
    """
    it returns JsonResponse object to generate charts in the homepage
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Return a list of all users.
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
        return Response(data)