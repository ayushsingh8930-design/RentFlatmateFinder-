# 🏠 Rent & Flatmate Finder

A full-stack web application that helps tenants find rental properties and compatible flatmates. The platform allows property owners to list properties, tenants to browse listings, check compatibility, express interest, and communicate.

## 🚀 Features

- User Signup & Login (JWT Authentication)
- Property Listing
- Add New Property
- Property Details
- Tenant Profile
- AI Compatibility Score
- Express Interest
- Email Notifications
- Real-time Chat (WebSocket)
- Admin APIs

## 🛠 Tech Stack

### Frontend
- React.js
- React Router
- Axios

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication

### AI
- Google Gemini API

## 📂 Project Structure

```
frontend/
backend/
```

## ⚙️ Installation

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## 🔑 Environment Variables

Create a `.env` file:

```
GEMINI_API_KEY=YOUR_API_KEY
SECRET_KEY=YOUR_SECRET_KEY

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USERNAME=YOUR_EMAIL
EMAIL_PASSWORD=YOUR_APP_PASSWORD
```

## 📌 API Modules

- Authentication
- Properties
- Tenant Profile
- Compatibility
- Interest
- Messages
- Chat
- Email

## 🔮 Future Enhancements

- Payment Integration
- Google Maps
- Image Upload
- Reviews & Ratings
- Notifications
- Mobile Application

## 👨‍💻 Developer

Ayush Singh

B.Tech CSE (Data Science)

PSIT Kanpur