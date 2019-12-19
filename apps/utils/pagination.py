from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from collections import OrderedDict


class Pagination(PageNumberPagination):
    """用于内容分页的类"""
    page_size = 10
    page_size_query_param = 'ps'
    page_query_param = 'p'
    max_page_size = 300
    page_number = 0

    def paginate_queryset(self, queryset, request, view=None):
        self.page_number = request.query_params.get(self.page_query_param, '1')
        return super().paginate_queryset(queryset, request, view=None)

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page', int(self.page_number)),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
