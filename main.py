from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Auth Router
from routes.auth import (
    router as auth_router
)

# Tea Router
from routes.tea import (
    router as tea_router
)

app = FastAPI()


# ==========================
# CORS
# ==========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================
# Include Authentication Routes
# ==========================
app.include_router(
    auth_router
)


# ==========================
# Include Tea Routes
# ==========================
app.include_router(
    tea_router
)