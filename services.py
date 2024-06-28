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
            gross_salary,
            basic_salary,
            request.allowances,
            paye_tax,
            employee_pension_contribution,
            self.calculate_employer_pension(basic_salary)
        )

    def calculate_employee_pension(self, basic_salary):
        return (basic_salary * self.TIER2_EMPLOYEE_RATE) + (basic_salary * self.TIER3_EMPLOYEE_RATE)

    def calculate_employer_pension(self, basic_salary):
        return (basic_salary * self.TIER1_EMPLOYER_RATE) + (basic_salary * self.TIER3_EMPLOYER_RATE)

    def calculate_paye_tax(self, taxable_income):
        if taxable_income <= 319:
            return taxable_income * 0.05
        if taxable_income <= 419:
            return 15.95 + ((taxable_income - 319) * 0.1)
        if taxable_income <= 539:
            return 25.95 + ((taxable_income - 419) * 0.175)
        if taxable_income <= 3549:
            return 46.45 + ((taxable_income - 539) * 0.25)
        return 876.45 + ((taxable_income - 3549) * 0.3)
