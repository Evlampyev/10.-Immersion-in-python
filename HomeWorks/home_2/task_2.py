"""Сложение дробей"""
from fractions import Fraction
from math import gcd

frac1: str = "2/3"
frac2: str = "1/4"

frac1_numerator, frac1_denominator = map(int, frac1.split('/'))
frac2_numerator, frac2_denominator = map(int, frac2.split('/'))

addition_numerator = frac1_numerator * frac2_denominator + frac2_numerator * frac1_denominator
addition_denominator = frac1_denominator * frac2_denominator
great_number = gcd(addition_numerator, addition_denominator)
print(f'Сумма дробей: {addition_numerator // great_number}/{addition_denominator // great_number}')

composition_numerator = frac1_numerator * frac2_numerator
composition_denumerator = frac1_denominator * frac2_denominator
great_number = gcd(composition_numerator, composition_denumerator)
print(f'Произведение дробей: {composition_numerator // great_number}/{composition_denumerator // great_number}')

fract_1 = Fraction(frac1_numerator, frac1_denominator)
fract_2 = Fraction(frac2_numerator, frac2_denominator)
print(f'Сумма дробей: {fract_2 + fract_1}')
print(f'Произведение дробей: {fract_2 * fract_1}')
