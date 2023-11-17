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

## frontend

### 프레임 워크 

> frontend 에서 가장 많이 사용하는 프레임워그 3개를 장점과 단점을 포함하여 표로 정리해 줘.

| 프레임워크 | 장점 | 단점 |
| --- | --- | --- |
| **React** | 1. 가상 DOM을 사용하여 화면을 빠르게 업데이트합니다.<br>2. 컴포넌트 기반의 구조로 재사용성이 높습니다.<br>3. 큰 커뮤니티와 많은 라이브러리를 가지고 있습니다. | 1. 학습 곡선이 가파르다.<br>2. 종합적인 가이드라인이 부족하다.<br>3. 설정과 툴링이 복잡하다. |
| **Angular** | 1. TypeScript를 기반으로 하여 타입 체크가 가능합니다.<br>2. MVC 패턴을 적용한 구조로 대규모 애플리케이션에 적합합니다.<br>3. 구글의 지원을 받고 있어 안정적입니다. | 1. 높은 학습 곡선을 가지고 있다.<br>2. 무거운 프레임워크로 인식될 수 있다.<br>3. 초기 로딩 속도가 느릴 수 있다. |
| **Vue.js** | 1. 가볍고 빠르며, 초기 설정이 간단합니다.<br>2. React와 Angular의 장점을 적절히 섞어 만든 프레임워크입니다.<br>3. HTML, CSS, JavaScript 기반으로 쉽게 접근 가능합니다. | 1. 커뮤니티와 라이브러리가 React나 Angular보다 작다.<br>2. 대규모 애플리케이션에 대한 검증이 상대적으로 적다.<br>3. 한국에서는 아직 사용 사례가 많지 않다. |

### Vue.js
>Vue.js 에 대해 다시 쉽게 설명해 줘. 예는 html 확장자에 CDN을 사용할 수 있는 예제로 작성해 줘.
>>Vue.js는 웹 페이지를 만들기 위한 자바스크립트 프레임워크입니다. 웹 페이지를 여러 개의 재사용 가능한 컴포넌트로 나누어 개발할 수 있어, 관리가 편리하고 가독성이 좋습니다.
<br>Vue.js는 직관적이며 쉬운 문법을 가지고 있어, 초보자도 쉽게 사용할 수 있습니다. 
<br>또한, CDN(Content Delivery Network)을 통해 쉽게 사용할 수 있습니다.
<br>아래는 HTML 파일에서 Vue.js를 CDN을 통해 사용하는 간단한 예제입니다.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Vue.js 초보자를 위한 예제</title>
    <!-- Vue.js를 CDN을 통해 가져옵니다. -->
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
</head>
<body>
    <div id="app">
        <!-- Vue.js의 데이터 바인딩을 사용하여, message 변수를 출력합니다. -->
        {{ message }}
    </div>

    <script>
        // Vue 인스턴스를 생성합니다.
        new Vue({
            // '#app' 요소에 Vue를 적용합니다.
            el: '#app',
            // message 데이터를 정의합니다.
            data: {
                message: '안녕하세요, Vue!'
            }
        });
    </script>
