def get_products_by_search(queryset, query):
    """Фильтрует продукты по поисковому запросу."""

    if not query:
        return queryset

    return queryset.filter(category__name__icontains=query)
