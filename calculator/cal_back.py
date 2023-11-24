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