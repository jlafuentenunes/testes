from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from typing import List
import os
import shutil
from processing import process_invoice_file

app = FastAPI(title="Invoice Processing System")

@app.get("/")
async def root():
    return {"message": "API Invoice Processing está a funcionar. Usa /docs para a interface."}

@app.post("/upload-invoices/")
async def upload_invoices(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded")

    save_dir = "/Users/jlafuente/PROJETOS/testes"
    os.makedirs(save_dir, exist_ok=True)
    saved_files = []
    for file in files:
        file_location = os.path.join(save_dir, file.filename)
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
        saved_files.append(file_location)

    csv_stream = process_invoice_file(saved_files[0])

    headers = {"Content-Disposition": f"attachment; filename=processed_invoices.csv"}
    return StreamingResponse(csv_stream, media_type="text/csv", headers=headers)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)