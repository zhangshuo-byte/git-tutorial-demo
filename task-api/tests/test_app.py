import pytest
import json
from src.app import app


@pytest.fixture
def client():
    """创建测试客户端"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestIndex:
    """首页接口测试"""
    
    def test_index_returns_200(self, client):
        """GET / 应返回 200"""
        rv = client.get('/')
        assert rv.status_code == 200
    
    def test_index_returns_json(self, client):
        """GET / 应返回正确的 JSON 格式"""
        rv = client.get('/')
        data = rv.get_json()
        assert data['message'] == 'Welcome to Task API'
        assert data['version'] == '0.1.0'


class TestTaskCRUD:
    """任务 CRUD 接口测试"""
    
    def test_create_task(self, client):
        """POST /api/tasks 应能创建任务"""
        rv = client.post('/api/tasks',
                        data=json.dumps({'title': 'Test Task'}),
                        content_type='application/json')
        assert rv.status_code == 201
        data = rv.get_json()
        assert data['title'] == 'Test Task'
        assert data['id'] is not None
    
    def test_list_tasks(self, client):
        """GET /api/tasks 应能列出所有任务"""
        # 先创建一个任务
        client.post('/api/tasks',
                   data=json.dumps({'title': 'Task 1'}),
                   content_type='application/json')
        client.post('/api/tasks',
                   data=json.dumps({'title': 'Task 2'}),
                   content_type='application/json')
        rv = client.get('/api/tasks')
        assert rv.status_code == 200
        tasks = rv.get_json()
        assert len(tests := tasks) >= 2
    
    def test_get_single_task(self, client):
        """GET /api/tasks/<id> 应能获取单个任务"""
        # 创建任务
        rv = client.post('/api/tasks',
                        data=json.dumps({'title': 'Specific Task'}),
                        content_type='application/json')
        task_id = rv.get_json()['id']
        
        # 获取单个任务
        rv = client.get(f'/api/tasks/{task_id}')
        assert rv.status_code == 200
        assert rv.get_json()['title'] == 'Specific Task'
    
    def test_update_task(self, client):
        """PUT /api/tasks/<id> 应能更新任务"""
        rv = client.post('/api/tasks',
                        data=json.dumps({'title': 'Old Title'}),
                        content_type='application/json')
        task_id = rv.get_json()['id']
        
        rv = client.put(f'/api/tasks/{task_id}',
                       data=json.dumps({'title': 'New Title', 'completed': True}),
                       content_type='application/json')
        assert rv.status_code == 200
        data = rv.get_json()
        assert data['title'] == 'New Title'
        assert data['completed'] is True
    
    def test_delete_task(self, client):
        """DELETE /api/tasks/<id> 应能删除任务"""
        rv = client.post('/api/tasks',
                        data=json.dumps({'title': 'Delete Me'}),
                        content_type='application/json')
        task_id = rv.get_json()['id']
        
        rv = client.delete(f'/api/tasks/{task_id}')
        assert rv.status_code == 204
        
        rv = client.get(f'/api/tasks/{task_id}')
        assert rv.status_code == 404


class TestAuth:
    """认证相关测试"""
    
    def test_protected_without_auth(self, client):
        """未认证访问受保护接口应返回 401"""
        # 由于使用的是内存存储，需要先注册路由
        from src.routes import register_routes
        register_routes(app)
        
        rv = client.get('/api/protected/tasks')
        assert rv.status_code == 401
        assert rv.get_json()['error'] == 'Unauthorized'
    
    def test_protected_with_auth(self, client):
        """已认证访问受保护接口应成功"""
        from src.routes import register_routes
        register_routes(app)
        
        rv = client.get('/api/protected/tasks', 
                       headers={'Authorization': 'Bearer valid-token'})
        assert rv.status_code == 200
