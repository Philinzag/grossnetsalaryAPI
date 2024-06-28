## Project Setup and Usage Guide

## Overview
The GrossNetSalaryAPI calculates the gross salary based on the desired net salary and allowances. It also provides additional details such as Basic Salary, Total PAYE Tax, Employee Pension Contribution, and Employer Pension Contribution.

### Prerequisites

Ensure you have the following installed on your machine:
- Python 3.7+
- `pip` (Python package installer)
- `virtualenv` (optional but recommended)

### Steps to Run the Application

1. **Clone the Repository**

   Open your terminal and clone the repository:

   ```bash
   git clone https://github.com/Philinzag/grossnetsalaryAPI
   cd flask_gross_net_salary
   ```

2. **Create a Virtual Environment**

   It's a good practice to create a virtual environment to manage your project dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   Start the Flask application:

   ```bash
   python app.py
   ```

   The application should now be running on `http://localhost:5000`.

### Testing the Application

1. **Install Test Dependencies**

   Ensure you have `Flask-Testing` installed. It should be listed in your `requirements.txt`, but if not, you can install it manually:

   ```bash
   pip install Flask-Testing
   ```

2. **Run Tests**

   Run the automated tests using the `unittest` framework:

   ```bash
   python -m unittest discover -s tests
   ```

   You should see output indicating the results of your tests.

3. **Run Tests with Coverage (Optional)**

   To check how much of your code is covered by tests, you can use the `coverage` tool:

   ```bash
   pip install coverage
   coverage run -m unittest discover -s tests
   coverage report
   ```

   Optionally, you can generate an HTML report:

   ```bash
   coverage html
   ```

   Open the `htmlcov/index.html` file in a web browser to view the coverage report.

### Project Structure

Here is a brief overview of the project structure:

```
flask_gross_net_salary/
├── app.py                  # Main application file
├── models.py               # Data models
├── services.py             # Salary calculation logic
├── tests/                  # Directory containing test cases
│   └── test_salary_calculator.py
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation (this file)
```

### API Usage

#### Endpoint

- **POST /api/salary**

  This endpoint calculates the gross salary based on the desired net salary and allowances.

#### Request Body

Send a JSON object with the following structure:

```json
{
  "desired_net_salary": 1000,
  "allowances": 200
}
```

#### Response

The response will be a JSON object containing the calculated salary details:

```json
{
  "gross_salary": 1234,
  "basic_salary": 1034,
  "total_allowances": 200,
  "paye_tax": 50,
  "employee_pension_contribution": 30,
  "employer_pension_contribution": 40
}
```
