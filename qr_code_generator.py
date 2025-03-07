from fastapi import FastAPI, Query
import qrcode
from io import BytesIO
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/generate_qr")
def generate_qr(data: str = Query("", description="Twitter")):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, format="PNG")
    img_io.seek(0)
    
    return StreamingResponse(img_io, media_type="image/png")

# Para rodar o servidor, execute: uvicorn qr_code_generator:app --reload
