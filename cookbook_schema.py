"""
Schemas for TA3 data output from TA4
"""
from pydantic import BaseModel, Field
from typing import Optional, TypeVar

Polygon = TypeVar("Polygon")
Line = TypeVar("Line")
Point = TypeVar("Point")
WKT = TypeVar("WKT", bound=str)


class ReferenceModel(BaseModel):
    name: str = Field(..., description="The name of the reference")
    description: str = Field(..., description="A description of the reference model")
    url: Optional[str] = Field(None, description="URL for reference")
    citation: Optional[list[str]] = Field(None, description="citations")


class CaseStudy(BaseModel):
    name: str = Field(..., description="The name of the case study")
    description: str = Field(..., description="A description of the case study")
    reference: Optional[ReferenceModel] = Field(..., description="Reference for the case study")


class Audience(BaseModel):
    name: str = Field(..., description="Name of the audience")


class ProcessingMethod(BaseModel):
    name: str = Field(..., description="Name of the processing method")
    reference: list[ReferenceModel] = Field(..., description="The reference model for the science input")


class DataSource(BaseModel):
    name: str = Field(..., description="The name of the data source")
    platform_type: str = Field(..., description="Platform type (satellite, ground sensor, etc.")
    references: list[ReferenceModel] = Field(..., description="References describing the source")


class DataProduct(BaseModel):
    name: str = Field(..., description="The name of the science input")
    description: str = Field(..., description="A description of the science input")
    science_input: Optional[str] = Field(None, description="The name of the science input")
    reference: list[ReferenceModel] = Field(..., description="The reference model for the science input")
    data_source: list[DataSource] = Field(..., description="Where this data comes from")
    processing_methods: list[ProcessingMethod] = Field(..., description="How to process data inputs")


class EcoContext(BaseModel):
    region: str = Field(..., description="Region answer applies to")
    ecosystem: str = Field(..., description="Ecosystem answer applies to")
    weather: str = Field(..., description="Weather answer applies to")


class Answer(BaseModel):
    eco_context: EcoContext = Field(..., description="Ecoregion answer applies to")
    case_studies: CaseStudy = Field(..., description="The case studies to which the question applies")
    data_inputs: list[DataProduct] = Field(..., description="The science inputs to which the question applies")
    processing_methods: list[ProcessingMethod] = Field(..., description="How to process data inputs")


class Question(BaseModel):
    question: str = Field(..., description="The question to be answered")
    answer: list[Answer] = Field(..., description="The answer to the question")
    context: str = Field(..., description="Context for question, e.x. land management, research")





