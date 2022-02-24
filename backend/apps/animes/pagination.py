"""Custom pagination settings."""

from rest_framework import pagination
from rest_framework.response import Response
from django.conf import settings


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 1000
    page_size_query_param = "page_size"
    max_page_size = 10000


class MyCustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "current_page_number": self.page.number,
                "results": data,
            }
        )
