from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Text-to-3D Demo", version="0.1.0")

class GenRequest(BaseModel):
    prompt: str

@app.get("/status")
def status():
    return {"ok": True, "version": "0.1.0", "model": "Shap-E"}

@app.get("/generate3d")
def generate3d(prompt: str):
    # Stubbed response: in a real service, you'd queue a generation job or return a pre-generated asset
    return {
        "message": "demo only",
        "prompt": prompt,
        "sample_asset": "outputs/asset_0.obj"
    }

# optional: also accept a JSON POST (same stub)
@app.post("/generate3d")
def generate3d_post(req: GenRequest):
    return {
        "message": "demo only",
        "prompt": req.prompt,
        "sample_asset": "outputs/asset_0.obj"
    }

if __name__ == "__main__":
    # Running directly: `python api_demo.py`
    uvicorn.run(app, host="0.0.0.0", port=8000)
