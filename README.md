Rent & Flatmate Finder
Project Overview
Rent & Flatmate Finder is a full-stack web application that helps tenants discover rental properties and compatible flatmates. Property owners can post room listings, while tenants can browse properties, check AI-powered compatibility scores, express interest, and communicate using WebSocket-based chat support.

🚀 Features
User Registration & Login (JWT Authentication)
Property Listing Management
Add New Property
Property Details
Property Search
AI Compatibility Scoring
Express Interest System
WebSocket Chat Support
Email Notification Support
Admin APIs
Property Availability Management
🛠 Tech Stack
Frontend
React.js
React Router
Axios
Vite
Backend
FastAPI
SQLAlchemy
SQLite
Pydantic
JWT Authentication
AI
Google Gemini API
📂 Project Structure
RentFlatmateFinder/

├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── ...

├── frontend/
│   ├── src/
│   ├── public/
│   └── ...

├── README.md
├── .env.example
└── .gitignore
⚙️ Installation
Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
Backend URL

http://127.0.0.1:8000
Swagger Documentation

http://127.0.0.1:8000/docs
Frontend
cd frontend
npm install
npm run dev
Frontend URL

http://localhost:5173
🔑 Environment Variables
Create a .env file inside the backend folder.

SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_gemini_api_key

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
🗄 Database Schema
The application uses the following primary tables:

User
Property
TenantProfile
Compatibility
Interest
Message
📌 API Endpoints
Authentication
POST /users/signup
POST /users/login
Properties
GET /properties
POST /properties
GET /properties/{property_id}
PUT /properties/{property_id}
DELETE /properties/{property_id}
Compatibility
POST /compatibility
Interest
POST /interest
PUT /interest/{interest_id}/accept
PUT /interest/{interest_id}/decline
Chat
WebSocket /ws/chat/{interest_id}
Email
Email Notification APIs
🤖 AI Compatibility Prompt
The application uses Google Gemini to calculate compatibility between tenant preferences and property details.

Example Prompt

Given this room listing and tenant profile,
calculate a compatibility score between 0 and 100
based on budget, preferred location and
move-in preference.

Return JSON:

{
  "score": 90,
  "explanation": "Budget and location are an excellent match."
}
If the AI service is unavailable, the backend can fall back to a rule-based compatibility calculation.

🔮 Future Enhancements
Google Maps Integration
Property Image Upload
Reviews & Ratings
Push Notifications
Payment Gateway Integration
Mobile Application
👨‍💻 Developer
Ayush Singh

B.Tech Computer Science & Engineering (Data Science)

Pranveer Singh Institute of Technology (PSIT)

Kanpur, Uttar Pradesh

📄 License
This project was developed for educational and internship assignment purposes.