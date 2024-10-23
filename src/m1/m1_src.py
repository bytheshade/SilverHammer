from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

class Inter:
    @staticmethod
    def polyDeg2Frac(coefficents, deg=None, frac=True):
        """
        Convert the given coefficients to fractions.

        Parameters:
        coefficents (array): A array of coefficients to be converted.
        deg (int, optional): The degree of the coefficients. Defaults to None, 
                             in which case len(coefficents) is used.
        frac (bool, optional): Whether to convert to fractions. Defaults to True.

        Returns:
        array: A array of coefficients converted to fractions.
        """
        # If deg is None, use len(coefficent)
        if deg == None:
            deg = len(coefficents)

        coefficents_frac = [Fraction(i).limit_denominator() for i in coefficents]

        return coefficents_frac

    @staticmethod
    def getPolyEq(x, y, deg=None, sym='**'):
        """
        Generate a polynomial from the given x and y values and return its coefficients.

        Parameters:
        x (array): A array of x values.
        y (array): A array of y values.
        deg (int, optional): The degree of the polynomial. Defaults to None, 
                             in which case len(y) - 1 is used.
        sym (str, optional): The symbol for exponentiation in the polynomial. 
                             Defaults to '**'.

        Returns:
        str: A string representation of the generated polynomial.
        """
        if deg == None:
            # If there is no degree set, set the degree as len(y) -1
            deg = len(y) - 1
        
        # Use np.polyfit to find the coefficents
        coefficents = np.polyfit(x, y, deg)
        # Convert coefficents to fractions
        coefficents = Inter.polyDeg2Frac(coefficents)
        # Reverse it because when enumerate(coefficents), the key will not match with the value's degree
        coefficents = reversed(coefficents)

        equationList = []
        for key, value in enumerate(coefficents):
            equationList.append(f'{value} * x {sym} {key}')
        
        # Reverse the list back to maintain standard polynomial order
        equationList = reversed(equationList)

        equation = ' + '.join(equationList)

        # Remove x ** 0
        equation = equation.replace(f' * x {sym} 0', '')

        return equation
    
    # TODO: construct graphing logic
    # 1. Draw points on where given x values are.
    # 2. Give 
    @staticmethod
    def graphPoly(x_points, y_points=None, equation=None, range=(None)):
        if x_points is None and y_points is None:
            raise ValueError("Both y_points and equation cannot be None.")

        if range is None:
            # default range
            range = (min(x_points), max(x_points))
        
        if equation is None:
            equation = Inter.getPolyEq(x_points, y_points)

        range_distance = np.abs(range[0]-range[1])

        # Use Sympy to solve issue that putting equation does not work because it is a string.
        # One another option I could do such as eval(equation.replace('x', 'x')), eval(equation.replace('x', 'x_points'))
        # but they were too risky
        x_sym = sp.symbols('x')
        expr = sp.sympify(equation)

        x = np.linspace(range[0], range[1], int(range_distance*100))

        y_values = [expr.subs(x_sym, val) for val in x] 

        fig = plt.figure(figsize=(8, 6))
        plt.title(f'{expr}')
        plt.style.use('ggplot')

        plt.plot(x, y_values, color='r', ls='--', linewidth='2', zorder=1)

        if y_points is not None:
            plt.scatter(x_points, y_points, color='blue', label='Data points', zorder=2)
        if y_points is None:
            y_points = [expr.subs(x_sym, val) for val in x_points]
            
            plt.scatter(x_points, y_points, color='blue', label='Data points', zorder=2)
        
        # plt.axis([x_points[0]-10, x_points[-1]+10, min(y_points)-10, max(y_points)+10])
        plt.grid()
        plt.show()

        

if __name__ == "__main__":
    x = [i for i in range(1, 6)]
    y = [1, 10, 3, 6, 7]

    Inter.graphPoly(x, y, None)