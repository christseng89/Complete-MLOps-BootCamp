# Monitoring ML Application

### Architecture of ML Application Monitoring
- ML Application (8105)
- Prometheus (9190)
- Grafana (3100)
- Node Exporter (9170)
- Network - example_network

### Hands On Monitoring of ML Application using Prometheus
cd Continuous-Monitoring-Prometheus-Grafana\Continuous-Monitoring-ML-Application

set PYTHONPATH=D:\development\Complete-MLOps-BootCamp\Continuous-Monitoring-Prometheus-Grafana\Continuous-Monitoring-ML-Application\src

python main.py

http://127.0.0.1:8005/
http://127.0.0.1:8005/metrics
http://127.0.0.1:8005/docs

docker build -t ml-app .
docker images | grep ml-app

docker-compose up -d --scale app=2 --remove-orphans

// Prometheus
http://localhost:9190/
http://localhost:9190/targets
http://localhost:9190/metrics
- http_requests_total
- http_request_duration_seconds_bucket

// Grafana
http://localhost:3100/
    admin/grafana

http://localhost:3100/datasources
http://localhost:3100/dashboards

Create dashboard => Import dashboard => Upload dashboard JSON file => prometheus-dashboard.json => Prometheus => Import

// App

http://localhost:8105/
http://localhost:8105/metrics
http://localhost:8105/docs

http://localhost:8106/
http://localhost:8106/metrics
http://localhost:8106/docs

docker-compose logs 
docker-compose logs app-1
docker-compose logs app-2
docker-compose logs prometheus
docker-compose logs grafana
