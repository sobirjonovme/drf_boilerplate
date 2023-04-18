from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    # max_page_size = 20

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {"next": self.get_next_link(), "previous": self.get_previous_link()},
                "total_elements": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "page": self.get_page_number(self.request, self.page.paginator),
                "page_size": self.get_page_size(self.request),
                "results": data,
            }
        )
