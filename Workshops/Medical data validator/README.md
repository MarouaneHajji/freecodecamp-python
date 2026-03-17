# Medical Records Validator

A Python script that validates the structure and content of a medical records dataset.

## What It Does

Given a list of patient records, the validator checks two things:

1. **Structure** — is the data shaped correctly? (list of dicts, correct keys)
2. **Content** — are the values in each field valid? (correct types, formats, ranges)

Any issue found is printed to the console with the position and field that failed.

---

## How to Run

```bash
python medical_validator.py
```

---

## Expected Data Format

The dataset must be a `list` or `tuple` of dictionaries. Each dictionary must contain exactly these keys:

| Key | Expected Format |
|---|---|
| `patient_id` | String matching `P` or `p` followed by digits — e.g. `P1001` |
| `age` | Integer, must be 18 or older |
| `gender` | String, either `male` or `female` (case-insensitive) |
| `diagnosis` | String, or `None` if no diagnosis |
| `medications` | Non-empty list of strings |
| `last_visit_id` | String matching `V` or `v` followed by digits — e.g. `V2301` |

---

## Functions

### `find_invalid_records(...)`

Takes the six fields of a patient record as individual arguments and returns a list of field names that failed validation.

```python
find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id)
# Returns: ['age', 'gender']  ← example of two failing fields
```

### `validate(data)`

Validates the full dataset. Checks structure first, then delegates field-level checks to `find_invalid_records`. Returns `True` if everything is valid, `False` if any error was found.

---

## Example Output

All valid:
```
Valid format.
```

With invalid records:
```
Unexpected format 'age: 15' at position 2.
Unexpected format 'gender: unknown' at position 2.
```

---

## Dependencies

- Python 3
- `re` module (standard library — no install needed)