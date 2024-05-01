import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Num_list(BaseModel):
    number_input: List[float]
    
class Number(BaseModel):
    number_1: float
    number_2: float

app = FastAPI()


@app.post("/calculator/summation/")
def summation(num_list: Num_list):

    '''This function can take unlimited amount of numbers and is used to sum all the numbers together'''

    array = np.array(num_list.number_input)
    result = np.sum(array)

    return result

@app.post("/calculator/subtraction/")
def subtraction(num_list: Num_list):

    '''This function can take unlimited amount of numbers and is used to subtract all the numbers'''

    result = num_list.number_input[0] - sum(num_list.number_input[1:])

    return result

@app.post("/calculator/multiplication/")
def multiplication(num_list: Num_list):

    '''This function can take unlimited amount of numbers and is used to multiply all the numbers'''

    result = num_list.number_input[0]

    for i in num_list.number_input[1:]:
      result = result * i

    return result

@app.post("/calculator/division/")
def division(number: Number):

    '''This funtion only takes two numbers and is used to divide the first number by the second number'''

    if number.number_2 == 0:

      result = "zero division error, second number cannot be 0"

    else:

      result = number.number_1 / number.number_2

    return result