from pydantic import BaseModel


class DocumentWriteRequest(BaseModel):
    files: list[str]
    filters: list[str]
    google_doc_url: str
