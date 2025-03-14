import numpy as np
import matplotlib.pyplot as plt

def compute_gradient(function, x_range=(-50, 50.1, 0.1)):
    """
    Computes the gradient using finite differences.
    
    Parameters:
    function : function
        The function to compute values for.
    x_range : tuple
        The range of x values (start, stop, step).
    
    Returns:
    array_xy : ndarray
        Concatenated x and y values.
    gradient : ndarray
        The gradient of the function.
    """
    x = np.arange(*x_range)
    y = function(x)
    gradient = np.diff(y) / np.diff(x)  # Compute gradient using finite differences
    array_xy = np.column_stack((x, y))
    
    return array_xy, gradient

def function1(x):
    return (1/2) * x + 1

def function2(x):
    return x ** 2

def function3(x):
    return 2 * x ** 2 + 2 * x

def function4(x):
    return np.sin(x / 12)

def plot_function_and_gradient(x, y, gradient, title):
    """Plots function and its gradient."""
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(x, y, label='Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{title} Function')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(x[:-1], gradient, label='Gradient', color='red')
    plt.xlabel('x')
    plt.ylabel('Gradient')
    plt.title(f'{title} Gradient')
    plt.legend()
    
    plt.show()

# Compute gradients and plot results
for func, title in zip([function1, function2, function3, function4],
                        ['Linear', 'Quadratic', 'Quadratic 2', 'Sine']):
    array_xy, gradient = compute_gradient(func)
    plot_function_and_gradient(array_xy[:, 0], array_xy[:, 1], gradient, title)

# Find minimum y-value for each function
for func, title in zip([function2, function3, function4], ['Quadratic', 'Quadratic 2', 'Sine']):
    x = np.arange(-50, 50.1, 0.1)
    y = func(x)
    min_index = np.argmin(y)
    min_value = y[min_index]
    
    print(f"Minimum y-value for {title} function: {min_value} at x = {x[min_index]}")
