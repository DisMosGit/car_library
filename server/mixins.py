from urllib.parse import unquote
from datetime import datetime


class ViewRouterMixin():
    router_prefix: str = r''
    router_basename: str = ''

    @classmethod
    def router_path(cls):
        return {
            'prefix': cls.router_prefix,
            'viewset': cls,
            'basename': cls.router_basename
        }


class FilterMixin():
    search_fields: list = []

    def get_filter_params(self):
        kwargs: dict = {}
        for field in self.search_fields:
            param = self.request.query_params.get(field, None)
            if param:
                param = unquote(param)
                if field in ['datetime__gte', 'datetime__lte']:
                    param = datetime.strptime(param, '%Y-%m-%d')
                kwargs.update({field: param})
        return kwargs

    def get_queryset(self):
        filters = self.get_filter_params()
        if filters:
            queryset = self.model.objects.filter(**filters)
        else:
            queryset = self.model.objects.all()
        return queryset