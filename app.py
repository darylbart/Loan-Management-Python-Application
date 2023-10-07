from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate simple interest
def calculate_simple_interest(principal, interest_rate, loan_period):
    return (principal * interest_rate * loan_period) / 100

# Function to calculate compound interest
def calculate_compound_interest(principal, interest_rate, loan_period):
    return principal * ((1 + interest_rate / 100)**loan_period - 1)

# Route for handling the interest calculation
@app.route('/', methods=['GET', 'POST'])
def calculate_interest():
    if request.method == 'POST':
        # Retrieve user input from the form
        principal = request.form['principal']
        interest_rate = request.form['interest_rate']
        loan_period = request.form['loan_period']

        # Check for empty or invalid input
        if not (principal and interest_rate and loan_period):
            return "Please fill in all fields."

        try:
            principal = float(principal)
            interest_rate = float(interest_rate)
            loan_period = float(loan_period)
        except ValueError:
            return "Invalid input. Please enter valid numeric values."

        interest_type = request.form['interest_type']

        # Calculate interest based on the selected type (simple or compound)
        if interest_type == 'simple':
            interest = calculate_simple_interest(principal, interest_rate, loan_period)
        elif interest_type == 'compound':
            interest = calculate_compound_interest(principal, interest_rate, loan_period)
        else:
            return "Invalid interest type"

        # Calculate monthly, yearly, and lifetime interest
        monthly_interest = interest / (loan_period * 12)
        yearly_interest = interest / loan_period

        # Calculate total amount repaid
        total_amount_repaid = principal + interest

        # Render the result page with calculated values
        return render_template('result.html',
                               principal=principal,
                               interest_rate=interest_rate * 100,
                               loan_period=loan_period,
                               monthly_interest=monthly_interest,
                               yearly_interest=yearly_interest,
                               total_interest=interest,
                               total_amount_repaid=total_amount_repaid)

    # Render the input form page for the initial GET request
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
