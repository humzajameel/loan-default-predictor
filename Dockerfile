# 1. Use official Python base image
FROM python:3.11-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy only dependency files first (for caching)
COPY requirements.txt requirements.txt
COPY requirements.in requirements.in

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the entire project code
COPY . .
COPY model.joblib model.joblib


# 6. Expose port 8000 (default for FastAPI)
EXPOSE 8000

# 7. Set the default command to run the API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
