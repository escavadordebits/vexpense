from flask import Flask, make_response, jsonify
import json
from pip._vendor import requests
from datetime import date

app = Flask(__name__)


@app.route('/expenses', methods=['GET'])
def buscar_dados():
    today = date.today()
    url = f'https://api.vexpenses.com/v2/reports/status/APROVADO?include=expenses,user,expenses.apportionment,expenses.expense_type,expenses.costs_center,expenses.payment_method,expenses.gps,advance,payment_method,approval&search=approval_date:2023-07-01,2023-07-31&searchFields=approval_date:between;payment_date:>=;created_at:=&searchJoin=and'
    response = requests.get(url, headers={
                            'Authorization': 'x34kkOXnPTc9wMw2TLOuBMKuamYsQAvuPApdT3j5VHySScyndzEu8Nj60mLT'})
    res = json.loads(response.text)
    return make_response(
        jsonify(res)
    )


#app.run()
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5005)
