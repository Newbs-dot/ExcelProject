from pydantic import BaseModel


class DocumentWriteRequest(BaseModel):
    google_doc_url: str
    filters: list[str]
    files: list[bytes]
