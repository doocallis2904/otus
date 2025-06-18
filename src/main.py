import fastapi
import uvicorn


app = fastapi.FastAPI()
@app.get("/health")
async def root():
    return {"status": "OK"}


uvicorn.run(app, host="0.0.0.0", port=8000)
