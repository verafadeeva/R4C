from robots.models import Robot


def create_robot(data: dict) -> Robot:
    serial = f"{data.get('model')}-{data.get('version')}"
    data['serial'] = serial
    robot, status = Robot.objects.get_or_create(**data)
    return robot, status
