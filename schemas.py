from pydantic import BaseModel

class KpaDataCreate(BaseModel):
    name: str
    phone: str

class KpaDataOut(KpaDataCreate):
    id: int

    class Config:
        orm_mode = True
