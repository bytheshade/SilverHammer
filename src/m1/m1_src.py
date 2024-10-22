from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np

class Inter:
    def __init__(self):
        pass

    @staticmethod
    def polyDeg2Frac(coefficents, deg=None, frac=True):
        # If deg is None, use len(coefficent)
        if deg == None:
            deg = len(coefficents)

        coefficents_frac = [Fraction(i).limit_denominator() for i in coefficents]

        return coefficents_frac

    @staticmethod
    def getPolyInt(x, y, deg=None, sym='**'):
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
            equationList.append(f'{value}x {sym} {key}')
        
        # Reverse the list back to maintain standard polynomial order
        equationList = reversed(equationList)

        equation = ' + '.join(equationList)

        # Remove x ** 0
        equation = equation.replace(f'x {sym} 0', '')

        return equation
    
    def graphPoly(equation, range=(None)):
        if range == None:
            # default range
            range = (-2, 7)

        # [Graphing logic here]


if __name__ == "__main__":
    pass