from flask import Flask, json

companies = [{"id": 1, "name": "My HomeCompany One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)
@api.route('/arpi', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/greet', methods=['GET'])
def greeating():
    return "Hello Friend"
if __name__ == '__main__':
    api.run(host='localhost', port=80)