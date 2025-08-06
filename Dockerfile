# --- Stage 1: Tailwind Build --- build 
FROM node:20-slim AS tailwind-builder

WORKDIR /app

# Copy config and input
COPY tailwind.config.js package*.json ./
COPY static/css/input.css ./static/css/input.css
COPY templates ./templates

RUN npm install -D tailwindcss
RUN npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify

# --- Stage 2: Python App ---
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copy final output CSS from builder stage
COPY --from=tailwind-builder /app/static/css/output.css ./static/css/output.css

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
