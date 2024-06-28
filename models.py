class SalaryDetails:
    def __init__(self, gross_salary, basic_salary, total_allowances, paye_tax, employee_pension_contribution, employer_pension_contribution):
        self.gross_salary = gross_salary
        self.basic_salary = basic_salary
        self.total_allowances = total_allowances
        self.paye_tax = paye_tax
        self.employee_pension_contribution = employee_pension_contribution
        self.employer_pension_contribution = employer_pension_contribution

class SalaryRequest:
    def __init__(self, desired_net_salary, allowances):
        self.desired_net_salary = desired_net_salary
        self.allowances = allowances