</body>
</html>
```
>>위 코드를 실행하면, 웹 페이지에 '안녕하세요, Vue!'라는 문구가 출력됩니다. 여기서 {{ message }}는 Vue.js의 데이터 바인딩 문법으로, message 데이터의 값을 HTML에 출력합니다. 이처럼 Vue.js를 사용하면, 웹 페이지의 동적인 부분을 쉽게 제어할 수 있습니다.

### CDN
>CDN 에 대해 초보자가 이해할 수 있도록 쉽게 설명해 줘.
>>CDN이란 Content Delivery Network의 약자로, 한국어로는 '콘텐츠 전송 네트워크'라고 번역할 수 있습니다.
<br>웹사이트를 운영하다 보면, 동일한 데이터를 여러 사용자에게 반복적으로 전송해야 하는 경우가 많습니다. 이 때 모든 데이터를 원본 서버에서 직접 전송하려고 하면 서버에 많은 부하가 발생하고, 사용자는 데이터를 받아오는 데 오래 걸릴 수 있습니다.
<br>이런 문제를 해결하기 위해 CDN이라는 기술이 사용됩니다. CDN은 전 세계 여러 곳에 데이터를 복사해 두고, 사용자가 데이터를 요청하면 가장 가까운 곳에서 데이터를 받아올 수 있도록 도와줍니다.
<br>예를 들어, 서울에서 운영하는 웹사이트의 사용자가 미국에 있다면, 원본 서버에서 데이터를 직접 받아오는 것보다 미국 내에 있는 CDN 서버에서 데이터를 받아오는 것이 훨씬 빠를 것입니다.
<br>또한, CDN은 웹사이트의 정적 콘텐츠(이미지, CSS, JavaScript 파일 등)를 캐싱하여 전송합니다. 이런 콘텐츠들은 변경되지 않는 경우가 많으므로, CDN을 통해 미리 전송해 두면 원본 서버의 부하를 줄이고, 사용자는 웹사이트를 더 빠르게 볼 수 있습니다.

>>따라서, CDN은 웹사이트의 속도를 향상시키고, 서버 부하를 줄이는 데 큰 도움을 줍니다. 

### Vue.js 라이브러리
>Vue.js 의 주요 라이브러리 중 가장 많이 활용하는 3가지를 표로

| 라이브러리 | 설명 | 사용 용도 |
| --- | --- | --- |
| **Vue Router** | Vue.js 공식 라우터 라이브러리입니다. | 싱글 페이지 애플리케이션(SPA)에서 페이지 간의 이동을 관리합니다. |
| **Vuex** | Vue.js의 상태 관리 패턴 + 라이브러리입니다. | 복잡한 앱의 컴포넌트들을 위한 중앙 집중식 저장소 역할을 합니다. |
| **Vuetify** | Vue.js를 위한 Material Design UI 라이브러리입니다. | 컴포넌트의 디자인과 레이아웃을 쉽게 구현할 수 있습니다. |

### bootstrap
>bootstrap 에 대해 쉽게 설명해 주고 Vue.js 에서 활용할 수 있는 방법을 알려 줘. 예제를 제공해 주는 데 CDN 환경에서 실행 가능하도록 해줘. 예제 에는 Button, Alert 등 화면에서 간단히 확인 가능 한 것들을 포함해 줘.
>>Bootstrap은 웹사이트를 디자인하는 데 사용되는 가장 인기있는 프레임워크 중 하나입니다. HTML, CSS, 그리고 JavaScript로 구성되어 있으며, 반응형 웹사이트를 쉽게 만들 수 있도록 도와줍니다.
<br>
Vue.js에서 Bootstrap을 사용하기 위해서는 Bootstrap Vue를 사용하거나 직접 CDN을 통해 Bootstrap을 불러와 사용할 수 있습니다.
<br>
Bootstrap Vue를 사용하면 Vue.js 컴포넌트 형태로 Bootstrap 기능을 쉽게 사용할 수 있지만, 별도의 설치 및 설정이 필요합니다. 따라서 여기서는 직접 CDN을 통해 Bootstrap을 불러와 사용하는 방법을 소개하겠습니다.
<br>
아래 예제에서는 Bootstrap의 버튼, 알림, 드롭다운 컴포넌트를 사용합니다. Calendar 컴포넌트는 Bootstrap 자체에서 제공하지 않으므로, 이를 대체할 수 있는 Datepicker 컴포넌트를 사용하겠습니다. 이 컴포넌트는 jQuery와 Bootstrap의 JavaScript가 필요하므로, 이 둘도 함께 불러옵니다.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Vue.js와 Bootstrap 예제</title>
    <!-- Vue.js를 CDN을 통해 가져옵니다. -->
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
    <!-- jQuery를 CDN을 통해 가져옵니다. -->
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <!-- Bootstrap CSS를 CDN을 통해 가져옵니다. -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <!-- Bootstrap JavaScript를 CDN을 통해 가져옵니다. -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
    <!-- Bootstrap Datepicker CSS를 CDN을 통해 가져옵니다. -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.9.0/css/bootstrap-datepicker.min.css">
    <!-- Bootstrap Datepicker JavaScript를 CDN을 통해 가져옵니다. -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.9.0/js/bootstrap-datepicker.min.js"></script>
</head>
<body>
    <div id="app" class="container">
        <!-- Bootstrap의 버튼 컴포넌트를 사용합니다. -->
        <button type="button" class="btn btn-primary" @click="alertVisible = !alertVisible">
            알림 토글
        </button>

        <!-- Bootstrap의 알림 컴포넌트를 사용합니다. -->
        <div class="alert alert-warning" role="alert" v-show="alertVisible">
            {{ message }}
        </div>

        <!-- Bootstrap의 드롭다운 컴포넌트를 사용합니다. -->
        <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                드롭다운 버튼
            </button>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a class="dropdown-item" href="#">액션</a>
                <a class="dropdown-item" href="#">다른 액션</a>
                <a class="dropdown-item" href="#">또 다른 액션</a>
            </div>
        </div>

        <!-- Bootstrap Datepicker 컴포넌트를 사용합니다. -->
        <input type="text" class="form-control datepicker">
    </div>

    <script>
        // Vue 인스턴스를 생성합니다.
        new Vue({
            // '#app' 요소에 Vue를 적용합니다.
            el: '#app',
            // message와 alertVisible 데이터를 정의합니다.
            data: {
                message: '안녕하세요, Vue와 Bootstrap!',
                alertVisible: true
            },
            // Vue 인스턴스가 생성된 후, Datepicker를 적용합니다.
            mounted: function () {
                $('.datepicker').datepicker();
            }
        });
    </script>
</body>
</html>


```
>>이 예제에서는 Vue.js의 데이터 바인딩과 이벤트 바인딩을 활용하여, 버튼 클릭에 따라 알림의 표시 여부를 변경하고 있습니다. 또한, Bootstrap Datepicker를 활용하여 달력 선택 기능을 구현하였습니다. 이처럼 Vue.js와 Bootstrap을 함께 사용하면, 동적이고 풍부한 사용자 인터페이스를 쉽게 구현할 수 있습니다.

