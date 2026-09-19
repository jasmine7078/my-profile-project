
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="My Profile API")

# 개인 소개 페이지에서 백엔드 API를 호출할 수 있도록 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "My Profile API is running!"}


@app.get("/profile")
def get_profile():
    return {
        "organization": "신용보증기금",
        "role": "매출채권보험 인수 및 심사",
        "interests": ["금융", "데이터 분석", "AI", "프로그래밍"]
    }