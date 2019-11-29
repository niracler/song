from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    """用于内容分页的类"""
    page_size = 10
    page_size_query_param = 'ps'
    page_query_param = 'p'
    max_page_size = 300