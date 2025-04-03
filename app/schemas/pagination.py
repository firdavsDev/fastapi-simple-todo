from typing import Generic, TypeVar

from fastapi import Request
from pydantic import BaseModel

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    total: int
    count: int
    next: str
    previous: str
    results: list[T]

    @classmethod
    def create(
        cls, data: list[T], total: int, limit: int, offset: int, request: Request
    ):
        base_url = str(request.url).split("?")[0]  # API URL
        next_offset = offset + limit
        prev_offset = max(offset - limit, 0)

        next_url = (
            f"{base_url}?limit={limit}&offset={next_offset}"
            if next_offset < total
            else None
        )
        prev_url = (
            f"{base_url}?limit={limit}&offset={prev_offset}" if offset > 0 else None
        )

        return cls(
            total=total, count=len(data), next=next_url, previous=prev_url, results=data
        )
