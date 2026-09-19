
# My Profile Project

클라우드컴퓨팅실습 개인 과제로 제작한 개인 소개 페이지 및
FastAPI 백엔드 연동 프로젝트입니다.

## 1. 프로젝트 소개

HTML과 CSS를 이용해 개인 소개 페이지를 제작하고,
JavaScript의 fetch()를 통해 FastAPI 백엔드에서
프로필 정보를 불러오도록 구현했습니다.

## 2. 주요 구성

- 프론트엔드: HTML, CSS, JavaScript
- 백엔드: Python, FastAPI
- 프론트엔드 배포: Vercel
- 백엔드 배포: Render

## 3. 주요 기능

- 개인 소개 및 관심 분야 표시
- FastAPI의 GET /profile API 제공
- 버튼 클릭 시 백엔드에서 프로필 정보를 받아 화면에 표시

## 4. 프로젝트 구조

```text
my-profile-project/
├── my-profile/
│   └── index.html
├── my-profile-backend/
│   ├── main.py
│   └── requirements.txt
└── README.md
```

## 5. 배포 주소

- 개인 소개 페이지 (Vercel): https://my-profile-project-zeta.vercel.app
- 백엔드 API 문서 (Render Swagger UI): https://my-profile-project-nbm.onrender.com/docs
- 백엔드 프로필 API: https://my-profile-project-nbm.onrender.com/profile