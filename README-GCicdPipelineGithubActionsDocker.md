# CI/CD Pipeline w GitHub Actions for Docker

### Test CI CD on ML Project with Docker - FastAPI
cd CI-CD-ml-project
python -m venv mlenv
mlenv\Scripts\activate

pip install -r requirements.txt

python main.py
http://127.0.0.1:8000/

// Postman => MLflow => FastAPI main => 