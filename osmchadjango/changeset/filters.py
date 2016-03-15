import django_filters
from models import Changeset
from django_filters import filters


class ChangesetFilter(django_filters.FilterSet):

    max_score = filters.MethodFilter()
    max_user_score = filters.MethodFilter()

    def filter_max_score(self, queryset, value):
        if value:
            return queryset.filter(score__lte=value).exclude(score__isnull=True)
        return queryset

    def filter_max_user_score(self, queryset, value):
        if value:
            return queryset.filter(user_detail__score__lte=value).exclude(user_detail__score__isnull=True)
        return queryset

    class Meta:
        model = Changeset
        fields = {
            # 'reasons': ['exact'],
            'create': ['gte', 'lte'],
            'modify': ['gte', 'lte'],
            'delete': ['gte', 'lte'],
            'date': ['gte', 'lte'],
            'max_score': [],
            'max_user_score': [],
            'user_detail__score': ['lte'],
            'user_detail__changesets_no': ['lte'],
            'user_detail__changesets_changes': ['lte'],
            'editor': ['icontains'],
            'comment': ['icontains'],
            'source': ['icontains'],
            'user': ['exact'],
            'is_suspect': ['exact']
        }

