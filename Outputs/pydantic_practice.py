# # PYDANTIC COMPLETE PRACTICE FILE

# """
# PYDANTIC COMPLETE PRACTICE FILE

# Topics Covered:

# 1. BaseModel
# 2. Type Conversion
# 3. Validation Errors
# 4. model_dump()
# 5. model_dump_json()
# 6. Default Values
# 7. Optional Fields
# 8. Field Constraints
# 9. Literal
# 10. Nested Models
# 11. List of Models
# 12. Field Descriptions
# 13. Field Validators
# 14. Data Transformation
# 15. LangChain Structured Output Schemas

# Useful For:
# - FastAPI
# - LangChain
# - OpenAI Structured Outputs
# - Data Validation
# - API Development
# """

from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal


# # ============================================================
# # 1. BASIC BASEMODEL
# # ============================================================

class User(BaseModel):
    name: str
    age: int


user = User(
    name="Bisakh",
    age=21
)

print(user)


# # ============================================================
# # 2. AUTOMATIC TYPE CONVERSION
# # ============================================================

# class UserConversion(BaseModel):
#     name: str
#     age: int


# user_conversion = UserConversion(
#     name="Bisakh",
#     age="21"
# )

# print(user_conversion)
# print(type(user_conversion.age))


# # ============================================================
# # 3. VALIDATION ERROR EXAMPLE
# # ============================================================

# class UserValidation(BaseModel):
#     name: str
#     age: int


# try:
#     UserValidation(
#         name="Bisakh",
#         age="twenty one"
#     )
# except Exception as e:
#     print(e)


# # ============================================================
# # 4. MODEL_DUMP()
# # ============================================================

# print(user.model_dump())


# # ============================================================
# # 5. MODEL_DUMP_JSON()
# # ============================================================

# print(user.model_dump_json())


# # ============================================================
# # 6. DEFAULT VALUES
# # ============================================================

# class UserDefault(BaseModel):
#     name: str
#     country: str = "India"


# user_default = UserDefault(
#     name="Bisakh"
# )

# print(user_default)


# # ============================================================
# # 7. OPTIONAL FIELDS
# # ============================================================

# class UserOptional(BaseModel):
#     name: str
#     email: Optional[str] = None


# user1 = UserOptional(name="Bisakh")

# user2 = UserOptional(
#     name="Bisakh",
#     email="bisakh@gmail.com"
# )

# user3 = UserOptional(
#     name="Bisakh",
#     email=None
# )

# print(user1)
# print(user2)
# print(user3)


# # ============================================================
# # 8. FIELD CONSTRAINTS
# # ============================================================

# class Product(BaseModel):
#     price: float = Field(
#         gt=0,
#         lt=10000
#     )


# product = Product(price=999)

# print(product)


# # ============================================================
# # 9. LITERAL
# # ============================================================

# class ReviewLiteral(BaseModel):
#     sentiment: Literal[
#         "positive",
#         "negative",
#         "neutral"
#     ]


# review_literal = ReviewLiteral(
#     sentiment="positive"
# )

# print(review_literal)


# # ============================================================
# # 10. FIELD DESCRIPTION
# # ============================================================

# class ReviewDescription(BaseModel):
#     summary: str = Field(
#         description="Short review summary"
#     )


# review_description = ReviewDescription(
#     summary="Amazing phone"
# )

# print(review_description)


# # ============================================================
# # 11. NESTED MODELS
# # ============================================================

# class Address(BaseModel):
#     city: str
#     pincode: int


# class UserAddress(BaseModel):
#     name: str
#     address: Address


# user_address = UserAddress(
#     name="Bisakh",
#     address={
#         "city": "Kolkata",
#         "pincode": 700001
#     }
# )

# print(user_address)


# # ============================================================
# # 12. LIST OF MODELS
# # ============================================================

# class Skill(BaseModel):
#     name: str


# class Resume(BaseModel):
#     candidate_name: str
#     skills: list[Skill]


# resume = Resume(
#     candidate_name="Bisakh",
#     skills=[
#         {"name": "Python"},
#         {"name": "LangChain"},
#         {"name": "Docker"}
#     ]
# )

# print(resume)


# # ============================================================
# # 13. SIMPLE VALIDATOR
# # ============================================================

# class UserValidator(BaseModel):
#     username: str

#     @field_validator("username")
#     @classmethod
#     def validate_username(cls, value):

#         if len(value) < 3:
#             raise ValueError(
#                 "Username too short"
#             )

#         return value


# user_validator = UserValidator(
#     username="bisakh"
# )

# print(user_validator)


