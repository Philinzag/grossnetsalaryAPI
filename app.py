from flask import Flask, request, jsonify
from models import SalaryRequest
from services import SalaryCalculator

app = Flask(__name__)
calculator = SalaryCalculator()

@app.route('/api/salary', methods=['POST'])
def calculate_gross_salary():
    data = request.get_json()
    desired_net_salary = data.get('desired_net_salary')
    allowances = data.get('allowances')

    if desired_net_salary is None or allowances is None:
        return jsonify({"error": "Invalid input"}), 400

    salary_request = SalaryRequest(desired_net_salary, allowances)
    salary_details = calculator.calculate_gross_salary(salary_request)

    return jsonify({
        "gross_salary": salary_details.gross_salary,
        "basic_salary": salary_details.basic_salary,
        "total_allowances": salary_details.total_allowances,
        "paye_tax": salary_details.paye_tax,
        "employee_pension_contribution": salary_details.employee_pension_contribution,
        "employer_pension_contribution": salary_details.employer_pension_contribution
    })

if __name__ == '__main__':
    app.run(debug=True)
