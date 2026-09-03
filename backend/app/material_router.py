from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/upload-material")
async def upload_material(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Learning material received successfully",
    }