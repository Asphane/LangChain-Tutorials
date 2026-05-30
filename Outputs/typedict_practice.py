# """
# TypedDict Complete Practice File
# Author: Bisakh

# Purpose:
# --------
# Learn and practice Python TypedDict concepts.

# Topics Covered:
# 1. Basic TypedDict
# 2. Required Fields
# 3. Optional Fields using total=False
# 4. Optional Fields using NotRequired
# 5. Nested TypedDict
# 6. Lists inside TypedDict
# 7. TypedDict Inheritance
# 8. Real API Response Modelling
# """

from typing import TypedDict, NotRequired


# # ============================================================
# # 1. BASIC TYPEDICT
# # ============================================================

class Student(TypedDict):
    """
    All fields are required by default.
    """
    name: str
    age: int
    cgpa: float


student: Student = {
    "name": "Bisakh",
    "age": 21,
    "cgpa": 8.5
}

print("Basic Student:")
print(student)
print()


# # ============================================================
# # 2. OPTIONAL FIELDS USING total=False
# # ============================================================

# class Employee(TypedDict, total=False):
#     """
#     Every field is optional.
#     """
#     name: str
#     salary: float
#     experience: int


# emp1: Employee = {}

# emp2: Employee = {
#     "name": "Rahul"
# }

# emp3: Employee = {
#     "salary": 50000.0,
#     "experience": 3
# }

# print("Employee Examples:")
# print(emp1)
# print(emp2)
# print(emp3)
# print()


# # ============================================================
# # 3. OPTIONAL FIELDS USING NotRequired
# # ============================================================

# class User(TypedDict):
#     """
#     Only specific fields are optional.
#     """
#     id: int
#     name: str
#     email: NotRequired[str]
#     is_active: NotRequired[bool]


# user1: User = {
#     "id": 1,
#     "name": "Bisakh"
# }

# user2: User = {
#     "id": 2,
#     "name": "Rahul",
#     "email": "rahul@gmail.com",
#     "is_active": True
# }

# print("User Examples:")
# print(user1)
# print(user2)
# print()


# # ============================================================
# # 4. NESTED TYPEDICT
# # ============================================================

# class Address(TypedDict):
#     city: str
#     pincode: int


# class StudentProfile(TypedDict):
#     name: str
#     address: Address


# profile: StudentProfile = {
#     "name": "Bisakh",
#     "address": {
#         "city": "Kolkata",
#         "pincode": 700001
#     }
# }

# print("Nested TypedDict:")
# print(profile)
# print()


# # ============================================================
# # 5. LISTS INSIDE TYPEDICT
# # ============================================================

# class Marksheet(TypedDict):
#     student_name: str
#     marks: list[int]


# result: Marksheet = {
#     "student_name": "Bisakh",
#     "marks": [90, 88, 95]
# }

# print("Marksheet:")
# print(result)
# print()


# # ============================================================
# # 6. TYPEDICT INHERITANCE
# # ============================================================

# class Person(TypedDict):
#     name: str


# class StudentRecord(Person):
#     """
#     Inherits 'name' from Person
#     """
#     roll: int


# record: StudentRecord = {
#     "name": "Bisakh",
#     "roll": 101
# }

# print("Inheritance Example:")
# print(record)
# print()


# # ============================================================
# # 7. WEATHER API RESPONSE
# # ============================================================

# class WeatherResponse(TypedDict):
#     """
#     Example of modelling an API response.
#     """
#     city: str
#     temperature: float
#     humidity: int
#     rainfall: NotRequired[float]


# weather1: WeatherResponse = {
#     "city": "Kolkata",
#     "temperature": 34.5,
#     "humidity": 78
# }

# weather2: WeatherResponse = {
#     "city": "Mumbai",
#     "temperature": 31.2,
#     "humidity": 82,
#     "rainfall": 12.4
# }

# print("Weather Response:")
# print(weather1)
# print(weather2)
# print()


# # ============================================================
# # 8. GITHUB USER API RESPONSE
# # ============================================================

# class GitHubUser(TypedDict):
#     id: int
#     username: str
#     followers: int
#     following: int
#     bio: NotRequired[str]


# github_user: GitHubUser = {
#     "id": 101,
#     "username": "bisakh",
#     "followers": 120,
#     "following": 50
# }

# print("GitHub User:")
# print(github_user)
# print()


# # ============================================================
# # 9. E-COMMERCE PRODUCT RESPONSE
# # ============================================================

# class Product(TypedDict):
#     product_id: int
#     name: str
#     price: float
#     stock: int
#     discount: NotRequired[float]


# product: Product = {
#     "product_id": 1,
#     "name": "Laptop",
#     "price": 65000.0,
#     "stock": 10
# }

# print("Product:")
# print(product)
# print()


# # ============================================================
# # 10. KEY TAKEAWAYS
# # ============================================================

# ============================================================
# 11. LANGCHAIN STRUCTURED OUTPUT SCHEMAS
# ============================================================

