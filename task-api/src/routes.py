from functools import wraps
from flask import request, jsonify


def require_auth(f):
    """Bearer Token 认证装饰器"""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth or auth != 'Bearer valid-token':
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated


def register_routes(app):
    """注册受保护的任务路由"""
    import uuid
    
    @app.route('/api/protected/tasks', methods=['GET'])
    @require_auth
    def protected_list_tasks():
        """需要认证的列表接口"""
        from src.app import tasks
        return jsonify([task.to_dict() for task in tasks])


def add_auth_headers(response):
    """添加认证相关响应头"""
    response.headers['X-Auth-Required'] = 'true'
    return response
