"""
Schemas for TA3 data output from TA4
"""
from pydantic import BaseModel, Field
from typing import Optional, TypeVar

Polygon = TypeVar("Polygon")
Line = TypeVar("Line")
Point = TypeVar("Point")
WKT = TypeVar("WKT", bound=str)


class ProspectivityModel(BaseModel):
    bounds: list[float] = Field(..., description="Bounding box of the tile scheme")
    crs: WKT = Field(
        ...,
        description="Coordinate reference system of the tile scheme",
        # default="EPSG:3857 (Web Mercator)",
    )
    resolution: float = Field(..., description="Resolution of the output prospectivity raster")