### backend 프로그램 다시 기억하기

> 아래 프로그램을 Task 관리를 위한 backend 프로그램으로 다시 기억해 줘.
```python
from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # 이 부분이 CORS를 적용하는 부분입니다.
api = Api(app)

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
>> 해당 코드는 Python의 Flask 및 Flask-RESTx 라이브러리를 사용하여 작성된 Task 관리를 위한 백엔드 프로그램입니다.
<br>
이 프로그램은 다음과 같은 기능을 제공합니다:
<br>
>><li>모든 Task를 목록으로 반환(GET /tasks/)
>><li>새 Task를 생성(POST /tasks/)
>><li>주어진 식별자를 가진 Task를 반환(GET /tasks/{id})
>><li>주어진 식별자를 가진 Task를 삭제(DELETE /tasks/{id})
>><li>주어진 식별자를 가진 Task를 업데이트(PUT /tasks/{id})
>><br>또한 이 프로그램은 CORS(Cross-Origin Resource Sharing)를 지원하여, 다른 도메인에서 이 API에 접근할 수 있도록 해줍니다.<br>
>>해당 코드를 다시 기억하고, 이를 Task 관리를 위한 백엔드 프로그램으로 인식하겠습니다. 이후 관련 질문이 있으시면 이에 대한 자세한 설명과 함께 답변을 드리겠습니다.

### Task 관리 frontend 프로그램
> 위의 'Task 관리를 위한 백엔드 프로그램' 에 맞는 프론트앤트 프로그램을 작성해 줘. Vue.js 프레임워크 와 bootstrap을 사용하고 CDN 으로 실행가능 하도록 만들어 줘.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Task Management</title>
    <!-- Vue.js를 CDN을 통해 가져옵니다. -->
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
    <!-- Axios를 CDN을 통해 가져옵니다. -->
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <!-- Bootstrap CSS를 CDN을 통해 가져옵니다. -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <!-- Bootstrap JavaScript를 CDN을 통해 가져옵니다. -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
</head>
<body>
    <div id="app" class="container">
        <div class="form-group">
            <label for="taskInput">New Task</label>
            <input type="text" class="form-control" id="taskInput" v-model="newTask.task">
            <button class="btn btn-primary" @click="addTask">Add</button>
        </div>

        <ul class="list-group">
            <li class="list-group-item" v-for="task in tasks">
                {{ task.task }}
                <button class="btn btn-danger btn-sm float-right" @click="deleteTask(task.id)">Delete</button>
            </li>
        </ul>
    </div>

    <script>
        var app = new Vue({
            el: '#app',
            data: {
                tasks: [],
                newTask: {}
            },
            methods: {
                getTasks: function() {
                    axios.get('http://localhost:5000/tasks/')
                        .then(response => {
                            this.tasks = response.data;
                        });
                },
                addTask: function() {
                    axios.post('http://localhost:5000/tasks/', this.newTask)
                        .then(response => {
                            this.tasks.push(response.data);
                            this.newTask = {};
                        });
                },
                deleteTask: function(id) {
                    axios.delete('http://localhost:5000/tasks/' + id)
                        .then(response => {
                            this.tasks = this.tasks.filter(task => task.id != id);
                        });
                }
            },
            mounted: function() {
                this.getTasks();
            }
        });
    </script>
</body>
</html>

```