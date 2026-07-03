# 🏠 Rent & Flatmate Finder

## Project Overview

Rent & Flatmate Finder is a full-stack web application that helps tenants discover rental properties and compatible flatmates. Property owners can list rooms, while tenants can browse listings, check AI-powered compatibility scores, express interest, and communicate using WebSocket-based chat support.

## 🚀 Features

- User Registration & Login (JWT Authentication)
- Property Listing Management
- Add New Property
- Property Details
- Property Search
- AI Compatibility Scoring
- Express Interest System
- WebSocket Chat Support
- Email Notification Support
- Admin APIs
- Property Availability Management

## 🛠 Tech Stack

### Frontend
- React.js
- React Router
- Axios
- Vite

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication

### AI
- Google Gemini API

## 📂 Project Structure

```text
RentFlatmateFinder/
│
├── backend/
├── frontend/
├── README.md
├── .env.example
└── .gitignore
```

## ⚙️ Installation

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend:
`http://127.0.0.1:8000`

Swagger:
`http://127.0.0.1:8000/docs`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend:
`http://localhost:5173`

## 🔑 Environment Variables

Create a `.env` file inside the **backend** folder.

```env
SECRET_KEY=your_secret_key
GEMINI_API_KEY=your_gemini_api_key

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

## 🗄 Database Schema

- User
- Property
- TenantProfile
- Compatibility
- Interest
- Message

## 📌 API Endpoints

### Authentication
- POST `/users/signup`
- POST `/users/login`

### Properties
- GET `/properties`
- POST `/properties`
- GET `/properties/{property_id}`
- GET `/properties/search`
- GET `/properties/owner/{owner_id}`
- PUT `/properties/{property_id}`
- PUT `/properties/{property_id}/filled`
- DELETE `/properties/{property_id}`

### Compatibility
- POST `/compatibility`

### Interest
- POST `/interest`
- PUT `/interest/{interest_id}/accept`
- PUT `/interest/{interest_id}/decline`

### Chat
- WebSocket `/ws/chat/{interest_id}`

### Admin
- Admin APIs

## 🤖 AI Compatibility Prompt

The application uses **Google Gemini API** to calculate compatibility between tenant preferences and property details.

Example:

```text
Given this room listing and tenant profile,
calculate a compatibility score between 0 and 100
based on budget, preferred location and move-in preference.

Return JSON:

{
  "score": 90,
  "explanation": "Budget and location are an excellent match."
}
```

If the AI service is unavailable, the backend falls back to a rule-based compatibility calculation.

## 🔮 Future Enhancements

- Google Maps Integration
- Property Image Upload
- Reviews & Ratings
- Push Notifications
- Payment Gateway Integration
- Mobile Application

## 👨‍💻 Developer

**Ayush Singh**

B.Tech Computer Science & Engineering (Data Science)

Pranveer Singh Institute of Technology (PSIT), Kanpur

## 📄 License

This project was developed for educational and internship assignment purposes.