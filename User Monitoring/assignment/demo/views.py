from rest_framework.views import APIView
from rest_framework.response import Response
from .models import activityPeriod
from django.http import HttpResponse, JsonResponse
from .serializers import activityPeriodSerializer
import pandas as pd
import json
from django.contrib.auth.models import User
# Create your views here.z

class periodModel(APIView):
    def get(self, request):
        activity = activityPeriod.objects.all()
        serializer = activityPeriodSerializer(activity, many=True)
        data = serializer.data
        df = pd.DataFrame(data)
        df = df.rename(columns={"userid": "id"})
        print(df)
        df = df.drop(columns=['session_key'],axis=0)
        j = (df.groupby(['id','real_name','tz'], as_index=True)
             .apply(lambda x: x[['start_time','end_time']].to_dict('r'))
             .reset_index()
             .rename(columns={0:'activity_periods'})
             .to_json(orient='records'))
        j=json.loads(j)
        result_output = {}
        result_output['ok'] = 'true'
        result_output['members'] = j
        print(result_output)
        return Response(result_output)