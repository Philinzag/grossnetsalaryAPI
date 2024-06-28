from models import SalaryDetails

class SalaryCalculator:
    TIER1_EMPLOYER_RATE = 0.13
    TIER2_EMPLOYEE_RATE = 0.055
    TIER3_EMPLOYEE_RATE = 0.05
    TIER3_EMPLOYER_RATE = 0.05

    def calculate_gross_salary(self, request):
        gross_salary = request.desired_net_salary
        basic_salary = gross_salary - request.allowances
        employee_pension_contribution = self.calculate_employee_pension(basic_salary)
        taxable_income = basic_salary - employee_pension_contribution
        paye_tax = self.calculate_paye_tax(taxable_income)
        net_salary = taxable_income - paye_tax

        while net_salary < request.desired_net_salary:
            gross_salary += 1
            basic_salary = gross_salary - request.allowances
            employee_pension_contribution = self.calculate_employee_pension(basic_salary)
            taxable_income = basic_salary - employee_pension_contribution
            paye_tax = self.calculate_paye_tax(taxable_income)
            net_salary = taxable_income - paye_tax

        return SalaryDetails(
            gross_salary=gross_salary,
            basic_salary=basic_salary,
            total_allowances=request.allowances,
            paye_tax=paye_tax,
            employee_pension_contribution=employee_pension_contribution,
            employer_pension_contribution=self.calculate_employer_pension(basic_salary)
        )

    def calculate_employee_pension(self, basic_salary):
        return (basic_salary * self.TIER2_EMPLOYEE_RATE) + (basic_salary * self.TIER3_EMPLOYEE_RATE)

    def calculate_employer_pension(self, basic_salary):
        return (basic_salary * self.TIER1_EMPLOYER_RATE) + (basic_salary * self.TIER3_EMPLOYER_RATE)

    def calculate_paye_tax(self, taxable_income):
        tax_brackets = [
            {'max_income': 490, 'rate': 0.05},
            {'max_income': 730, 'rate': 0.1},
            {'max_income': 3896.67, 'rate': 0.175},
            {'max_income': 19896.67, 'rate': 0.25},
            {'max_income': 50416.67, 'rate': 0.3},
            {'max_income': float('inf'), 'rate': 0.35}
        ]

        tax = 0
        previous_max_income = 0

        for bracket in tax_brackets:
            if taxable_income <= bracket['max_income']:
                tax += (taxable_income - previous_max_income) * bracket['rate']
                break
            else:
                tax += (bracket['max_income'] - previous_max_income) * bracket['rate']
                previous_max_income = bracket['max_income']

        return tax
