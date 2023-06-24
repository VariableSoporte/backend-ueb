from pydantic import BaseModel


class ListDocumentBase(BaseModel):
    pass


class ListDocumentCreate(ListDocumentBase):
    list_id: int
    document: str


class ListDocument(ListDocumentBase):
    id: int
    # list_id: int
    document: str

    class Config:
        orm_mode = True
