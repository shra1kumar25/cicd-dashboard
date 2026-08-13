from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate,
)
from app.services.project_service import (
    create_project,
    delete_project,
    get_project,
    get_projects,
    update_project,
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_project_endpoint(
    project_data: ProjectCreate,
    db: Session = Depends(get_db),
):
    return create_project(db, project_data)


@router.get(
    "",
    response_model=list[ProjectResponse],
)
def list_projects(
    db: Session = Depends(get_db),
):
    return get_projects(db)


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
def get_project_endpoint(
    project_id: int,
    db: Session = Depends(get_db),
):
    project = get_project(db, project_id)

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    return project


@router.put(
    "/{project_id}",
    response_model=ProjectResponse,
)
def update_project_endpoint(
    project_id: int,
    project_data: ProjectUpdate,
    db: Session = Depends(get_db),
):
    project = get_project(db, project_id)

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    return update_project(
        db,
        project,
        project_data,
    )


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_project_endpoint(
    project_id: int,
    db: Session = Depends(get_db),
):
    project = get_project(db, project_id)

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    delete_project(db, project)
