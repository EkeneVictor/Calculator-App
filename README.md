# Calculator App with Currency Converter

## Overview

This is a simple calculator application built using **PyQt6**. The app provides basic calculator functionalities like addition, subtraction, multiplication, division, square roots, percentages, and exponents. Additionally, it includes a currency converter that fetches real-time exchange rates using an external API.

## Features

### Basic Calculator

- Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
- Handles square root calculations.
- Supports exponentiation using the `x²` button.
- Backspace functionality to delete digits one by one.
- Error handling for invalid operations.

### Currency Converter

- Allows users to convert between two currencies based on the latest exchange rates.
- Utilizes an external API to fetch real-time currency rates.
- Supports conversion between various currencies.

## Installation

### Prerequisites

- **Python 3.9+**
- **PyQt6**
- **requests** library for currency conversion API.

### Setup

1. **Clone the Repository**:

    ```bash
    git clone <https://github.com/EkeneVictor/Calculator-App>
    ```

2. **Install the required dependencies**:

    ```bash
    pip install pyqt6 requests
    ```

3. **Run the application**:

    ```bash
    python calculator.py
    ```

4. **UI File**:

   The application uses a UI file (`calculator.ui`), which should be included in the project folder. This file was created using Qt Designer.

## How to Use

### Calculator

- Use the number buttons (`0–9`) to enter numbers.
- Use the operators (`+`, `-`, `*`, `/`) to perform calculations.
- Click on `=` to evaluate the expression.
- The `√` button calculates the square root, while `x²` is used for exponentiation.
- Use the backspace button to delete the last character entered.
- The `C` button clears the current expression.

### Currency Converter

- Enter the amount to be converted.
- Choose the source currency from the first dropdown and the target currency from the second dropdown.
- Click the `Convert` button to see the converted amount.

## API for Currency Conversion

The currency converter uses the ExchangeRate-API to fetch live currency exchange rates. You can modify the API endpoint and add your API key to the `convert_currency()` method.

```python
response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
```

Make sure to replace the URL with your API endpoint and add your API key if necessary.

## Project Structure

```bash
├── calculator.py           # Main Python script for the calculator
├── calculator.ui           # UI file for the calculator (created in Qt Designer)
├── README.md               # Project README file
└── requirements.txt        # Dependencies (optional)
```
## Known Issues

- The application uses the `eval()` function to evaluate expressions, which can be dangerous if not handled properly. Consider sanitizing inputs to prevent potential security risks.
- The API call for currency conversion lacks retry logic, so it might fail if the API is temporarily unreachable.

## Future Enhancements

- Add support for more advanced scientific calculations.
- Improve error handling for currency conversion failures.
- Implement an offline mode for the currency converter using cached exchange rates.

## License

This project is licensed under the cipher License.

