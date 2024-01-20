from typing import Iterable, Union
from numbers import Real

from regressors.regressor_abc import RegressorABC


class RegressorLSM(RegressorABC):

    _abscissa = None
    _ordinate = None

    def fit(self, abscissa: Iterable, ordinates: Iterable) -> None:
        if len(abscissa) == 0:
            raise RuntimeError("Abscissa length must be not empty")
        if len(ordinates) == 0:
            raise RuntimeError("Ordinates length must be not empty")
        if len(abscissa) != len(ordinates):
            raise RuntimeError("Abscissa and ordinates must have equal length")
        
        self._abscissa = abscissa
        self._ordinate = ordinates

    def predict(self, abscissa: Union[Real, Iterable]) -> list:
        
        mean_abs = self._mean_val_(self._abscissa)
        mean_ord = self._mean_val_(self._ordinate)
        mean_abs_ord = self._mean_func_val_(lambda x, y: x*y, self._abscissa, self._ordinate)
        mean_abs_pow = self._mean_func_val_(lambda x: x**2, self._abscissa)

        a = ( mean_abs_ord - mean_abs * mean_ord ) / ( mean_abs_pow - mean_abs ** 2 )
        b = mean_ord - a * mean_abs

        res = [ a*x + b for x in abscissa]
        return res
    
    def _mean_val_(self, list_val):
        return sum(list_val) / len(list_val)
    def _mean_func_val_(self, func, *list_val):
        new_val = list(map(func, *list_val))
        return sum(new_val) / len(new_val)
        

