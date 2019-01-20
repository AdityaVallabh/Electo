from django.core.management.base import BaseCommand
from Portal.models import Voter

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not Voter.objects.filter(username='admin').exists():
            Voter.objects.create_superuser('admin', '', 'admin123')
