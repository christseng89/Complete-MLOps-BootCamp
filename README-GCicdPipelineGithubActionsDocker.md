# CI/CD Pipeline w GitHub Actions for Docker

### Test CI CD on ML Project with Docker - FastAPI
cd CI-CD-ml-project
python -m venv mlenv
mlenv\Scripts\activate

pip install -r requirements.txt

python main.py
http://127.0.0.1:8000/

// Postman => MLflow => FastAPI - main => 'Loan Predict - CI/CD main'

python tests\test_prediction.py
    Model has been loaded

docker build -t my-mlapp:latest .

### Pre-requisite setup for CI CD pipeline

// AWS and GitHub
- Create ECR - Registry
- Create EC2 Instance 
- EC2 Connection
    - Install Docker
    - Login to ECR
- Setup GitHub Actions Secrets => GitHub => <repository> => Settings => Secrets and Variables
    https://github.com/<uid>/<repository>/settings/secrets/actions

    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_REGION
    - AWS_ACCOUNT_ID
    - EC2_HOST (Public IPv4 DNS, ec2-3-...)
    - EC2_USERNAME (ec2-user)
    - EC2_SSH_KEY (RSA Private Key)
