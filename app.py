import base64
import os
import shutil
from pathlib import Path
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from ultralytics import YOLO

app = FastAPI()

templates = Jinja2Templates(directory="templates")

uploads_folder = Path("uploads")

# ✅ Load model once
model = None

@app.on_event("startup")
def load_model():
    global model
    model = YOLO("yolov8n.pt")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/detect/")
async def detect_objects(request: Request, image: UploadFile = File(...)):

    if not image:
        return JSONResponse(status_code=400, content={"error": "No image uploaded"})

    uploads_folder.mkdir(parents=True, exist_ok=True)
    file_path = uploads_folder / image.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # ✅ Run detection
    results = model(str(file_path))

    output = []

    for r in results:
        for box, value, prob in zip(r.boxes.xywh, r.boxes.cls, r.boxes.conf):
            detected_label = r.names[int(value.item())]
            x, y, w, h = box
            confidence = round(prob.item(), 2)

            output.append({
                "label": detected_label,
                "x": int(x),
                "y": int(y),
                "width": int(w),
                "height": int(h),
                "confidence": confidence
            })

    # Encode image
    with open(file_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    return {
        "image": encoded_image,
        "objects": output,
        "count": len(output)
    }