from django.core.management.base import BaseCommand, \
    CommandError, NoArgsCommand
from expirefield.fields import ExpireField
from django.db import models
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Crawl through database and remove rows from tables with ExpireFields'

    def handle(self, *args, **options):
        if len(args) < 1:
            self.stderr.write('Please specify number of hours\n')
            return 0
        # get all models that have an ExpireField
        ms = [m for m in models.get_models() 
             if any( type(f) is ExpireField for f in m._meta.fields)]
        # asume parameter is in hours
        hours = int(args[0])
        oldest_time = (datetime.now()-timedelta(hours=hours))
        for m in ms:
            self.stdout.write('expiring ' + m._meta.verbose_name + '\n')
            # get first expirefield, so if multiple are defined, only
            # the first is used
            name = next(f.name for f in m._meta.fields 
                        if type(f) is ExpireField )

            filter_args = {'{0}__{1}'.format(name, 'lt'): oldest_time,}
            # delete all the old objects
            q = m.objects.filter(**filter_args)
            q.delete()
