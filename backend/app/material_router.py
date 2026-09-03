from fastapi import APIRouter, UploadFile, File

from app.material_service import extract_pdf_text
from app.material_pipeline import process_material


router = APIRouter()


@router.post("/upload-material")
async def upload_material(file: UploadFile = File(...)):
    file_bytes = await file.read()

    text = extract_pdf_text(file_bytes)

    processing_result = process_material(text)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "character_count": len(text),
        "preview": text[:500],
        "chunk_count": processing_result["chunk_count"],
        "message": "Material uploaded and processed successfully",
    }