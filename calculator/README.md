# 계산기 프로그램

## 백엔드 프로그램
>파이썬으로 계산기 프로그램 만들기. Flask를 사용하고 flask_restx 를 사용하여 swagger를 제공하고 CORS 이슈가 없도록 하고 math 모듈을 사용하여 공학용 계산이 가능 하도록 백엔드 프로그램을 만들어 줘. 

```python
from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_cors import CORS
import math
import logging # 로깅 모듈 추가

app = Flask(__name__)
CORS(app)
api = Api(app, title='Calculator API', version='1.0', description='A simple Calculator API')

ns = api.namespace('calculator', description='Calculator operations')

calculator_fields = api.model('Calculator', {
    'a': fields.String(required=True, description='First input value'),
    'b': fields.String(required=False, description='Second input value'),
    'operation': fields.String(required=True, description='Operation to perform', enum=['+', '-', '*', '/', 'sqrt', 'pow', 'log', 'sin', 'cos', 'tan'])
})

# 로거 설정
logging.basicConfig(filename='calculator.log', level=logging.DEBUG)

def calculate(a, b, operation):
    a = float(a)
    b = float(b) if b else None

    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            api.abort(400, "Can't divide by 0")
    elif operation == 'sin':
        return round(math.sin(math.radians(a)), 3)
    elif operation == 'cos':
        return round(math.cos(math.radians(a)), 3)
    elif operation == 'tan':
        return round(math.tan(math.radians(a)), 3)
    elif operation == 'sqrt':
        return math.sqrt(a)
    elif operation == 'pow':
        return math.pow(a, b)
    elif operation == 'log':
        if b > 0:
            return math.log(a, b)
        else:
            api.abort(400, "b (base) must be greater than 0 for log operation")


@ns.route('/')
class CalculatorAPI(Resource):
    @ns.expect(calculator_fields, validate=True)
    @ns.doc(responses={
        200: 'OK',
        400: 'Invalid Argument',
        500: 'Mapping Key Error'
    })
    def post(self):
        '''Perform a calculation'''
        data = request.json
        a = data['a']
        b = data.get('b')  # b is not required for sqrt operation
        operation = data['operation']
        result = calculate(a, b, operation)
        
        # 로깅
        logging.debug(f"a: {a}, b: {b}, operation: {operation}, result: {result}")

        return {'result': result}


if __name__ == '__main__':
    app.run(debug=False)
```
## 프론트 엔트 프로그램

>위 백엔드 프로그램을 활용할 수 있도록 계산기 UI를 사용하도록 프론트엔드 프로그램을 작성해 줘. Vue.js를 CDN 모드로 사용할 수 있도록 하고, bootstrap을 활용한 디자인을 사용할 수 있도록 해 줘. UI는 공학용 계산기와 유사하게 만들어 줘.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Engineering Calculator</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.12"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.19.2/axios.min.js"></script>
</head>
<body>
    <div id="app" class="container mt-4">
        <h1 class="mb-4">Engineering Calculator</h1>
        <div class="jumbotron">
            <h2>{{ a }} {{ operation }} {{ b }}</h2>
            <h2 v-if="result != null">Result: {{ result }}</h2>
        </div>

        <div class="row">
            <div class="col-9">
                <button v-for="num in numbers" @click="appendNum(num)" class="btn btn-secondary btn-lg mr-1 mb-1">{{ num }}</button>
            </div>
            <div class="col-3">
                <button @click="calculate" class="btn btn-primary btn-lg">=</button>
            </div>
        </div>

        <div class="row mt-3">
            <div class="col-9">
                <button v-for="op in operations" @click="setOperation(op)" class="btn btn-secondary btn-lg mr-1 mb-1">{{ op }}</button>
            </div>
            <div class="col-3">
                <button @click="clear" class="btn btn-danger btn-lg">C</button>
            </div>
        </div>
    </div>

    <script>
        new Vue({
            el: '#app',
            data: {
                a: '',
                b: '',
                operation: null,
                result: null,
                numbers: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'],
                operations: ['+', '-', '*', '/', 'sqrt', 'pow', 'log', 'sin', 'cos', 'tan']
            },
            methods: {
                appendNum: function(num) {
                    if (this.operation) {
                        this.b += num;
                    } else {
                        this.a += num;
                    }
                },
                setOperation: function(op) {
                    this.operation = op;
                },
                calculate: function() {
                    var vm = this;
                    axios.post('http://localhost:5000/calculator/', {
                        a: vm.a,
                        b: vm.b,
                        operation: vm.operation
                    })
                    .then(function(response) {
                        vm.result = response.data.result;
                    })
                    .catch(function(error) {
                        console.log(error);
                    });
                },
                clear: function() {
                    this.a = '';
                    this.b = '';
                    this.operation = null;
                    this.result = null;
                }
            }
        });
    </script>
</body>
</html>
```

