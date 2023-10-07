# 💸 Simple and Compound Interest Calculator

This web application calculates both simple and compound interest based on user input for principal amount, interest rate, and loan period. It provides the option to calculate interest using either simple interest or compound interest formulas.

## 🛠️ How It Works

The application is built using Flask, a lightweight and powerful web framework for Python. It consists of two main functions to calculate simple and compound interest, respectively. Here's an overview of the calculations:

### Simple Interest Formula

\[ \text{Simple Interest} = \frac{{\text{Principal} \times \text{Interest Rate} \times \text{Loan Period}}}{{100}} \]

### Compound Interest Formula

\[ \text{Compound Interest} = \text{Principal} \times \left(1 + \frac{{\text{Interest Rate}}}{{100}}\right)^{\text{Loan Period}} - \text{Principal} \]

**Manipulating the Formulas:**
- You can experiment with different values of principal, interest rate, and loan period to understand how the interest changes.

## 🚀 How to Use

1. Make sure you have Python installed on your machine.

2. Install the required dependencies using pip:

   ```bash
   pip install Flask
   python3 app.py
   ```

5. Open your web browser and visit [http://localhost:5000](http://localhost:5000).

6. Fill in the form with the principal amount, interest rate, loan period, and select the type of interest (simple or compound).

7. Click on the "Calculate" button to see the calculated interest and other related details.

## ❗ Possible Bugs/Errors

- The application currently does not handle negative or zero values for principal, interest rate, or loan period.
- If the user enters non-numeric values for input, the application will not provide meaningful calculations.

## 🛣️ Roadmap

- **Version 1.1: Enhancement of UI**
  - Add a sleeker UI to improve user experience.
  - Implement real-time feedback and validation for user inputs.

- **Version 1.2: Error Handling and Robustness**
  - Implement error handling for invalid inputs to provide clear messages to the user.
  - Ensure the application can handle a high volume of requests without crashing or slowing down.
