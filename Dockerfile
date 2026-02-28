FROM python:3.10-slim
WORKDIR /app
RUN pip install fastapi uvicorn
COPY app.py .
EXPOSE 7860
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]