# Employee pay calculator

## Sample code
This repository contains some template code in a file called `employee.py`.  It contains an initial definition of an `Employee` class.  It also creates 6 `Employee` objects.

The `Employee` class contains a method called `get_pay()`.  This method should compute the pay for the employee object.  What a person's pay is depends the type of contract they have and what they have done in the past month.  It also contains a method called `__str__`.  This method is automatically invoked if the `Employee` object is converted to a string by means of the `str` function.  It should produce a string explaining how the pay has been calculated.

The repository also includes a file with tests called `employee_test.py`.  You must **not** touch this file.

## Background
Your task for this exercise is to extend the code in `employee.py` such that it can compute pay for different types of workers and produce an explanatory string

### Contract
Workers either have a salary contract or an hourly contract.  Workers on a salary contract earn the monthly salary.  The wage of a worker on on an hourly contract is their hourly wage * the number of hours worked.

### Commission
Some but not all workers also receive a commission.  There are two types of commission.  Some workers receive a fixed bonus on top of their salary.  Some workers receive a commission based on the number of contracts they have landed.  Their commission is the number of contracts landed * the commission per contract.

### Total pay
The total pay of worker is their contract pay + their commission (if any).  There are six different types of worker in this scenario and pay is calculated differently for each one:
1. Workers on an salary contract without commission.
2. Workers on an hourly contract without commission.
3. Workers on an salary contract with a bonus commission.
4. Workers on an hourly contract with a bonus commission.
5. Workers on an salary contract with a contract commission.
6. Workers on an hourly contract with a contract commission.

## Assignment
Your task is to extend `employee.py` such that all the tests pass.  Your solution must be able to calculate total pay from the parameters provided and produce a string that explains how pay is calculated.  You must use your solution to construct appropriate employee objects for the six employees identified in the `employee.py` file, as follows

### Tests
#### Billie
`billie.get_pay()` must return 4000.

`str(billie)` must equal *"Billie works on a monthly salary of 4000.  Their total pay is 4000."*

### Charlie
`charlie.get_pay()` must return 2500.

`str(charlie)` must equal *"Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500."*

#### Renee
`renee.get_pay()` must return 3800.

`str(renee)` must equal *"Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800."*

#### Jan
`jan.get_pay()` must return 4410.

`str(jan)` must equal *"Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410."*

#### Robbie
`robbie.get_pay()` must return 3500.

`str(robbie)` must equal *"Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500."*

#### Ariel
`ariel.get_pay()` must return 4200.

`str(ariel)` must equal *"Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200."*

### Expectations
To produce your solution, you may add any classes and methods you see fit. You may change the way the billie, charlie, renee, jan, robbie, and ariel objects are constructed.  You may also construct additional objects or objects or different types.  The only constraint on your solution is that the total pay must be calculated from the parameters provided using the formulae explained above.  

You must **not** change the `employee_test.py` file.  That means that you cannot add  arguments to the `get_pay` and the `__str__` methods for the billie, charlie, renee, jan, robbie, and ariel objects.  The output of these methods must be calculated solely from attributes of the objects.

When tackling this exercise, try to produce a solution that satisfies the tests first.  That should be quite easy.  Once you manage that, consider your design.  Can you adjust it to keep the classes small and avoid repetition of code?

## How to complete the exercise
To start work on the exercise, find the URL of this repository on GitHub and clone it to your machine with:

`$ git clone URL`

where `URL` is the URL of your repository on GitHub.  Find the `employee.py` file and complete your solution.

You can test your solution in the development environment by running pytest.  From the root of your Python project, simply run

`$ pytest`

If pytest has not been installed yet, run:

`$ pip3 install pytest`

I recommend that you test your solution locally, but you do not have to do this.  Once your exercise is complete, you need to push your repository with:

`$ git push`

GitHub will automatically test your solution.
