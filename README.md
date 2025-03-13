# Numpy Gradient Calculation

## Overview
This project demonstrates how to compute the gradient of different mathematical functions using NumPy. It also visualizes the functions and their gradients using Matplotlib.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install numpy matplotlib
```

Alternatively, if using Anaconda:

```bash
conda install numpy matplotlib
```

## Functions Implemented
The following mathematical functions are included:
1. **Linear Function**: \( y = \frac{1}{2}x + 1 \)
2. **Quadratic Function**: \( y = x^2 \)
3. **Quadratic Function with Linear Term**: \( y = 2x^2 + 2x \)
4. **Trigonometric Function**: \( y = \sin(\frac{x}{2}) \)

## Features
- Computes the gradient using finite differences.
- Plots both the function and its gradient.
- Finds and prints the minimum value of each function.

## Usage
Run the Python script to compute gradients and visualize results:

```bash
python script.py
```

## Output
The script generates plots showing:
- The function curve
- The gradient of the function
- Prints the minimum value of each function

## Example Output
```
Minimum of y = (1/2)x + 1: y = -24.0 at x = -50.0
Minimum of y = x^2: y = 0.0 at x = 0.0
Minimum of y = 2x^2 + 2x: y = -0.5 at x = -0.5
Minimum of y = sin(x/2): y = -1.0 at x = -47.12
```




