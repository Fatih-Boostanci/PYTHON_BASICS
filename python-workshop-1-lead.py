{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<center><img src=\"https://github.com/aaron-clarusway/fullstack/blob/master/itf-logo.png?raw=true\"  alt=\"alt text\" width=\"200\"/></center>\n",
    "<br>\n",
    "<h1><p style=\"text-align: center; color:darkblue\">Python Basic</p><h1>\n",
    "<center><h1>Workshop - 1</h1></center>\n",
    "<p><img align=\"right\"\n",
    "  src=\"https://secure.meetupstatic.com/photos/event/3/1/b/9/600_488352729.jpeg\"  width=\"15px\"></p>\n",
    "<br>\n",
    "\n",
    "\n",
    "# Subject: Basic Data Types and Useful Operations\n",
    "\n",
    "## Learning Goals\n",
    "\n",
    "* to work with quotes in strings,\n",
    "* to practice basic data types,\n",
    "* to consolidate basic boolean operations."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q1\n",
    "\n",
    "Write a program that multiplies three numbers entered by the user. Print the output with the format method."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "a=int(input(\"a:\"))\n",
    "b=int(input(\"b:\"))\n",
    "c=int(input(\"c:\"))  \n",
    "\n",
    "output = a * b * c\n",
    "\n",
    "print(\"{}*{}*{} = {}\".format(a, b, c, output))\n",
    "print(f\"{a}*{b}*{c} = {output}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q2\n",
    "\n",
    "Write a program that calculates body mass index from **height** and **weight** entered by the user. \n",
    "\n",
    "Body mass index :  Weight / Height(m) * Height(m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "height=float(input(\"Enter your height (example: 1.85):\"))\n",
    "weight=int(input(\"Enter your weight (example: 75):\"))\n",
    "\n",
    "print(\"Body mass index:\",weight / (height ** 2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Problem 3\n",
    "\n",
    "\n",
    "#### With your $200, how many  pieces of material can you get for $11 each? How much money do you have left after buying?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "totalMoney = 200\n",
    "materialPrice = 11\n",
    "piece = 200 // 11\n",
    "remainingMoney = totalMoney % piece\n",
    "print(\"With your ${}, {} pieces of material you can get for ${} each.  The remaining money is ${}\".format(totalMoney, piece, materialPrice, remainingMoney))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Problem 4\n",
    "\n",
    "Get **word**, **seperator** and **repetition** values from the user and print the word on the screen according to the given values. \n",
    "\n",
    "Ex: ``word = ali, sep = /, repetition = 3`` ----> ``ali/ali/ali``"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "word = input(\"Word: \")\n",
    "seperator = input(\"Seperator: \")\n",
    "repetitions = int(input(\"repetitions: \"))\n",
    "a = (word + seperator) * (repetitions -1) + word # henry/ * 2 = henry/henry/henry\n",
    "print(a)\n",
    "# print(*list([word] * repetitions), sep=seperator)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Problem 5\n",
    "\n",
    ">Do not run the code, try to figure out in your mind.\n",
    "\n",
    "What will be the output of the following syntax :\n",
    "\n",
    "```python\n",
    "print(True and False and (not True and False) and not (True or False))\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(True and False and (not True and False) and not (True or False))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Problem 6\n",
    "\n",
    ">Do not run the code, try to figure out in your mind.\n",
    "\n",
    "What will be the output of the following syntax :\n",
    "\n",
    "```python\n",
    "print(True and False and not \"False\" and None and (\"None\" or None))\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(True and False and not \"False\" and None and (\"None\" or None))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q7\n",
    "\n",
    ">Do not run the code, try to figure out in your mind.\n",
    "\n",
    "What will be the output of the following syntax :\n",
    "\n",
    "```python\n",
    "print(\"clarusway\" and 0 and not \"\" and False and (\" \" or None))\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "print(\"clarusway\" and 0 and not \"\" and False and (\" \" or None))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# WS-2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Code Challenge -1¶\n",
    "💡Objective:\n",
    "To improve your boolean logic and arithmetic operator algorithm skills.\n",
    "Using the all following items once each, set a correct boolean expression that returns write me. Use the print() function to display the result.\n",
    "0\n",
    "and\n",
    "not\n",
    "\"write me\"\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Solution - 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(not 0 and \"write me\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Code Challenge-2\n",
    "💡Objective:\n",
    "To improve your boolean logic algorithm and truth value skills.\n",
    "Find out if a given year is a \"leap\" year.\n",
    "\n",
    "In the Gregorian calendar, three criteria must be taken into account to identify leap years:\n",
    "\n",
    "The year must be evenly divisible by 4;\n",
    "If the year can also be evenly divided by 100, it is not a leap year; unless...(next one)\n",
    "The year is also evenly divisible by 400. Then it is a leap year.\n",
    "According to these rules, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.\n",
    "\n",
    "Write a Python program that;\n",
    "\n",
    "Takes a 4-digit year from the user,\n",
    "Prints True if the given year by the user is a leap year, prints False otherwise.\n",
    "Note that; this question is famous on the web, so that do it yourself to get more benefits from it."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Solution-2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "year = int(input(\"enter the year to check: \"))\n",
    "print(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Code Challenge-3\n",
    "💡Objective:\n",
    "To improve your collection type knowledge, using new built-in function comprehension, string formatting and problem solving skills.\n",
    "Task - 1 :\n",
    "You work for a manufacturer as a programmer and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary (sales) containing the cost price per unit (in dollars), sell price per unit (in dollars), and the beginning inventory. Write a program to return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold. The name and the keys of the dictionary are constant, so use them as they are.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The example of the values (sell-cost value, inventory) and total profit :\n",
    "\n",
    "sales = {\n",
    "  \"cost_value\": 31.87,\n",
    "  \"sell_value\": 45.00,\n",
    "  \"inventory\": 1000\n",
    "}  \n",
    "\n",
    "# the profit will be : 13130"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Task - 2 :\n",
    "Your boss wants you to prepare the payrolls of the workers in your department. You have to convert the amount of dollars into payroll format. In order to help move things along, you have volunteered to write a code that will take a float and return the money in the following format (as dollars and cents). \n",
    "\n",
    "\n",
    "Examples :\n",
    "Given Float Type amount\tDesired Output\n",
    "3\t$3.00\n",
    "29.99\t$29.99\n",
    "4.1\t$4.10\n",
    "The output should be float type as well and two digits after the period.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Solution-3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Task-1\n",
    "\n",
    "sales = {\n",
    "  \"cost_value\": 31.87,\n",
    "  \"sell_value\": 45.00,\n",
    "  \"inventory\": 1000\n",
    "}  \n",
    "\n",
    "print(round((sales[\"sell_value\"] - sales[\"cost_value\"]) * sales[\"inventory\"]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Task-2\n",
    "money = float(input(\"what is the payroll: \"))\n",
    "print(\"{0:.2f}\".format(money))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# TW_6"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 6, 10]\n"
     ]
    }
   ],
   "source": [
    "a=[1,2,3,4]\n",
    "b=[sum(a[0:x+1]) for x in range(0,len(a))]\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# L1 = []\n",
    "# L1.append([1, [2, 3], 4])\n",
    "# L1.extend([7, 8, 9])\n",
    "# print(L1[0][1][1] + L1[2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "L1 = []\n",
    "L1 = L1.append([1, [2, 3], 4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[1, [2, 3], 4]]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "L1 = L1.extend([7, 8, 9])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[1, [2, 3], 4], 7, 8, 9]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n"
     ]
    }
   ],
   "source": [
    "print(L1[0][1][1] + L1[2])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# T = (1, 2, 3, 4, 5, 6, 7, 8)\n",
    "# print(T[T.index(5)], end = \" \")\n",
    "# print(T[T[T[6]-3]-6])# "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 "
     ]
    }
   ],
   "source": [
    "T = (1, 2, 3, 4, 5, 6, 7, 8)\n",
    "print(T[T.index(5)], end = \" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "print(T[T[T[6]-3]-6])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# D = {1 : 1, 2 : '2', '1' : 1, '2' : 3}\n",
    "# D['1'] = 2\n",
    "# print(D[D[D[str(D[1])]]])# "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1: 1, 2: '2', '1': 2, '2': 3}"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "D = {1 : 1, 2 : '2', '1' : 1, '2' : 3}\n",
    "D['1'] = 2\n",
    "D"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "print(D[D[D[str(D[1])]]])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# set1 = {1, 2, 3}\n",
    "# set2 = set1.copy()\n",
    "# set2.add(4)\n",
    "# print(set1)# "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "set1 = {1, 2, 3}\n",
    "set2 = set1.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3}"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "set2.add(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3}"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "c = {1, 2, 3}.add(4)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
