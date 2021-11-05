from common.api_response import ApiResponse
from common.utils import login_required
from flask import Blueprint, request, g


def create_task_blueprint(services):
    task_service = services.task_service

    task_bp = Blueprint("task", __name__, url_prefix="/tasks")

    @task_bp.route("", methods=["POST"])
    @login_required
    def save_task():
        return ApiResponse.ok(task_service.save_task(g.user_id, request.json))

    @task_bp.route("", methods=["GET"])
    @login_required
    def get_all_task():
        return ApiResponse.ok(task_service.get_all_task(g.user_id))

    return task_bp
