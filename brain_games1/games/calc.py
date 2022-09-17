import random
import operator

CONDITION = 'What is the result of the expression?'

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def math_function(num_1, num_2, op):
    operation = OPERATORS.get(op)
    return operation(num_1, num_2)


def get_answer():

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    op = random.choice(list(OPERATORS))

    question = f'{num_1} {op} {num_2} = '

    correct_answer = math_function(num_1, num_2, op)

    return question, str(correct_answer)
