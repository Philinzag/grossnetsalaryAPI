import unittest
from flask import Flask, json
from flask_testing import TestCase
from app import app

class SalaryCalculatorTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_calculate_gross_salary(self):
        tester = self.client
        response = tester.post('/api/salary', 
                               data=json.dumps({
                                   'desired_net_salary': 1000,
                                   'allowances': 200
                               }),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreater(data['gross_salary'], 1000)
        self.assertEqual(data['total_allowances'], 200)

if __name__ == '__main__':
    unittest.main()
