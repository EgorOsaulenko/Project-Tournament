# 🏆 Tournaments App

A web application for managing **sport and esports tournaments** — from local football leagues to Dota 2 brackets.  
Built with **FastAPI** (backend) and ready for frontend integration.

---

## 🚀 Features

### ✅ Authentication & Users
- User registration and login
- Token-based authentication (JWT)
- Role-based access control (admin/player)

### 🧑‍🤝‍🧑 Teams & Players
- Create and manage teams
- Add and remove players
- View team info and rosters

### 🏟️ Tournaments
- Create new tournaments
- Set game, rules, and participant limits
- Join or leave tournaments

### 📅 Matches & Scheduling
- Match generation (round-robin or knockout)
- Assign matches to teams
- Track match results

### 📊 Statistics
- Team rankings
- Player performance
- Match history

---

## 📦 Tech Stack

- **FastAPI** — high-performance Python web framework
- **SQLAlchemy** — database ORM
- **SQLite** — local development DB (easily swappable to PostgreSQL)
- **Pydantic** — data validation
- **Uvicorn** — ASGI server

---

## 📁 Project Structure

app/
├── models/     # SQLAlchemy models
├── schemas/    # Pydantic schemas
├── routes/     # API routes (users, tournaments, matches, etc.)
├── services/   # Business logic
└── main.py     # App entry point
