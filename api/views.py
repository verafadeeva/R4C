import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from api.serializers import serialize_robot_data
from robots.services import create_robot


@csrf_exempt
@require_http_methods(["POST"])
def robot_create(request):
    data = json.loads(request.body.decode())
    errors = serialize_robot_data(data)
    if errors:
        return HttpResponseBadRequest(
            json.dumps(errors, indent=4, ensure_ascii=False),
            headers={"Content-Type": "application/json"},
        )
    robot, created = create_robot(data)
    status = 201 if created else 200
    return HttpResponse(
        json.dumps({'id': robot.id}, indent=4),
        status=status,
    )
