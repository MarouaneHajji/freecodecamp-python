import re  # Regular expressions module for pattern matching

# Sample dataset: a list of patient records, each represented as a dictionary
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    },
]


def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    """
    Checks each field of a patient record against its expected format.
    Returns a list of keys that failed their validation constraint.
    """
    constraints = {
        # Must be a string matching pattern: 'P' or 'p' followed by one or more digits
        'patient_id': isinstance(patient_id, str) and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE),

        # Must be an integer and at least 18 (no minors in this system)
        'age': isinstance(age, int) and age >= 18,

        # Must be a string and, when lowercased, equal to 'male' or 'female'
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),

        # Must be a string or None (diagnosis is optional)
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,

        # Must be a non-empty list where every item is a string
        'medications': isinstance(medications, list) and all([isinstance(i, str) for i in medications]),

        # Must be a string matching pattern: 'V' or 'v' followed by one or more digits
        'last_visit_id': isinstance(last_visit_id, str) and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE),
    }

    # Return only the keys whose constraint evaluated to False (i.e. invalid fields)
    return [key for key, value in constraints.items() if not value]


def validate(data):
    """
    Validates the overall structure and content of a medical records dataset.
    Expects a list or tuple of dictionaries, each with the required keys and valid values.
    Returns True if all records are valid, False otherwise.
    """

    # Check that the top-level data is a list or tuple
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False

    is_invalid = False  # Tracks whether any validation error was found

    # The exact set of keys every record must have
    key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

    # Iterate over each item with its index for meaningful error messages
    for index, dictionary in enumerate(data):

        # Each item must be a dictionary
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue  # Skip further checks for this item

        # The dictionary's keys must exactly match the expected key set
        if set(dictionary.keys()) != key_set:
            print(f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.')
            is_invalid = True
            continue  # Skip value checks if the structure is already wrong

        # Unpack the dictionary into the function and get back a list of invalid field names
        invalid_records = find_invalid_records(**dictionary)

        # Report each invalid field with its actual value and position
        for key in invalid_records:
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            is_invalid = True

    if is_invalid:
        return False

    print('Valid format.')
    return True


validate(medical_records)