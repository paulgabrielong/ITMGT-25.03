{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "15f2a4bf-86f6-4634-a615-d457095b4e4f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def savings(gross_pay, tax_rate, expenses):\n",
    "    '''Savings.\n",
    "    5 points.\n",
    "\n",
    "    This function calculates the money remaining\n",
    "        for an employee after taxes and expenses.\n",
    "\n",
    "    To get the take-home pay of an employee, we will\n",
    "        follow the following process:\n",
    "        1. Apply the tax rate to the gross pay of the employee; round down\n",
    "        2. Subtract the expenses from the after-tax pay of the employee\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    gross_pay: int\n",
    "        the gross pay of an employee for a certain time period, expressed in centavos\n",
    "    tax_rate: float\n",
    "        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)\n",
    "    expenses: int\n",
    "        the expenses of an employee for a certain time period, expressed in centavos\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the number of centavos remaining from an employee's pay after taxes and expenses\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    tax = int(gross_pay * tax_rate)\n",
    "    total = int (gross_pay - tax - expenses)\n",
    "    return total"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "77789883-c605-48d7-bb21-e56cd81d882e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def material_waste(total_material, material_units, num_jobs, job_consumption):\n",
    "    '''Material Waste.\n",
    "    5 points.\n",
    "\n",
    "    This function calculates how much material input will be wasted\n",
    "        after running a certain number of jobs that consume\n",
    "        a set amount of material.\n",
    "\n",
    "    To get the waste of a set of jobs:\n",
    "        1. Multiply the number of jobs by the material consumption per job.\n",
    "        2. Subtract the total material consumed from the total material available.\n",
    "\n",
    "    The users of this function also want you to format the output as a string, annotated with the\n",
    "        units in which the material is expressed. Do not add a space between the number and the unit.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    total_material: int\n",
    "        the total material available\n",
    "    material_units: str\n",
    "        the units used to express a quantity of the material (e.g., \"kg\", \"L\", etc.)\n",
    "    num_jobs: int\n",
    "        the number of jobs to run\n",
    "    job_consumption: int\n",
    "        the amount of material consumed per job\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the amount of remaining material expressed with its unit (e.g., \"10kg\").\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "\n",
    "    total_consumed = int (job_consumption * num_jobs)\n",
    "    waste_from_jobs = str (total_material - total_consumed)\n",
    "    waste = (waste_from_jobs + str(material_units))\n",
    "    return waste"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8f454c82-b49b-4f51-bb26-70fc69d938eb",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'-19900kg'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "material_waste(100, \"kg\", 200, 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e68d92b2-28f7-45db-b1f9-3570cd38e42e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def interest(principal, rate, periods):\n",
    "    '''Interest.\n",
    "    5 points.\n",
    "\n",
    "    This function calculates the final value of an investment after\n",
    "        gaining simple interest over a number of periods.\n",
    "\n",
    "    To calculate simple interest, simply multiply the principal to the quantity (rate * time).\n",
    "        Add this amount to the principal to get the final value.\n",
    "\n",
    "    Round down the final amount.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    principal: int\n",
    "        the principal (i.e., starting) amount invested, expressed in centavos\n",
    "    rate: float\n",
    "        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)\n",
    "    periods: int\n",
    "        the number of periods invested\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the final value of the investment\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    amount = int(principal * (rate*periods))\n",
    "    simple_interest = int(amount + principal)\n",
    "    return simple_interest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "28e9e79c-7f35-4519-abb3-893de8fcf5b4",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "189"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "interest(100, 0.3, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1bd57a21-6df6-44c6-9583-2b1038c4c8bc",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def body_mass_index(weight, height):\n",
    "    '''Body Mass Index.\n",
    "    5 points.\n",
    "\n",
    "    This function calculates the body mass index (BMI) of a person\n",
    "        given their weight and height.\n",
    "\n",
    "    The formula for BMI is: kg / (m ^ 2)\n",
    "        (i.e., kilograms over meters squared)\n",
    "\n",
    "    Unfortunately, the users of this function use the imperial system.\n",
    "        You will need to first convert their arguments to the metric system.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    weight: float\n",
    "        the weight of the person, in pounds\n",
    "    height: list\n",
    "        the height of the person, expressed as a list of two integers.\n",
    "        the first integer is the foot component of their height.\n",
    "        the second integer is the inches component of their height.\n",
    "        for example, 5'10\" would be passed as [5, 10].\n",
    "\n",
    "    We have not yet discussed lists, but use the skills you developed\n",
    "        in the command line exercise. How would you learn how to work with\n",
    "        lists?\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    float\n",
    "        the BMI of the person.\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    \n",
    "    weight_kg = weight/2.205\n",
    "    height_m2 = ((int(str(height)[0])*12 + int(str(height)[1]))*0.0254)**2\n",
    "    bmi = weight_kg / height_m2\n",
    "    return bmi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7e89abd2-ada5-45cb-8ec1-4e02898d2ddf",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20.52295609428448"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "body_mass_index (135, 58)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0657640b-6032-4bd7-918e-de06c642a04a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
