from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProjectCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    description: str | None = None
    repository_url: str | None = None


class ProjectUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=100)
    description: str | None = None
    repository_url: str | None = None
    status: str | None = None


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None
    repository_url: str | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
