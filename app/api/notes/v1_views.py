from turtle import title
from fastapi import APIRouter, Depends, Path, Request

from app.models import NoteSchema

from .biz import CreateNote, DeleteNote, ReadAllNote, ReadNote, UpdateNote
from .schema import (
    CreateNoteRequest,
    CreateNoteResponse,
    ReadAllNoteResponse,
    ReadNoteResponse,
    UpdateNoteRequest,
    UpdateNoteResponse,
)

router = APIRouter(prefix="/notes")


@router.post(
    "",
    response_model=CreateNoteResponse,
    summary="创建笔记",
    description="创建新的笔记，主要功能点在：【学习】, 场景：学生端学生上课",
)
async def create(
    request: Request,
    data: CreateNoteRequest,
    use_case: CreateNote = Depends(CreateNote),
) -> NoteSchema:
    return await use_case.execute(data.notebook_id, data.title, data.content)


@router.get(
    "",
    response_model=ReadAllNoteResponse,
    summary="查询所有笔记",
    description="查询所有笔记， 主要在功能点: 【笔记列表】",
)
async def read_all(
    request: Request,
    use_case: ReadAllNote = Depends(ReadAllNote),
) -> ReadAllNoteResponse:
    return ReadAllNoteResponse(notes=[note async for note in use_case.execute()])


@router.get(
    "/{note_id}",
    response_model=ReadNoteResponse,
    summary="查询笔记",
    description="查询笔记详情， 主要在功能点: 【编辑笔记】、【预览笔记】",
)
async def read(
    request: Request,
    note_id: int = Path(..., description=""),
    use_case: ReadNote = Depends(ReadNote),
) -> NoteSchema:
    return await use_case.execute(note_id)


@router.put(
    "/{note_id}",
    response_model=UpdateNoteResponse,
    summary="更新笔记",
    description="更新笔记详情， 主要在功能点: 【更新笔记】",
)
async def update(
    request: Request,
    data: UpdateNoteRequest,
    note_id: int = Path(..., description=""),
    use_case: UpdateNote = Depends(UpdateNote),
) -> NoteSchema:
    return await use_case.execute(note_id, data.notebook_id, data.title, data.content)


@router.delete(
    "/{note_id}",
    status_code=204,
    summary="删除笔记",
    description="删除笔记详情， 主要在功能点: 【删除笔记】",
)
async def delete(
    request: Request,
    note_id: int = Path(..., description=""),
    use_case: DeleteNote = Depends(DeleteNote),
) -> None:
    await use_case.execute(note_id)
