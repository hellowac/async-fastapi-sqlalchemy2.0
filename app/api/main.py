from fastapi import APIRouter

from .notebooks.v1_views import router as v1_notebooks_router
from .notebooks.v2_views import router as v2_notebooks_router
from .notes.v1_views import router as v1_notes_router
from .notes.v2_views import router as v2_notes_router

# v1
v1_router = APIRouter(tags=["笔记和备注v1"])  # prefix="/v1"
v1_router.include_router(v1_notes_router)
v1_router.include_router(v1_notebooks_router)

# v2
v2_router = APIRouter(tags=["笔记和备注v2"])  # prefix="/v2"
v2_router.include_router(v2_notes_router)
v2_router.include_router(v2_notebooks_router)
