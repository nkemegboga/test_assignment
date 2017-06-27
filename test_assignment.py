import os


def my_print_function():

    return "Hello, World!"

def my_equal_to_function():

    return 1


def test_my_print_function():

    environment_variable = os.environ['ANSWER1']

    assert my_print_function() == environment_variable

def test_my_equal_to_function():

    environment_variable = int(os.environ['ANSWER2'])

    assert my_equal_to_function() == environment_variable



