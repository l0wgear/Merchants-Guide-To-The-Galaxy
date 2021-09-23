import re
import roman


def destructure_input(input):
    """
    Destructures input list and returns lists of numerical assignments,
    credit assignments and queries

    Keyword arguments:
    input -- input text with new line separators
    """
    num_assignment = [item.strip() for item in input if "Credits" not in item and "?" not in item]
    credit_assignment = [item.strip() for item in input if "Credits" in item and "?" not in item]
    queries = [item.strip() for item in input if "?" in item]
    return num_assignment, credit_assignment, queries


def get_roman_values(num_assignment):
    """
    Forms a dictionary of units and their roman values

    Keyword arguments:
    num_assignment -- list of numerical assignment strings
    """
    return {item.split(' ')[0]:item.split(' ')[2] for item in num_assignment}


def convert_str_to_decimal(str, roman_values):
    """
    Converts an intergalactic number into decimal system

    Keyword arguments:
    str -- intergalactic number as a string
    roman_values -- dictionary of units and their roman values
    """
    try:
        roman_numeral = "".join([roman_values[item] for item in str.split(' ')])
        return roman.fromRoman(roman_numeral) 
    except roman.InvalidRomanNumeralError:
        raise roman.InvalidRomanNumeralError("Invalid numeral")
    except KeyError:
        raise KeyError("Insufficient numerical data")


def get_credit_values(credit_assignment, roman_values):
    """
    Forms a dictionary of materials and their values

    Keyword arguments:
    roman_values -- dictionary of units and their roman values
    credit_assignment -- list of credit assignment strings
    """
    credit_values = {}
    for item in credit_assignment:
        word_list = item.split(' ')
        key = word_list[0:word_list.index('is')]
        decimal_num = convert_str_to_decimal(" ".join(key[0:-1]), roman_values)
        material = key[-1]
        value = int(word_list[word_list.index('is') + 1])
        material_price = value / decimal_num
        credit_values[material] = material_price
    return credit_values


def calculate_query_results(queries, credit_values, roman_values):
    """
    Calculates values for query results

    Keyword arguments:
    queries -- list of query strings
    credit_values -- dictionary of materials and their credit values
    roman_values -- dictionary of units and their roman values
    """
    results = []
    for query in queries:
        if ("how much is " in query):
            try:
                num_value = convert_str_to_decimal(query[12:-2], roman_values)
                results.append(f"{query[12:-2]} is {num_value}")
            except (roman.InvalidRomanNumeralError, KeyError) as e:
                results.append(e)
        elif ("how many Credits is " in query):
            try:
                split_list = query[20:-2].split(' ')
                intergalactic_num = " ".join(split_list[0:-1])
                num_value = convert_str_to_decimal(intergalactic_num, roman_values)
                material = split_list[-1]
                credit_value = credit_values[material]
                price = num_value * credit_value
                results.append(f"{query[20:-2]} is {price} Credits")
            except roman.InvalidRomanNumeralError as e:
                results.append("Invalid numeral")
            except KeyError:
                results.append("Insufficient data")
        else:
            results.append("Unknown query")
    return results

def output_results(results):
    for result in results:
        print(result)

def main():
    """
    Reads input from a file and writes conversion results to console
    """
    with open("input.txt") as input:
        num_assignment, credit_assignment, queries = destructure_input(input.readlines())
    roman_values = get_roman_values(num_assignment)
    credit_values = get_credit_values(credit_assignment, roman_values)
    query_results = calculate_query_results(queries, credit_values, roman_values)
    output_results(query_results)


if (__name__ == "__main__"):
    main()