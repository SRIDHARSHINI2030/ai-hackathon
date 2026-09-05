from io import BytesIO

from pypdf import PdfReader


def clean_material_text(text: str) -> str:
    cleaned_text = " ".join(text.split())
    return cleaned_text


def extract_pdf_text(file_bytes: bytes) -> str:
    reader = PdfReader(BytesIO(file_bytes))

    pages_text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            pages_text.append(page_text)

    return clean_material_text("\n".join(pages_text))