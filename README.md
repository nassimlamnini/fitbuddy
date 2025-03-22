# 🏋️‍♂️ FitBuddy: FastAPI + MQTT + PostgreSQL in Docker

This project is a backend system for processing and storing movement data from connected fitness machines. It simulates receiving IoT sensor data, processes it via FastAPI, and stores it in PostgreSQL, all running inside Docker containers with MQTT integration.

---

## 📦 Features

- ⏱ Receives **sensor data** from IoT machines via MQTT (Mosquitto)
- 💾 Stores data in a **PostgreSQL** database (via Docker)
- ⚙️ Clean architecture using **FastAPI**, **SQLAlchemy**, and **Pydantic**
- 📊 Three dedicated tables:
  - `sensor_data` (repetitions, speed, etc.)
  - `asymmetry_data` (left/right side force, imbalance)
  - `sensor_status` (battery, firmware, health)
- 🐳 Containerized using **Docker + Docker Compose**
- ☁️ Prepares for **AWS migration** (API Gateway, RDS, IoT Core)

---

## 🗂 Project Structure

. ├── alembic/ # Database migration folder (alembic) 
  ├── alembic.ini # Alembic configuration 
  ├── database.py # Database connection config 
  ├── models.py # SQLAlchemy ORM models 
  ├── schemas.py # Pydantic request/response schemas 
  ├── services.py # Business logic 
  ├── main.py # FastAPI app + MQTT listener 
  ├── requirements.txt # Python dependencies 
  ├── .env # Environment variables 
  ├── Dockerfile # Docker build config for FastAPI 
  ├── docker-compose.yml # Multi-container setup: API + DB + MQTT 
  └── .dockerignore # Prevents venv & junk files in Docker image
## 🚀 How to Run the Project Locally

### ✅ 1. Prerequisites

- Docker + Docker Compose installed
- Python 3.9+ (optional for MQTT testing outside the container)

---

### ✅ 2. Clone the Repository

```bash
git clone https://github.com/nassimlamnini/fitbuddy
cd fitbuddy
```
---

### ✅ 3. Create .env File

```env
DATABASE_URL=postgresql://nassim:Project145@db/fitbuddy
MQTT_BROKER=mosquitto
MQTT_PORT=1883
```
---

### ✅ 4. Create requirements.txt
```txt
Copy
Edit
fastapi
uvicorn
sqlalchemy
psycopg2
alembic
paho-mqtt
python-dotenv
```
---

### ✅ 5. Launch Everything with Docker Compose
```bash
docker-compose up --build
```
After the build finishes, access the API docs here:

```bash
http://localhost:8000/docs
```
