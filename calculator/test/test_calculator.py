import pytest
from src.main import summation, subtraction, division, multiplication, Num_list, Number


# test summation function

def test_summation1():

  num_list_instance = Num_list(number_input=[10, 20, 30])
  actual = summation(num_list=num_list_instance)
  expected = 60
  message = f'calculator.summation([10,20,30]) returned {actual} instead of {expected}'

  assert actual == expected, message

def test_summation2():

  num_list_instance = Num_list(number_input=[0])
  actual = summation(num_list=num_list_instance)
  expected = 0
  message = f'calculator.summation([0]) returned {actual} instead of {expected}'

  assert  actual == expected , message

def test_summation3():

  num_list_instance = Num_list(number_input=[1,1])
  actual = summation(num_list=num_list_instance)
  expected = 2
  message = f'calculator.summation([1,1]) returned {actual} instead of {expected}'

  assert  actual == expected , message

def test_summation4():

  num_list_instance = Num_list(number_input=[100,10, 30])
  actual = summation(num_list=num_list_instance)
  expected = 140
  message = f'calculator.summation([100,10, 30]) returned {actual} instead of {expected}'

  assert  actual == expected , message


# testing the subtraction function

def test_subtraction1():

  num_list_instance = Num_list(number_input=[10,20,30])
  actual = subtraction(num_list=num_list_instance)
  expected = -40
  message = f'calculator.subtraction([10,20,30]) returned {actual} instead of {expected}'

  assert actual == expected , message

def test_subtraction2():

  num_list_instance = Num_list(number_input=[0])
  actual = subtraction(num_list=num_list_instance)
  expected = 0
  message = f'calculator.subtraction([0]) returned {actual} instead of {expected}'

  assert actual == expected, message

def test_subtraction3():

  num_list_instance = Num_list(number_input=[1,1])
  actual = subtraction(num_list=num_list_instance)
  expected = 0
  message = f'calculator.subtraction([1,1]) returned {actual} instead of {expected}'

  assert actual == expected , message

def test_subtraction4():

  num_list_instance = Num_list(number_input=[100,10, 30])
  actual = subtraction(num_list=num_list_instance)
  expected = 60
  message = f'calculator.subtraction([100, 10, 30]) returned {actual} instead of {expected}'

  assert actual == expected , message


# test division function

def test_division1():

  num_list_instance = Number(number_1=10, number_2=2)
  actual = division(number= num_list_instance)
  expected = 5
  message = f'calculator.division(10,2) returned {actual} instead of {expected}'

  assert actual == expected , message

def test_division2():

  num_list_instance = Number(number_1=1, number_2=1)
  actual = division(number= num_list_instance)
  expected = 1
  message = f'calculator.division(1,1) returned {actual} instead of {expected}'

  assert actual == expected, message

def test_division3():

  num_list_instance = Number(number_1=100, number_2=5)
  actual = division(number= num_list_instance)
  expected = 20
  message = f'calculator.division(100,5) returned {actual} instead of {expected}'

  assert actual == expected, message

def test_division4():

  num_list_instance = Number(number_1=1, number_2=0)
  actual = division(number= num_list_instance)
  expected = "zero division error, second number cannot be 0"
  message = f'calculator.division(1,0) returned {actual} instead of {expected}'

  assert actual == expected, message


# test multiplication function

def test_multiplication1():

  num_list_instance = Num_list(number_input=[10,20,30])
  actual = multiplication(num_list=num_list_instance)
  expected = 6000
  message = f'calculator.multiplication([10,20,30]) returned {actual} instead of {expected}'

  assert actual == expected, message

def test_multiplication2():

  num_list_instance = Num_list(number_input=[0])
  actual = multiplication(num_list=num_list_instance)
  expected = 0
  message = f'calculator.multiplication([0]) returned {actual} instead of {expected}'

  assert actual == expected , message

def test_multiplication3():

  num_list_instance = Num_list(number_input=[1,1])
  actual = multiplication(num_list=num_list_instance)
  expected = 1
  message = f'calculator.multiplication([1,1]) returned {actual} instead of {expected}'

  assert actual == expected, message

def test_multiplication4():

  num_list_instance = Num_list(number_input=[100,10, 30])
  actual = multiplication(num_list=num_list_instance)
  expected = 30000
  message = f'calculator.multiplication([100,10, 30]) returned {actual} instead of {expected}'

  assert actual == expected, message