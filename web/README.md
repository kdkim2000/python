# 파이썬 웹 프로그램 만들기

## backend 

### 파이썬 프레이 워크

파이썬의 프레임워크를 이해하기 위해선 먼저 '프레임워크'가 무엇인지부터 알아야 합니다. 프레임워크란 특정 프로그램을 개발하기 위해 제공되는 라이브러리와 도구의 집합을 말합니다. 특히 웹 개발 프레임워크는 웹 사이트를 생성하고 관리하기 위한 구조를 제공하는 도구입니다.

파이썬에서는 다양한 프레임워크가 있지만, 가장 널리 사용되는 것들은 Django와 Flask입니다.

Django: 이 프레임워크는 "배터리 포함"이라는 철학을 가지고 있어, 개발자가 필요로 하는 거의 모든 기능을 내장하고 있습니다. 즉, 데이터베이스 인터페이스, 관리자 패널, ORM(Object-relational mapping) 등을 제공하므로 개발 시간을 크게 단축시킬 수 있습니다. 그러나 이런 특징 때문에 때로는 Django가 너무 무겁다는 비판도 있습니다.

Flask: 이 프레임워크는 '마이크로' 프레임워크로, 최소한의 기능만을 제공합니다. 하지만, 그로 인해 개발자가 필요한 기능을 자유롭게 추가하고, 원하는 대로 애플리케이션을 구성할 수 있습니다. 또한, 복잡하지 않은 웹 사이트를 빠르게 개발하는 데 적합합니다.

이 외에도 파이썬에는 다양한 프레임워크가 있으니, 개발하고자 하는 프로젝트의 목적과 요구사항에 맞게 선택하시면 됩니다. 그리고 각 프레임워크의 공식 문서를 참고하시면 좀 더 깊이 있는 이해를 할 수 있습니다.

| 항목 | Django | Flask |
| --- | --- | --- |
| 철학 | "배터리 포함" - 필요한 모든 기능을 내장 | "마이크로" - 최소한의 기능만 제공 |
| 복잡성 | 복잡한 기능과 구조, 높은 학습 곡선 | 간단하고 직관적, 낮은 학습 곡선 |
| 확장성 | 기본적으로 많은 기능을 제공하므로 확장성이 높음 | 필요한 기능을 직접 추가해야 하므로 확장성이 낮음 |
| 적합한 프로젝트 | 크고 복잡한 웹 애플리케이션 | 작고 간단한 웹 애플리케이션 |
| 관리 도구 | 관리자 패널 제공 | 관리 도구 없음 |
| ORM 지원 | Django ORM 제공 | SQLAlchemy 등을 사용하여 별도 구성 필요 |


### Flask 사용법

Flask는 파이썬을 사용하여 웹 애플리케이션을 만들기 위한 간단하고 가벼운 웹 프레임워크입니다. Flask를 사용하면 복잡한 설정 없이도 간단한 웹 애플리케이션을 빠르게 만들 수 있습니다.

아래는 간단한 Flask 애플리케이션의 예제입니다.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

이 코드는 아주 기본적인 Flask 애플리케이션입니다.

먼저, Flask 클래스를 임포트하고, 해당 클래스의 인스턴스를 생성합니다. 이 인스턴스를 웹 애플리케이션으로 생각하면 됩니다.
그 다음으로 @app.route('/') 데코레이터를 사용하여 루트 URL('/')에 대한 동작을 정의합니다. 여기서는 'Hello, World!'라는 문자열을 반환하는 간단한 함수를 작성하였습니다. 이 함수는 루트 URL에 HTTP 요청이 오면 호출되며, 반환하는 문자열이 웹 브라우저에 표시됩니다.
마지막으로, if __name__ == '__main__': 구문은 이 스크립트가 실행되는 환경을 확인합니다. 만약 이 스크립트가 메인으로 실행되는 경우, 즉 직접 실행되는 경우에는 웹 서버를 실행하라는 의미입니다.
위 코드를 파이썬 파일(예: app.py)로 저장하고 실행하면, Flask 웹 서버가 시작되고 브라우저에서 http://localhost:5000 에 접속하면 'Hello, World!' 라는 메시지를 볼 수 있습니다.

이는 매우 기본적인 예제이며, 실제 웹 애플리케이션은 라우팅, 템플릿, 데이터베이스 등과 같은 다양한 추가 기능을 사용하게 됩니다. 이런 내용을 배우기 위해서는 Flask의 공식 문서를 참고하시는 것이 좋습니다.

