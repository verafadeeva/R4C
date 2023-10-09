from django.db.models.signals import post_save
from django.dispatch import receiver

from core.threads import EmailThread
from orders.selectors import get_customers
from stock.models import Stock


@receiver(post_save, sender=Stock)
def my_handler(sender, instance, created, **kwargs):
    if not created and instance.amount > 0:
        customers = get_customers(instance)
        for customer in customers:
            EmailThread(instance, customer).start()
