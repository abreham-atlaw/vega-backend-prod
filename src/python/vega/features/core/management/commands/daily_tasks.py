from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management.base import BaseCommand

from features.authentication.models import VegaUser
from dependency_injection.utils_providers import UtilsProviders


class Command(BaseCommand):
    help = "Runs Daily Tasks"

    @staticmethod
    def __generate_playlists():
        print("Generating Daily Playlists")
        generator = UtilsProviders.provide_generator()
        for user in VegaUser.objects.all():
            generator.generate_playlist(user)

    def handle(self, *args, **options):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.__generate_playlists, 'interval', days=1)
        scheduler.start()
