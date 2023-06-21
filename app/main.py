from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.main import v1_router as api_v1_router, v2_router as api_v2_router

app = FastAPI(
    title="微服务模板", description="微服务模板，支持接口标签分组显示,", swagger_ui_parameters={"docExpansion": "none"}
)

app.include_router(api_v1_router, prefix="/api/v1")
app.include_router(api_v2_router, prefix="/api/v2")


@app.get("/", include_in_schema=False)
async def health() -> JSONResponse:
    return JSONResponse({"message": "It worked!!"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
