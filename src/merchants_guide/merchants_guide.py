import roman


def destructure_input(input):
    """
    Destructures input and returns lists of numerical assignments,
    credit assignments and queries

    Keyword arguments:
    input -- input text with new line separators
    """
    num_assignment = [item.strip() for item in input.split("\n") if "Credits" not in item and "?" not in item]
    credit_assignment = [item.strip() for item in input.split("\n") if "Credits" in item and "?" not in item]
    queries = [item.strip() for item in input.split("\n") if "?" in item]
    return num_assignment, credit_assignment, queries


def get_roman_values(num_assignment):
    """
    Forms a dictionary of units and their roman values

    Keyword arguments:
    num_assignment -- list of numerical assignment strings
    """
    pass


def convert_str_to_decimal(str, roman_values):
    """
    Converts an intergalactic number into decimal system

    Keyword arguments:
    str -- intergalactic number as a string
    roman_values -- dictionary of units and their roman values
    """
    pass


def get_credit_values(credit_assignment, roman_values):
    """
    Forms a dictionary of materials and their values

    Keyword arguments:
    roman_values -- dictionary of units and their roman values
    credit_assignment -- list of credit assignment strings
    """
    pass


def calculate_query_results(queries, credit_values, roman_values):
    """
    Calculates values for query results

    Keyword arguments:
    queries -- list of query strings
    credit_values -- dictionary of materials and their credit values
    roman_values -- dictionary of units and their roman values
    """
    pass
