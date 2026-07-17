
PERSON_INFO = [
    {'name': 'John', 'age': 30, 'interest': ['Python']},
    {'name': 'Jack', 'age': 45, 'interest': ['C++', 'Python', 'Machine Learning']},
    {'name': 'Ann', 'age': 28, 'interest': ['Deep Learning', 'LLM']},
    {'name': 'Bob', 'age': 25},
    {'name': 'Chris', 'age': 20, 'interest': ['LLM']},
    {'name': 'David', 'age': 36}
]


def get_unique_interest_count():
    """Return the number of unique values of interest."""

    interest_set = set()

    for person in PERSON_INFO:
        interest = person.get('interest', None)
        if interest is not None:
            interest_set = interest_set.union(interest)

    print(interest_set)
    return len(interest_set)


def get_unique_interest_count_assignment_expression():
    """Return the number of unique values of interest.
       used assignment expression (for Python 3.8+)
    """

    interest_set = set()

    for person in PERSON_INFO:
        if (interest := person.get('interest')) is not None:
            interest_set = interest_set.union(interest)

    print(interest_set)
    return len(interest_set)


def get_unique_interest_count_assignment_expression_set_comprehension():
    """Return the number of unique values of interest.
       used assignment expression (for Python 3.8+) + set comprehension
    """

    interest_set = {  # used set comprehension
        item
        for person in PERSON_INFO
        if (interest := person.get('interest')) is not None
        for item in interest
    }

    print(interest_set)
    return len(interest_set)


if __name__ == '__main__':
    print(get_unique_interest_count())
    print(get_unique_interest_count_assignment_expression())
    print(get_unique_interest_count_assignment_expression_set_comprehension())

