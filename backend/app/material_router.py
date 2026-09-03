from fastapi import APIRouter, UploadFile, File
from app.material_service import extract_pdf_text

router = APIRouter()


@router.post("/upload-material")
async def upload_material(file: UploadFile = File(...)):
    file_bytes = await file.read()
    text = extract_pdf_text(file_bytes)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "text": text,
        "character_count": len(text),
        "preview": text[:500],
        "message": "PDF text extracted successfully",
    }