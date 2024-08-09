import os
import uvicorn
from pypdf import PdfWriter
from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
from fastapi import HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return {"status_code": 200, "status_message": "OK 200 Response"}

@app.post("/pdfmerger")
async def pdf_merger(files: list[UploadFile] = File(...)):
    try:
        merger = PdfWriter()

        for file in files:
            with open(file.filename, "wb") as f:
                f.write(await file.read())
            merger.append(file.filename)

        output_path = "output.pdf"
        merger.write(output_path)
        merger.close()

        for fname in [fn for fn in os.listdir() if fn.lower().endswith(".pdf") and fn != output_path]:
            os.remove(fname)

        return FileResponse(output_path, media_type='application/pdf', filename=output_path)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=False)
