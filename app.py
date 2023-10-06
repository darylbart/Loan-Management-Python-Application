from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_simple_interest(principal, interest_rate, loan_period):
    return (principal * interest_rate * loan_period) / 100

def calculate_compound_interest(principal, interest_rate, loan_period):
    return principal * (1 + interest_rate / 100)**loan_period - principal

@app.route('/', methods=['GET', 'POST'])
def calculate_interest():
    if request.method == 'POST':
        principal = float(request.form['principal'])
        interest_rate = float(request.form['interest_rate'])
        loan_period = float(request.form['loan_period'])
        interest_type = request.form['interest_type']

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

        return render_template('result.html', 
                               principal=principal, 
                               interest_rate=interest_rate*100,
                               loan_period=loan_period,
                               monthly_interest=monthly_interest,
                               yearly_interest=yearly_interest,
                               total_interest=interest,
                               total_amount_repaid=total_amount_repaid)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