# # ============================================================
# # 14. VALIDATOR TRANSFORMATION
# # ============================================================

# class UserTransform(BaseModel):
#     username: str

#     @field_validator("username")
#     @classmethod
#     def normalize_username(cls, value):
#         return value.lower()


# user_transform = UserTransform(
#     username="BISAKH"
# )

# print(user_transform.username)


# # ============================================================
# # 15. STRIP + LOWER + VALIDATE
# # ============================================================

# class UserClean(BaseModel):
#     username: str

#     @field_validator("username")
#     @classmethod
#     def clean_username(cls, value):

#         value = value.strip()

#         if len(value) < 3:
#             raise ValueError(
#                 "Username too short"
#             )

#         return value.lower()


# user_clean = UserClean(
#     username="  BISAKH  "
# )

# print(user_clean.username)


# # ============================================================
# # 16. EMAIL VALIDATOR
# # ============================================================

# class EmailUser(BaseModel):
#     email: str

#     @field_validator("email")
#     @classmethod
#     def validate_email(cls, value):

#         if "@" not in value:
#             raise ValueError(
#                 "Invalid email"
#             )

#         return value


# email_user = EmailUser(
#     email="bisakh@gmail.com"
# )

# print(email_user)


# # ============================================================
# # 17. RESUME ANALYZER (LANGCHAIN STYLE)
# # ============================================================

# class ResumeAnalysis(BaseModel):

#     candidate_name: str = Field(
#         description="Full name of candidate"
#     )

#     skills: list[str] = Field(
#         description="List all skills"
#     )

#     years_of_experience: int = Field(
#         ge=0,
#         description="Total years of experience"
#     )

#     recommendation: Literal[
#         "hire",
#         "reject"
#     ]


# resume_analysis = ResumeAnalysis(
#     candidate_name="Bisakh",
#     skills=[
#         "Python",
#         "LangChain",
#         "Docker"
#     ],
#     years_of_experience=2,
#     recommendation="hire"
# )

# print(resume_analysis)


# # ============================================================
# # 18. PRODUCT REVIEW ANALYZER
# # ============================================================

# class ProductReview(BaseModel):

#     product_name: str = Field(
#         description="Product name"
#     )

#     rating: int = Field(
#         ge=1,
#         le=5,
#         description="Rating from 1 to 5"
#     )

#     sentiment: Literal[
#         "positive",
#         "negative",
#         "neutral"
#     ]

#     summary: str = Field(
#         description="Review summary"
#     )


# product_review = ProductReview(
#     product_name="Samsung S24 Ultra",
#     rating=5,
#     sentiment="positive",
#     summary="Excellent flagship phone"
# )

# print(product_review)


# # ============================================================
# # 19. SENTIMENT ANALYSIS SCHEMA
# # ============================================================

# class SentimentAnalysis(BaseModel):

#     summary: str = Field(
#         description="Brief summary"
#     )

#     sentiment: Literal[
#         "positive",
#         "negative",
#         "neutral"
#     ]

#     confidence: float = Field(
#         ge=0,
#         le=1
#     )


# sentiment_result = SentimentAnalysis(
#     summary="Excellent phone",
#     sentiment="positive",
#     confidence=0.95
# )

# print(sentiment_result)


# # ============================================================
# # 20. LANGCHAIN STRUCTURED OUTPUT SCHEMA
# # ============================================================

# class Review(BaseModel):

#     summary: str = Field(
#         description="Short summary of review"
#     )

#     sentiment: Literal[
#         "positive",
#         "negative",
#         "neutral"
#     ]

#     rating: int = Field(
#         ge=1,
#         le=5,
#         description="Rating between 1 and 5"
#     )


# """
# Usage:

# structured_model = model.with_structured_output(Review)
# result = structured_model.invoke(review_text)
# """


# # ============================================================
# # INTERVIEW REVISION NOTES
# # ============================================================

# """
# 1. BaseModel creates validated objects.

# 2. model_dump()
#    -> Python dictionary

# 3. model_dump_json()
#    -> JSON string

# 4. Field()
#    -> Constraints + metadata

# 5. description=
#    -> Used by LangChain/OpenAI

# 6. gt
#    -> greater than

# 7. ge
#    -> greater than or equal

# 8. lt
#    -> less than

# 9. le
#    -> less than or equal

# 10. Literal
#     -> Restricts allowed values

# 11. field_validator
#     -> Validate or transform data

# 12. Pydantic automatically:
#     - converts types
#     - validates values
#     - parses nested models

# 13. TypedDict
#     -> static typing only

# 14. Pydantic
#     -> runtime validation

# 15. Production LangChain
#     -> Prefer Pydantic
# """