from pydantic import BaseModel, Field


class Post(BaseModel):
    id: int = Field(le = 3)  # Встроенная валидация
    title: str

    # Кастомная валидация
    # @field_validator("id")
    # def check_id_is_less_two(cls, v):
    #     if v > 3:
    #         raise ValueError('id is not less than two')
    #     else:
    #         return v
