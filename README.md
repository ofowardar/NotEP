# NotEP - Modern Notes Application

A full-stack notes application built with FastAPI (backend) and React (frontend), featuring user authentication, real-time synchronization, and a beautiful modern UI.

---

## 🎯 Overview

NotEP is a production-ready notes application that demonstrates:
- **Secure Authentication**: JWT-based user authentication with argon2 password hashing
- **RESTful API**: Fully documented FastAPI backend with SQLAlchemy ORM
- **Modern Frontend**: Responsive React UI with Tailwind CSS and smooth animations
- **Professional Deployment**: Deployed on Render (backend) and Vercel (frontend)
- **Comprehensive Testing**: 10 automated tests covering auth and CRUD operations

---

## 🚀 Live Demo

| Component | URL |
|-----------|-----|
| **API Documentation** | https://notep-api-latest.onrender.com/docs |
| **Backend API** | https://notep-api-latest.onrender.com |
| **Frontend** | https://notep-frontend-iy2pgoumt-ofo1.vercel.app |

> **Note**: Render free tier may take 30 seconds for first request (spin-down behavior)

---

## 📸 Screenshots

### Login Screen
![Login Page](pics\login_page.png)
*Screenshot 1: Register/Login interface with dark modern design*

**How to add this screenshot:**
1. Take a screenshot of the login page
2. Upload to GitHub (Issues → paste image → copy markdown link)
3. Replace the placeholder URL above

---

### Dashboard
![Dashboard](pics\notes_dashboard.png)
*Screenshot 2: Notes dashboard showing create, edit, and delete functionality*

**How to add this screenshot:**
1. Login and take a screenshot of the notes list
2. Create/edit a note
3. Upload image to GitHub and replace link above

---

### API Documentation
![Swagger UI](pics\swagger_ui.png)
*Screenshot 3: Interactive Swagger API documentation*

---

## ✨ Features

### Authentication & Security
- ✅ User registration with email validation
- ✅ JWT token-based authentication
- ✅ Argon2 password hashing (industry standard)
- ✅ Secure token storage in localStorage
- ✅ Session management with token expiry

### Notes Management
- ✅ Create, Read, Update, Delete (CRUD) operations
- ✅ Real-time synchronization with backend
- ✅ User data isolation (users only see their own notes)
- ✅ Pagination support (100 notes per request)
- ✅ Search functionality

### User Experience
- ✅ Dark modern UI with gradient accents
- ✅ Smooth animations and transitions
- ✅ Responsive design (mobile, tablet, desktop)
- ✅ Error handling with user-friendly messages
- ✅ Loading states for all async operations

### Development & DevOps
- ✅ Comprehensive test suite (10 tests, 100% pass rate)
- ✅ Environment configuration management
- ✅ Structured logging to file and console
- ✅ Docker containerization
- ✅ CI/CD ready deployment pipeline

---

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI 0.104.1
- **Database**: SQLite (development) / PostgreSQL-ready
- **ORM**: SQLAlchemy 2.0
- **Authentication**: JWT (python-jose) + Argon2
- **Server**: Uvicorn
- **Testing**: Pytest with 100% auth & CRUD coverage
- **Logging**: Python logging with file persistence

### Frontend
- **Framework**: React 18.3
- **Styling**: Tailwind CSS + custom CSS
- **Animations**: Smooth CSS transitions
- **HTTP Client**: Fetch API
- **Storage**: localStorage for JWT tokens
- **Build Tool**: None required (uses CDN)

### Infrastructure
- **Backend Deployment**: Render (Docker container)
- **Frontend Deployment**: Vercel (static hosting)
- **Version Control**: Git & GitHub

---

## 📋 Project Structure

```
NotEP/
├── Backend (FastAPI)
│   ├── main.py              # Application entry point
│   ├── app/
│   │   ├── config.py        # Environment configuration
│   │   ├── database.py      # Database setup & session
│   │   ├── models.py        # SQLAlchemy models
│   │   ├── schemas.py       # Pydantic request/response models
│   │   ├── security.py      # JWT & password utilities
│   │   ├── logging_config.py # Logging configuration
│   │   └── routers/
│   │       ├── auth.py      # Authentication endpoints
│   │       └── notes.py     # Notes CRUD endpoints
│   ├── tests/
│   │   ├── test_auth.py     # Authentication tests
│   │   └── test_notes.py    # Notes functionality tests
│   ├── .env                 # Environment variables (local)
│   ├── .env.example         # Example environment file
│   ├── Dockerfile           # Docker configuration
│   ├── requirements.txt      # Python dependencies
│   └── notes.db             # SQLite database (local)
│
└── Frontend (React)
    ├── index.html           # Single-page application
    └── [Deployed on Vercel]
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 16+ (for frontend development)
- Git

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ofowardar/NotEP.git
   cd NotEP
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run API**
   ```bash
   python -m uvicorn main:app --reload
   ```
   
   API will be available at: `http://localhost:8000`
   Docs: `http://localhost:8000/docs`

