# 🎓 Student Grade Tracker

A full-stack-ish web application that helps students(in first year for now) track their academic modules, assessments, and progress.  
Built with a Flask backend and a React frontend.
* App created as a side project with cput App dev students and blackbard as usecases.
---

## 🚀 Features



- User registration and login
- Add/edit/delete academic modules
- Track assessments per module
- Calculate current grades
- Show required grades to reach targets
- Flag progress: On Track / Achievable / At Risk

---
## 📦 Tech Stack
* Backend: Flask, SQLAlchemy, Flask-Login, Flask-WTF, Python-dotenv
* Frontend: React, Tailwind CSS, Lucide Icons
* Database: SQLite (for development), PostgreSQL/MySQL (optional for prod)
* Auth: Session-based (Flask-Login)Backend: Flask, SQLAlchemy, Flask-Login, Flask-WTF, Python-dotenv
* Frontend: React, Tailwind CSS, Lucide Icons

## Development Notes
* Backend uses the app factory pattern
* All backend config is loaded via .env
* REST API returns JSON for frontend consumption
* Authentication uses session cookies (can be swapped for JWT if needed)

---
## 📅 Roadmap (Next Steps)

- [ ] Set up Flask backend and virtualenv
- [ ] Design API and implement authentication
- [ ] Build React module management UI
- [ ] Connect the frontend to the Flask backend
- [ ] Add grade analysis logic
- [ ] Polish UI and prepare for deployment
- [ ] Test deployment models
- [ ] ...
