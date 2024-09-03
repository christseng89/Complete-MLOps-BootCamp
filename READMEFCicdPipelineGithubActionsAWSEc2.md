# CI/CD Pipeline w GitHub Actions for AWS EC2

### Agenda of the Section
// Git clone
git clone https://github.com/manifoldailearning/python-for-mlops-aiops-devops.git

// Folder Python-for-mlops-aiops-devops\8.ci-cd-python

// GitHub Checkout Versions
https://github.com/actions/checkout
https://github.com/actions/checkout/tree/releases/v3
https://github.com/actions/checkout/tree/releases/v4.0.0

### Exploring the files of CI CD Python
cd Python-for-mlops-aiops-devops\8.ci-cd-python
python app.py

http://10.39.101.8:5000/

cd Python-for-mlops-aiops-devops\8.ci-cd-python
python tests.py

    Ran 1 test in 0.013s
    OK

docker build -t my-flask-app:latest .

// .github\workflows\actions.yaml # Reference ONLY...