from typing import TypedDict, Annotated, NotRequired, Literal


class ResumeAnalysis(TypedDict):
    """
    Schema for extracting information from resumes.
    Useful with:
        model.with_structured_output(ResumeAnalysis)
    """

    candidate_name: Annotated[
        str,
        "Full name of the candidate"
    ]

    skills: Annotated[
        list[str],
        "List all technical and non-technical skills mentioned in the resume"
    ]

    years_of_experience: Annotated[
        int,
        "Total years of professional experience"
    ]

    email: Annotated[
        NotRequired[str],
        "Candidate email address if available"
    ]

    recommendation: Annotated[
        Literal["hire", "reject"],
        "Final hiring recommendation"
    ]


sample_resume_output: ResumeAnalysis = {
    "candidate_name": "Bisakh Patra",
    "skills": [
        "Python",
        "LangChain",
        "Machine Learning",
        "Docker"
    ],
    "years_of_experience": 2,
    "recommendation": "hire"
}

print("Resume Analysis:")
print(sample_resume_output)
print()


# ============================================================
# 12. PRODUCT REVIEW ANALYZER
# ============================================================

class ProductReview(TypedDict):

    product_name: Annotated[
        str,
        "Name of the reviewed product"
    ]

    rating: Annotated[
        int,
        "Rating between 1 and 5"
    ]

    sentiment: Annotated[
        Literal["positive", "negative"],
        "Overall sentiment of the review"
    ]

    reviewer: Annotated[
        NotRequired[str],
        "Name of reviewer if available"
    ]


sample_review: ProductReview = {
    "product_name": "Samsung Galaxy S24 Ultra",
    "rating": 5,
    "sentiment": "positive",
    "reviewer": "Nitish Singh"
}

print("Product Review:")
print(sample_review)
print()


# ============================================================
# 13. MOVIE REVIEW ANALYZER
# ============================================================

class MovieReview(TypedDict):

    title: Annotated[
        str,
        "Movie title"
    ]

    rating: Annotated[
        int,
        "Rating from 1 to 10"
    ]

    sentiment: Annotated[
        Literal["positive", "negative"],
        "Overall movie sentiment"
    ]

    reviewer: Annotated[
        NotRequired[str],
        "Reviewer name"
    ]


movie_review: MovieReview = {
    "title": "Interstellar",
    "rating": 9,
    "sentiment": "positive",
    "reviewer": "Bisakh"
}

print("Movie Review:")
print(movie_review)
print()


# ============================================================
# 14. LANGCHAIN REVIEW EXTRACTION
# ============================================================

class Review(TypedDict):

    key_themes: Annotated[
        list[str],
        "All key themes discussed in the review"
    ]

    summary: Annotated[
        str,
        "Brief summary of the review"
    ]

    sentiment: Annotated[
        Literal["positive", "negative", "neutral"],
        "Overall sentiment"
    ]

    pros: Annotated[
        NotRequired[list[str]],
        "Advantages mentioned in review"
    ]

    cons: Annotated[
        NotRequired[list[str]],
        "Disadvantages mentioned in review"
    ]

    name: Annotated[
        NotRequired[str],
        "Reviewer name"
    ]


sample_extraction: Review = {
    "key_themes": [
        "Camera",
        "Battery",
        "Performance"
    ],
    "summary": "Excellent flagship phone with strong performance.",
    "sentiment": "positive",
    "pros": [
        "Great camera",
        "Long battery life"
    ],
    "name": "Nitish Singh"
}

print("Structured Review:")
print(sample_extraction)
print()


# ============================================================
# 15. COMMON INTERVIEW NOTES
# ============================================================

"""
TypedDict Interview Revision

1. TypedDict creates type-safe dictionaries.

2. Annotated[T, description]
   -> Type = T
   -> Description used by LangChain/LLMs

3. Optional[str]
   -> Key required
   -> Value can be str or None

4. NotRequired[str]
   -> Key may be absent

5. Literal["a", "b"]
   -> Restricts allowed values

6. total=False
   -> Makes ALL keys optional

7. TypedDict supports:
   - Nesting
   - Inheritance
   - Lists
   - Optional fields
   - Structured LLM outputs

8. Common LangChain Usage:

   structured_model =
       model.with_structured_output(MySchema)

9. Most common use cases:
   - Resume Extraction
   - Review Analysis
   - Invoice Extraction
   - User Profiles
   - API Responses
   - Agent Outputs

10. TypedDict is for static typing.
    At runtime, it behaves like a normal dict.
"""

# """
# 1. TypedDict creates type-safe dictionaries.
# 2. All fields are required by default.
# 3. total=False makes all fields optional.
# 4. NotRequired makes selected fields optional.
# 5. TypedDict supports nesting.
# 6. TypedDict supports inheritance.
# 7. Useful for APIs, JSON responses, configs,
#    LangChain projects and backend development.
# """