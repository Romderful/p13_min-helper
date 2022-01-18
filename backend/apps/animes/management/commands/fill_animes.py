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
        """Initialize.

        Instantiate the current API class used.
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
        self.entire_dataset = []
        self.filtered_dataset = []

        self.get_anime_data()
        self.filter_anime_data()
        self.insert_anime_data()

    def get_anime_data(self) -> list:
        """Returns the entire data retrieved from AniAPI API."""
        running = True
        page = 1
        while running:
            response = requests.get(self.api_url, params={"page": page})
            print(f"page : {page} - getting the data...")
            if page < response.json()["data"]["last_page"]:
                self.entire_dataset.append(response.json())
                time.sleep(62)  # API restriction
            else:
                running = False
            page += 1
        return self.entire_dataset

    def filter_anime_data(self) -> list:
        """Returns the data filtered with only anime related informations."""
        for anime in self.entire_dataset[0]["data"]["documents"]:
            self.filtered_dataset.append(anime)
        return self.filtered_dataset

    def insert_anime_data(self):
        """Insert the filtered data into our database."""
        for anime in self.filtered_dataset:
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
                created_anime.category.add(created_category)
