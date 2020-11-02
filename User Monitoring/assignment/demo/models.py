from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
# Create your models here.
import logging
import datetime
error_log=logging.getLogger('error')


class activityPeriod(models.Model):
    userid = models.CharField(max_length=100)
    real_name = models.ForeignKey(User, on_delete=models.CASCADE)
    tz = models.CharField(max_length=40,default='Asia/Kolkata')
    session_key = models.CharField(max_length=100, blank=False, null=False)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'login_logout_logs'

@receiver(user_logged_in)

def log_user_logged_in(sender, user, request, **kwargs):
    try:
        login_logout_logs = activityPeriod.objects.filter(session_key=request.session.session_key, 
        real_name=user)[:1]
        if not login_logout_logs:
            login_logout_log = activityPeriod(start_time=datetime.datetime.now(),
            session_key=request.session.session_key, 
            real_name=user,
            userid=user.id)

            login_logout_log.save()
    except Exception as e:
        # log the error
        error_log.error("log_user_logged_in request: %s, error: %s" % (request, e))


@receiver(user_logged_out)
def log_user_logged_out(sender, user, request, **kwargs):
    try:
        login_logout_logs = activityPeriod.objects.filter(session_key=request.session.session_key, 
        real_name=user)
        login_logout_logs.filter(end_time__isnull=True).update(end_time=datetime.datetime.now())
        if not login_logout_logs:
            login_logout_log = activityPeriod(end_time=datetime.datetime.now(), 
            session_key=request.session.session_key, 
            real_name=user,
            userid = user.id)
            login_logout_log.save()
    except Exception as e:
        #log the error
        error_log.error("log_user_logged_out request: %s, error: %s" % (request, e))