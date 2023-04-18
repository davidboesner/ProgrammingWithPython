'''
Created on 14.04.2023

@author: david
'''
from hamcrest.core.core.isnone import none

"""
The purpose of this class is to find the ideal function, which is the best fit out of the functions provided.
The criterion for choosing the ideal functions for the training function is how they minimize the sum of all ydeviations squared (Least-Square)
"""

import doctest

from exceptions.IllegalTypeException import IllegalTypeException
from exceptions.UnequalsLenghtException import UnequalLengthExcpetion
from function_xy import FunctionXY
from numbaAdder import get_sum_of_deviations_squared
import numpy as np

class Function2Compare():
    f1 = None
    f2 = None
    index_of_compared_function = None
    
    def __init__(self, f1,f2,index_of_compared_function):
        if not isinstance(f1, FunctionXY) or not isinstance(f2, FunctionXY):
            raise IllegalTypeException();
        
        self.f1 = f1
        self.f2 = f2
        self.index_of_compared_function = index_of_compared_function
        
    def __get_sum_of_y_deviations_squared(self):
        """
        Gets the sum of the deviations between the functions f1 and f2 sqaured
        """

        # check input
        if len(self.f1.get_x_values())!=len(self.f2.get_x_values()):
            raise UnequalLengthExcpetion()
        
        # sum y values
        y1 = np.array(self.f1.get_y_values())
        y2 = np.array(self.f2.get_y_values())

        return get_sum_of_deviations_squared(y1, y2)
    
    def __eq__(self, other):        
        return self.__get_sum_of_y_deviations_squared() == other.__get_sum_of_y_deviations_squared()
    
    def __lt__(self, other):        
        return self.__get_sum_of_y_deviations_squared() < other.__get_sum_of_y_deviations_squared()
    
    def __gt__(self, other):
        return self.__get_sum_of_y_deviations_squared() > other.__get_sum_of_y_deviations_squared()
    
    def get_f1(self):
        return self.f1
    
    def get_f2(self):
        return self.f2
    
    def get_index_of_compared_function(self):
        return self.index_of_compared_function
    
class IdealDatasetFinder():
    all_datasets = None
    function = None
    
    def __init__(self, a, f):
        self.all_datasets = a
        self.function = f
    
    def get_func_with_least_y_squares(self):
        l = []
        for ds in self.all_datasets:
            fc = Function2Compare(self.function,ds,ds.get_n())
            l.append(fc)
        return min(l);
    
if __name__ == '__main__':
    doctest.testmod()