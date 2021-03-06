from django.core.management.base import BaseCommand

from game.models import Genre
from game.utils import IGDBGenreParser


class Command(BaseCommand):
    help = 'Updating games database'

    def handle(self, *args, **options):
        self.stdout.write(
            f"{self.style.NOTICE('COMMAND')}"
            f" | "
            f"{self.style.WARNING('Genres loading...')}"
        )

        parser = IGDBGenreParser()
        genres = parser.parse()

        existing_genres = Genre.objects.values_list('id', flat=True)
        created = Genre.objects.bulk_create(
            [Genre(id=i['id'], name=i['name']) for i in genres if i['id'] not in existing_genres]
        )

        self.stdout.write(
            f"{self.style.NOTICE('COMMAND')}"
            f" | "
            f"{self.style.SUCCESS(f'{len(created)} genres successfully loaded')}"
        )
