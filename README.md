# Coding assignment for itemis CC Cloud & Enterprise recruiting

## Problem 3: MERCHANT'S GUIDE TO THE GALAXY

This is an implementation of the assigment done by Artem Lukin for itemis AG

### Rules

You decided to give up on earth after the latest financial collapse left 99.99% of the earth's population with 0.01% of the wealth. Luckily, with the scant sum of money that is left in your account, you are able to afford to rent a spaceship, leave earth, and fly all over the galaxy to sell common metals and dirt (which apparently is worth a lot). Buying and selling over the galaxy requires you to convert numbers and units, and you decided to write a program to help you.

The numbers used for intergalactic transactions follows similar convention to the romannumerals and you have painstakingly collected the appropriate translation between them.

Input to your program consists of lines of text detailing your notes on the conversion
between intergalactic units and roman numerals. You are expected to handle invalid queries
appropriately.

Test input:

- glob is I
- prok is V
- pish is X
- tegj is L
- glob glob Silver is 34 Credits
- glob prok Gold is 57800 Credits
- pish pish Iron is 3910 Credits
- how much is pish tegj glob glob ?
- how many Credits is glob prok Silver ?
- how many Credits is glob prok Gold ?
- how many Credits is glob prok Iron ?
- how much wood could a woodchuck chuck if a woodchuck could chuck wood ?

Test Output:
- pish tegj glob glob is 42
- glob prok Silver is 68 Credits
- glob prok Gold is 57800 Credits
- glob prok Iron is 782 Credits
- Unknown query

### Assumptions

- Values of intergalactic numbers are given in format "*name* is *roman value*"
- Words of input are separated with single space
- Input is case sensitive
- Question mark in queries is separated with a space
- Numerical queries start with "how much is"
- Credits queries start with "how many Credits is"

### Build process
- Install python 3
- Open terminal package folder
- Install package using command: 
    ```bash
    pip install -e .
    ```