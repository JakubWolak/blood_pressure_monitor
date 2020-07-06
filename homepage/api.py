from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from measurements.models import Measurement
from your_health.models import UserData


class MyBasicAuthentication(BasicAuthentication):
    def authenticate(self, request):
        user, _ = super(MyBasicAuthentication, self).authenticate(request)
        login(request, user)

        return user, _


class ChartData(APIView):
    """
    it returns JsonResponse object to generate charts in the homepage
    """
    authentication_classes = [SessionAuthentication, MyBasicAuthentication]
    permission_classes = [IsAuthenticated]

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
            # gets 5 latest measurements
            measurements = list(Measurement.objects.filter(userdata=userdata)[:5])
            measurements.reverse()
        except Measurement.DoesNotExist as e:
            print(e)
            measurements = []
        
        measurement_date = []
        systolic_pressure = []
        diastolic_pressure = []
        pulse = []

        for measurement in measurements:
            measurement_date.append(measurement.measurement_time.strftime('%m-%d %H:%M'))
            systolic_pressure.append(measurement.systolic_pressure)
            diastolic_pressure.append(measurement.diastolic_pressure)
            pulse.append(measurement.pulse)

        data = {
            'measurement_date': measurement_date,
            'systolic_pressure': systolic_pressure,
            'diastolic_pressure': diastolic_pressure,
            'pulse': pulse
        }
        return Response(data)