### swagger

Swagger는 API의 설계, 빌드, 문서화, 소비를 도와주는 도구 세트입니다. Swagger를 사용하면 API에 대한 정보를 시각적으로 표현하고, API의 동작을 직접 시험해볼 수 있습니다.

Flask-RESTX는 Flask 확장으로, RESTful API를 구축하고 관리하는데 도움을 줍니다. Flask-RESTX는 데이터 유효성 검사, URL 라우팅, 직렬화 등을 처리해주고, Swagger UI를 통한 API 문서화도 지원합니다.

```python
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API', description='A sample API')

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        """A greeting to the world"""
        return {'message' : 'Hello, World!'}

if __name__ == "__main__":
    app.run(debug=True)
```
이 코드는 Flask-RESTX의 Api와 Resource를 사용하여 API를 정의하고 있습니다. Resource는 Flask-RESTX에서 HTTP 메서드를 처리하는 클래스이며, Api.route 데코레이터를 사용하여 URL 라우팅을 정의합니다. 또한, 각 메서드에 docstring으로 설명을 추가하면 이 정보를 바탕으로 Swagger 문서를 자동으로 생성합니다.

위 코드를 실행한 후, 웹 브라우저에서 http://localhost:5000/ 주소로 접속하면 Swagger UI를 통해 API 문서를 확인하고, API를 직접 호출해볼 수 있습니다. 이렇게 하면 API의 동작을 쉽게 테스트하고 문서를 관리할 수 있습니다.

### restAPI
REST API는 Representational State Transfer의 약자로, 웹 서버와 클라이언트 간에 정보를 주고받는 방식을 정의한 아키텍처 스타일입니다. REST API를 사용하면, HTTP 메서드(GET, POST, PUT, DELETE 등)를 이용하여 웹 서버의 리소스에 접근하고 조작할 수 있습니다.

파이썬에서는 Flask와 같은 웹 프레임워크를 사용하여 REST API를 구현할 수 있습니다.

#### restApi 메소드
아래는 REST API에서 주로 사용되는 HTTP 메서드와 그 역할에 대한 표입니다.

| HTTP 메서드 | 설명 | 예시 |
|---|---|---|
| GET | 리소스를 조회합니다. | 사용자 정보를 가져올 때 사용 |
| POST | 새로운 리소스를 생성합니다. | 새로운 사용자를 등록할 때 사용 |
| PUT | 리소스를 전체 수정합니다. 존재하지 않는 경우 새로 생성할 수도 있습니다. | 사용자의 전체 정보를 수정할 때 사용 |
| PATCH | 리소스의 일부를 수정합니다. | 사용자의 일부 정보(예: 이메일 주소)를 수정할 때 사용 |
| DELETE | 리소스를 삭제합니다. | 사용자 정보를 삭제할 때 사용 |

### Task 관리
```python
from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Task API', description='A simple Task API')

ns = api.namespace('tasks', description='Task operations')

task = api.model('Task', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details'),
})

TASKS = []

@ns.route('/')
class TaskList(Resource):
    @ns.doc('list_tasks')
    def get(self):
        """List all tasks"""
        return TASKS

    @ns.doc('create_task')
    @ns.expect(task)
    @ns.marshal_with(task, code=201)
    def post(self):
        """Create a new task"""
        new_task = api.payload
        new_task['id'] = len(TASKS) + 1
        TASKS.append(new_task)
        return new_task, 201

@ns.route('/<int:id>')
@ns.response(404, 'Task not found')
@ns.param('id', 'The task identifier')
class Task(Resource):
    @ns.doc('get_task')
    @ns.marshal_with(task)
    def get(self, id):
        """Fetch a task given its identifier"""
        for task in TASKS:
            if task['id'] == id:
                return task
        api.abort(404, "Task {} doesn't exist".format(id))

    @ns.doc('delete_task')
    @ns.response(204, 'Task deleted')
    def delete(self, id):
        """Delete a task given its identifier"""
        global TASKS
        TASKS = [task for task in TASKS if task['id'] != id]
        return '', 204

    @ns.expect(task)
    @ns.marshal_with(task)
    def put(self, id):
        """Update a task given its identifier"""
        for task in TASKS:
            if task['id'] == id:
                task.update(api.payload)
                return task
        api.abort(404, "Task {} doesn't exist".format(id))

if __name__ == "__main__":
    app.run(debug=True)
```