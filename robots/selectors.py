from datetime import timedelta

from django.db.models import Count, QuerySet
from django.utils import timezone

from robots.models import Robot


def get_robots_for_last_week() -> QuerySet:
    today = timezone.now()
    since_last_week = today - timedelta(days=7)
    robots = Robot.objects.filter(
        created__gte=since_last_week
    ).values('model', 'version').annotate(
        total=Count('version'))
    return robots
