from typing import Optional, Dict, Any

from fastapi import APIRouter, HTTPException, status, Query

from app.models.professor import Professor
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.get("/professors/{p_uni}", tags=["professors"], response_model=Professor)
async def get_professor(p_uni: str) -> Professor:
    res = ServiceFactory.get_service("ProfessorResource")
    result = res.get_by_key(p_uni)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Professor {p_uni} not found")
    return result


@router.post("/professors", tags=["professors"], response_model=Professor, status_code=status.HTTP_201_CREATED)
async def create_professor(professor: Professor) -> Professor:
    res = ServiceFactory.get_service("ProfessorResource")
    result = res.insert_by_fields(professor.first_name, professor.last_name)
    return result


@router.patch("/professors/{p_uni}", tags=["professors"], response_model=Professor)
async def update_professor(p_uni: str, professor: Professor) -> Professor:
    res = ServiceFactory.get_service("ProfessorResource")
    if res.get_by_key(p_uni) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Professor {p_uni} not found")
    res.update_by_fields(p_uni, "first_name", professor.first_name)
    result = res.update_by_fields(p_uni, "last_name", professor.last_name)
    return result


@router.delete("/professors/{p_uni}", tags=["professors"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_professor(p_uni: str):
    res = ServiceFactory.get_service("ProfessorResource")
    if res.get_by_key(p_uni) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Professor {p_uni} not found")
    res.delete_by_key(p_uni)
    return None


@router.get("/professors", tags=["professors"], response_model=Dict[str, Any])
async def get_all_professors(
        page: int = Query(1, ge=1),
        size: int = Query(10, ge=1, le=100),
        professor_id: Optional[str] = None
) -> Dict[str, Any]:
    res = ServiceFactory.get_service("ProfessorResource")
    result = res.get_all_professors(page, size, professor_id)
    return result
