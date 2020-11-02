from rest_framework import serializers
from .models import activityPeriod


class activityPeriodSerializer(serializers.Serializer):
    userid = serializers.CharField(required=True)
    real_name = serializers.CharField(required=True)
    tz = serializers.CharField(required=True)
    session_key = serializers.CharField(required=True)
    #host = seri+alizers.CharField(required=True)
    start_time = serializers.DateTimeField(required=False)
    end_time = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return activityPeriod.objects.create(**validated_data)
