"""
Schemas for TA3 data output from TA4
"""
from pydantic import BaseModel, Field
from typing import Optional, TypeVar

Polygon = TypeVar("Polygon")
Line = TypeVar("Line")
Point = TypeVar("Point")
WKT = TypeVar("WKT", bound=str)


class CaseStudy(BaseModel):
    name: str = Field(..., description="The name of the case study")
    description: str = Field(..., description="A description of the case study")
    case_study: Optional[str] = Field(None, description="The name of the case study")


class ScienceInput(BaseModel):
    name: str = Field(..., description="The name of the science input")
    description: str = Field(..., description="A description of the science input")
    science_input: Optional[str] = Field(None, description="The name of the science input")


class QuestionModel(BaseModel):
    question: str = Field(..., description="The question to be answered")
    answer: str = Field(..., description="The answer to the question")
    case_studies: CaseStudy = Field(..., description="The case studies to which the question applies")
    science_inputs: list[ScienceInput] = Field(..., description="The science inputs to which the question applies")


