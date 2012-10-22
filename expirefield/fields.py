from django.db.models import DateTimeField

class ExpireField(DateTimeField):
    def __init__(self, verbose_name=None, name=None, **kwargs):
        super(ExpireField, self).__init__(verbose_name, name, **kwargs)