### Frontend Setup

1. **Run local HTTP server**
   ```bash
   python -m http.server 5500
   ```

2. **Open in browser**
   ```
   http://localhost:5500
   ```

3. **Create an account and start taking notes!**

---

## 📝 API Endpoints

### Authentication
- `POST /auth/register` - Create new account
- `POST /auth/login` - Login and get JWT token

### Notes Management
- `GET /notes` - List user's notes (with pagination)
- `GET /notes/{note_id}` - Get specific note
- `POST /notes` - Create new note
- `PUT /notes/{note_id}` - Update note
- `DELETE /notes/{note_id}` - Delete note

**Full API documentation available at**: `/docs` (Swagger UI)

---

## 🧪 Testing

Run the comprehensive test suite:

```bash
pytest -v
```

**Test Coverage:**
- ✅ User registration (duplicate prevention)
- ✅ User login (password validation)
- ✅ Note creation, retrieval, update, deletion
- ✅ Authorization (user data isolation)
- ✅ Error handling and edge cases

**Result**: `10 passed in 1.75s`

---

## 🐳 Docker Deployment

### Build Docker Image
```bash
docker build -t notep-api:latest .
```

### Run Container Locally
```bash
docker run -p 8000:8000 notep-api:latest
```

### Deploy to Render
1. Push to GitHub
2. Connect GitHub repo to Render
3. Render automatically builds and deploys

---

## 📚 Learning Outcomes

This project demonstrates:
- ✅ Full-stack development from backend to frontend
- ✅ RESTful API design with FastAPI
- ✅ Database design with SQLAlchemy ORM
- ✅ JWT authentication and authorization patterns
- ✅ Modern React component architecture
- ✅ Responsive design with Tailwind CSS
- ✅ Testing strategies (unit & integration tests)
- ✅ Docker containerization
- ✅ Cloud deployment (Render + Vercel)
- ✅ Professional development workflow (Git, GitHub, CI/CD)

---

## 🔐 Security Features

- **Password Security**: Argon2 hashing (resistant to GPU attacks)
- **JWT Tokens**: Secure token-based authentication
- **CORS Protection**: Configured whitelist for allowed origins
- **Input Validation**: Pydantic schemas for all requests
- **User Isolation**: Users can only access their own notes
- **Error Handling**: Secure error messages (no sensitive data leakage)

---

## 📊 Performance

- **API Response Time**: < 100ms (local), < 500ms (cloud)
- **Database Queries**: Optimized with proper indexing
- **Frontend Bundle**: Minimal dependencies, fast load time
- **Deployment**: Automated with CI/CD pipeline

---

## 🤝 Contributing

This is a portfolio project. For improvements or issues:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**Ömer Faruk Özvardar**
- GitHub: [@ofowardar](https://github.com/ofowardar)
- Email: ofo@example.com
- Role: AI Engineer / Full-Stack Developer

---

## 🎓 Built with Mentorship

This project was developed as part of a comprehensive AI Engineer roadmap, combining:
- Backend API development (FastAPI)
- Frontend development (React)
- Database design (SQLAlchemy)
- Cloud deployment (Render, Vercel)
- Testing & CI/CD practices

---

## 📞 Support

For questions or issues:
1. Check the API docs: `/docs`
2. Review the code comments
3. Check test cases for usage examples
4. Open an issue on GitHub

---

## 🚀 Next Steps

Planned enhancements:
- [ ] PostgreSQL integration for production
- [ ] Advanced search and filtering
- [ ] Note sharing and collaboration
- [ ] Rich text editor integration
- [ ] Mobile app (React Native)
- [ ] Note versioning and history
- [ ] Tag system for organization

---

**Last Updated**: October 15, 2026

Made with ❤️ by Ömer Faruk Özvardar
