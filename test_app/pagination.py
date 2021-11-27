from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 3
    # page_query_param = 'p'
    # page_size_query_param = 'size'
    max_page_size = 8

class WatchListOLPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'

class WatchListCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'created'