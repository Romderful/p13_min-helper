"""Fill the database with the dataset retrieved from AniAPI."""

import requests
import time

from django.core.management.base import BaseCommand
from ...models import Anime, Category


class Command(BaseCommand):
    """Custom command.

    Can start the custom command typing './manage.py fill_animes'.
    """

    def __init__(self):
        """Initializer.

        Instantiates the current API class used.
        """
        self.used_api = AniAPI()

    def handle(self, *args, **options):
        """Launch the custom command."""
        pass


class AniAPI:
    """AniAPI.

    Manage the data retrieved from AniAPI API.
    """

    def __init__(self):
        """Initialize.

        Set up the base url for the API endpoint.
        """
        self.api_url = "https://api.aniapi.com/v1/anime?nsfw=true"
        self.animes_dataset = []
        self.filtered_animes_dataset = []

        self.get_animes_data()
        self.filter_animes_data(self.animes_dataset)
        self.insert_animes_data()

    def get_animes_data(self) -> list:
        """Returns the animes data retrieved from AniAPI API."""
        running = True
        page = 1
        while running:
            response = requests.get(self.api_url, params={"page": page})
            print(f"page : {page} - getting the data...")
            if page < response.json()["data"]["last_page"]:
                for anime in response.json()["data"]["documents"]:
                    self.animes_dataset.append(anime)
                time.sleep(1)  # API restriction
            else:
                running = False
            page += 1
        return self.animes_dataset

    def filter_animes_data(self, data: list) -> list:
        """Checks that the animes data fits with the models restrictions.

        Args:
            data (list): animes_dataset.

        Returns:
            list: filtered_animes_dataset.
        """
        for anime in data:
            if (
                (anime["titles"]["en"] and len(anime["titles"]["en"]) <= 175)
                and (anime["titles"]["jp"] == None or len(anime["titles"]["jp"]) <= 175)
                and (anime["start_date"] == None or len(anime["start_date"]) <= 25)
                and (anime["end_date"] == None or len(anime["end_date"]) <= 25)
            ):
                self.filtered_animes_dataset.append(anime)
        return self.filtered_animes_dataset

    def insert_animes_data(self):
        """Inserts the filtered data into our database."""
        for anime in self.filtered_animes_dataset:
            created_anime, created = Anime.objects.update_or_create(
                english_name=anime["titles"]["en"],
                japanese_name=anime["titles"]["jp"],
                description=anime["descriptions"]["en"],
                start_date=anime["start_date"],
                end_date=anime["end_date"],
                episodes_count=anime["episodes_count"],
                cover_image=anime["cover_image"],
                score=anime["score"],
            )

            for category in anime["genres"]:
                created_category, created = Category.objects.update_or_create(
                    name=category
                )
                created_anime.categories.add(created_category)
