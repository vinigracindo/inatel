from django.db import models
from django.contrib.auth import get_user_model


class Log(models.Model):
    # The url the user requested
    endpoint = models.CharField(max_length=100, null=True)
    # User that made request, if authenticated
    user_id = models.CharField(max_length=100, null=True)
    response_code = models.PositiveSmallIntegerField()
    method = models.CharField(max_length=10, null=True)
    # IP address of user
    remote_address = models.CharField(max_length=20, null=True)
    # Time taken to create the response
    exec_time = models.IntegerField(null=True)
    # Date and time of request
    date = models.DateTimeField(auto_now=True)
    body_response = models.TextField()
    body_request = models.TextField()

    def get_user_object(self):
        try:
            return get_user_model().objects.get(pk=self.user_id)
        except get_user_model().DoesNotExist:
            return 'Usuário anônimo'
