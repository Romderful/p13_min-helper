"""Fill the database with the dataset retrieved from AniAPI."""

import requests

from django.core.management.base import BaseCommand


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
        self.api_url = "https://api.aniapi.com/v1/anime/"
        self.entire_dataset = []
        self.filtered_dataset = []

        self.get_anime_data()
        self.filter_anime_data()
        self.insert_anime_data()

    def get_anime_data(self) -> list:
        """Returns the entire data retrieved from AniAPI API."""
        running = True
        page = 144
        while running:
            response = requests.get(self.api_url, params={"page": page})
            print(f"page : {page} - getting the data...")
            if page < response.json()["data"]["last_page"]:
                self.entire_dataset.append(response.json())
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
        print(self.filtered_dataset)
