# shap-e-text-to-3d
# Text-to-3D with Shap-E (Game Asset Demo)

This mini-project generates simple 3D meshes from text using OpenAI’s **Shap-E**.
Outputs include an **OBJ** mesh and a small **GIF** preview suitable for quick game-art prototyping.

## What this project does
- Takes a text prompt (e.g., “a low-poly red panda holding a game controller”)
- Runs Shap-E in Google Colab to generate a 3D mesh
- Exports **.OBJ** (plus **.PLY**) and a rotating **preview GIF**

## How to run (Google Colab, free)
1. Open a new Colab notebook.
2. Runtime → Change runtime type → **GPU** → Save.
3. Copy the cells from this README’s linked gist / instructions and run in order:
   - install packages
   - load models
   - generate from your prompt
   - preview GIF
   - export OBJ
4. Download `outputs/asset_0.obj` and `preview_0.gif` from the Colab file sidebar.

> Tip: First run may take a while to download weights.

## Sample outputs
- Prompt: `a low-poly red panda holding a game controller`
- Files:
  - [OBJ file](https://raw.githubusercontent.com/Manha-kabir/shap-e-text-to-3d/refs/heads/main/asset_0.obj)
  - [Preview GIF] 
  - [PLY file]

![preview](./preview_0.gif)

## Model / references
- OpenAI Shap-E examples and community guides.

## What I’d improve with more time
- Automatic OBJ→GLB conversion and web preview (three.js).
- Better prompt shaping and mesh post-processing (smoothing/decimation).
- Batch generation + simple quality filters.

## Optional API (stub)

A tiny FastAPI stub is included to show how an API would look if this project were hosted.

- `/status` → returns uptime/version
- `/generate3d?prompt=...` → returns a stub response with pointer to `outputs/asset_0.obj`

⚠️ Note: This API is **just a demo** (no real generation).  
To run locally:
1. Install requirements: `pip install fastapi uvicorn pydantic`
2. Run: `python api_demo.py`
3. Visit `http://127.0.0.1:8000/docs` for interactive API docs.


---
