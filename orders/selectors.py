from orders.models import Order
from stock.models import Stock


def get_customers(obj: Stock) -> list:
    robot_ser = obj.robot_serial
    customers = Order.objects.filter(
        robot_serial=robot_ser,
        is_done=False,
    ).select_related('customer').values_list('customer__email', flat=True)
    return list(customers)
