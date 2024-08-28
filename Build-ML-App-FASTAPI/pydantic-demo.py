from pydantic import BaseModel, field_validator, constr, EmailStr, ValidationError
from typing import List

class Instructor(BaseModel):
    name: str
    fullname: constr(min_length=3, max_length=20)
    age: int
    course: str
    ratings: List[int] = []
    email: EmailStr = None

    # Custom validator for 'age'
    @field_validator('age', mode='before')
    def validate_age(cls, value):
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Age must be an integer, received: {value}")

    # Custom validator for 'ratings' to validate each element in the list
    @field_validator('ratings', mode='before')
    def validate_ratings(cls, value):
        # Check if 'value' is a list
        if not isinstance(value, list):
            raise TypeError(f"Ratings must be a list, received: {type(value).__name__}")

        # Validate each element in the list
        validated_ratings = []
        for rating in value:
            try:
                validated_ratings.append(int(rating))
            except ValueError:
                raise ValueError(f"Rating must be an integer, received: {rating}")
        return validated_ratings

# Example data
data = {
    "name": "Murthy",
    "fullname": "Murthy Koushik",
    "age": "28",
    "course": "MLOps BootCamp",
    "ratings": [4, 4, "4", "5", 4],
    "email": "test@example.com"
}

invalid_data = {
    "name": "Murthy",
    "fullname": "Mu", # Invalid fullname value
    "age": "aaa",  # Invalid age value
    "course": "MLOps BootCamp",
    "ratings": [4, 4, "bbb", "5", 4], # Invalid rating value
    "email": "aaaaa" # Invalid email value
}

def user_validator(data):
    try:
        user = Instructor(**data)
        print(f"\nFound an Instructor: {user}")
    except ValidationError as e:
        print("\nValidation error with data:", e.json())

# Validate the correct data
user_validator(data)

# Validate the incorrect data
user_validator(invalid_data)