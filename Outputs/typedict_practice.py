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