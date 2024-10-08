# Continuous Monitoring By Prometheus

### Introduction to Continuous Monitoring
#### What is Continuous Monitoring?
- Continuous Monitoring is an automated process by which one can observe and detect compliance issues and security threats during each phase of the DevOps and MLOps pipeline.

- Continuous Monitoring in ML refers to the ongoing process of tracking the Performance and behavior of ML models after they have been deployed into production. The goal of continuous monitoring is to ensure that the models continue to perform as expected, remain accurate, and provide reliable predictions as the environment and data they operate on evolve over time.

#### Key Aspects of Continuous Monitoring in ML:
1. Performance Monitoring:
   - Regularly track metrics such as accuracy, precision, recall, F1 score, AUC, etc., to ensure the model's predictions are still valid.
   - Compare current Performance metrics against historical Performance to detect any significant changes.

2. Data Drift Detection:
   - Concept Drift: Occurs when the relationship between input data and target output changes over time. Continuous monitoring helps detect and address such changes.
   - Data Drift: Involves monitoring input data distributions to detect when the data the model is seeing in production starts to differ significantly from the training data.

3. Infrastructure Monitoring:
   - Keep an eye on system-level metrics such as CPU/GPU utilization, memory usage, latency, and throughput.
   - Ensure that the infrastructure supporting the ML model is performing efficiently and can handle the incoming data and prediction requests.

4. Error and Anomaly Detection:
   - Monitor for unexpected errors or anomalies in the model's output, such as unusually high error rates or unexpected prediction distributions.
   - Set up alerts to notify the team when something goes wrong, allowing for quick response and troubleshooting.

5. Model Versioning and Retraining:
   - Track which version of the model is currently in production and how it performs over time.
   - Monitor the need for retraining the model based on new data or changes in Performance.

6. Cost Monitoring:
   - Track the computational and operational costs associated with running ML models in production.
   - Manage budgets and optimize resources to ensure cost-effective operations, especially in Cloud-based deployments.

7. Compliance and Governance:
   - Ensure that the model adheres to regulatory requirements and organizational policies.
   - Monitor for any biases or ethical concerns that might arise in the model's predictions.

8. User Feedback Integration: ***[1]***
   - Continuously gather feedback from end-users to assess how well the model is meeting their needs and expectations.
   - Use feedback to make adjustments or improvements to the model over time.

#### Why Continuous Monitoring is Important:
- Maintain Model Accuracy: As Real-world data can change over time, continuous monitoring helps ensure that the model remains accurate and reliable.
- Early Detection of Issues: Continuous monitoring allows for the early detection of problems like data drift, concept drift, or infrastructure issues, minimizing downtime and negative impact.
- Compliance: Helps maintain compliance with industry regulations by continuously monitoring for biases, fairness, and other ethical considerations.
- Optimized Operations: By keeping track of system Performance and costs, continuous monitoring can help in optimizing resources and reducing operational expenses.

#### Tools and Techniques for Continuous Monitoring:
- Monitoring Tools: Prometheus, Grafana, Sensu, etc.
- Alerting Systems: Prometheus AlertManager, Slack, PagerDuty, etc.
- Metrics Storage: InfluxDB, Splunk, Elasticsearch, AWS S3, etc.
- Visualization Tools: Grafana, Kibana, Tableau, etc.

- Prometheus and Grafana: For system and Performance MONITORING, with customizable dashboards and ALERTING.
- Evidently, Alibi Detect, and DeepChecks: For Data and Concept Drift detection.
- MLflow, Tecton, and Neptune.ai: For Experiment tracking and model Performance monitoring.
- AWS CloudWatch, Azure Monitor, Google Cloud Monitoring: For Cost tracking and infrastructure monitoring in Cloud environments.

In summary, continuous monitoring is an essential practice in MLOps (ML Operations) that helps ensure that ML models continue to perform effectively, adapt to changing conditions, and remain aligned with business goals and compliance requirements.

### Use case on Continuous Monitoring by Prometheus and Grafana
Prometheus and Grafana

- Prometheus provided the company an easy way to collect all the required metrics for day-to-day operations.
- Prometheus also provided the ability to monitor the modern system as well as legacy system.
- Alerting mechanism in the new monitoring system was easy to embed with the dashboards.
- Grafana made the dashboard visualization more accessible for various teams in the organization.

Prometheus helps in collecting and monitoring metrics, while Grafana provides accessible and customizable dashboard visualizations that make it easier for teams to analyze and respond to data.

### Introduction to Prometheus
// Dimensional Data of Prometheus
- Metrics: Time-series data representing the state of a system or application.
- Labels: Key-value pairs that help identify and differentiate time-series data.
- Samples: Individual data points in a time-series.
- Scraping: The process of collecting metrics data from targets.
- Alerting: The ability to define alerting rules based on metrics data.

// Prometheus Features
- Prometheus includes a Flexible Query Language - PromQL (Read ONLY).
- Can generate visualizations using Built-in expression browser, or can be integrated with Grafana.
- It stores metrics in memory and Local Disk in an own custom, efficient format.
- Written in Go.
- Supports multiple- Client libraries and Integrations available.
- Pull-based model for collecting metrics data.

### Architecture of Prometheus
https://prometheus.io/docs/introduction/overview/

Long-term Storage for Prometheus by integrating other systems like:
- Cortex, or
- Remote storage solutions 
   - AWS S3, DynamoDB,
   - Google Cloud Storage, etc.

// Prometheus Server
- Prometheus collects the metrics from monitored targets by 'SCRAPING' the metrics via HTTP endpoints.
   - Database
   - Linux/Windows Host
   - Kubernetes Cluster
   - Docker Containers
   - Web Servers
   - Application Servers
   - etc.
- Instead of running custom scripts that check on particular services & systems, the monitoring data itself is used.
- A single Prometheus server is able to ingest up to 1M samples per second as several million time series.

// Prometheus PushGateway
- The Prometheus PushGateway exists to allow ephemeral and batch jobs to expose their metrics to Prometheus.
- Since these kinds of jobs may NOT exist long enough to be scraped, they can instead PUSH their metrics to a PushGateway.
- The PushGateway then exposes these metrics to Prometheus.

// Exporters and Integrations
- There are a number of libraries and servers which help in exporting existing metrics from 3 party systems (that do NOT natively expose metrics in a format Prometheus) into Prometheus metrics.
- This is useful for cases where it is NOT feasible to instrument a given system with Prometheus metrics directly (for example, HAProxy or Linux system stats).
- https://prometheus.io/docs/instrumenting/exporters/

// Prometheus AlertManager
- The AlertManager handles alerts sent by client applications such as the Prometheus server.
- It takes care of deduplicating, grouping, and routing them to the correct receiver integration such as email, PagerDuty, or OpsGenie.
- It also takes care of silencing and inhibition of alerts.

// Service Discovery
- Prometheus service discovery is a standard method of finding endpoints to scrape for metrics.
- We need to configure prometheus.yaml and custom jobs to prepare for scraping endpoints in the same way we do for native Prometheus.
- https://prometheus.io/docs/prometheus/latest/configuration/configuration/#service_discovery

// PromQL
- PromQL, short for Prometheus Querying Language, is the main way to query metrics within Prometheus.
- You can display an expression’s return either as a graph or export it using the HTTP API.

### Metric Types of Prometheus
Prometheus metrics are typically time-series data, meaning that they are recorded over time and can be queried based on time ranges.

// Metric Types
https://www.timescale.com/blog/four-types-prometheus-metrics-to-collect/

1. Counter: A cumulative metric that represents a Single monotonically Increasing counter whose value can only increase or be reset to zero on restart.
   Use Case: Track things like the number of requests received, the number of errors/completed encountered, or the total bytes processed.

2. Gauge: A metric that represents a Single numerical value that can arbitrarily go Up and Down.
   Use Case: Track metrics like CPU usage, memory usage, current temperatures, concurrent request, or the current number of active sessions.
   
3. Histogram: Samples observations (usually things like request durations or response sizes) and counts them in configurable buckets.  It also provides a sum of all observed values.
   Use Case: Track the distribution of a metric, such as the response times of an API, by observing values and counting them in specified buckets.

4. Summary: Similar to a histogram, but instead of counting observations, it sums them and calculates quantiles over a sliding time window.
   Use Case: Track metrics like request durations or response sizes and calculate quantiles (e.g., 50th, 90th, 99th percentile) over a sliding time window.

   http_request_duration_seconds{quantile="0.5", endpoint="/api/v1/resource"} 0.150 # 50th percentile
   http_request_duration_seconds{quantile="0.9", endpoint="/api/v1/resource"} 0.250 # 90th percentile
   http_request_duration_seconds{quantile="0.99", endpoint="/api/v1/resource"} 0.400 # 99th percentile

### Installation of Prometheus
https://prometheus.io/docs/prometheus/latest/installation/
https://github.com/prometheus/prometheus/releases
https://github.com/prometheus/prometheus/releases/tag/v2.54.1

// WSL2
sudo su -
git --version
   git version 2.34.1   

cd /mnt/d/development/Complete-MLOps-BootCamp

git clone https://github.com/manifoldailearning/Prometheus-Grafana-Docs
cd Prometheus-Grafana-Docs/

// Prometheus Installation
1. Check the architecture of your System
uname -m
   If it returns x86_64, your system is running a 64-bit architecture.
   If it returns armv7l or aarch64, your system is running on an ARM architecture.

2. Download the Prometheus Binaries
wget https://github.com/prometheus/prometheus/releases/download/v2.54.1/prometheus-2.54.1.linux-arm64.tar.gz
tar xvfz prometheus-2.54.1.linux-arm64.tar.gz

3. Move the Prometheus Binaries
sudo mv prometheus-2.54.1.linux-arm64/prometheus /usr/local/bin/
sudo mv prometheus-2.54.1.linux-arm64/promtool /usr/local/bin/

4. Create a Prometheus user
sudo useradd --no-create-home --shell /bin/false prometheus

5. Create a Prometheus Configuration Directory
sudo mkdir -p /etc/prometheus
sudo mkdir -p /var/lib/prometheus

6. Move the configuration files
sudo mv prometheus-2.54.1.linux-arm64/prometheus.yml /etc/prometheus/
sudo mv prometheus-2.54.1.linux-arm64/consoles /etc/prometheus/
sudo mv prometheus-2.54.1.linux-arm64/console_libraries /etc/prometheus/

7. Set ownership
sudo chown -R prometheus:prometheus /etc/prometheus /var/lib/prometheus

8. Create a systemd service file
echo "[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus \
  --config.file=/etc/prometheus/prometheus.yml \
  --storage.tsdb.path=/var/lib/prometheus/ \
  --web.console.templates=/etc/prometheus/consoles \
  --web.console.libraries=/etc/prometheus/console_libraries

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/prometheus.service

9. Reload systemd and start Prometheus
sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl enable prometheus

10. Check the status of Prometheus
sudo systemctl status prometheus
   ● prometheus.service - Prometheus
      Loaded: loaded (/etc/systemd/system/prometheus.service; enabled; vendor preset: enabled)
      Active: active (running) since Fri 2024-09-06 18:40:56 CST; 20s ago
      ...

11. Clean up
rm -rf prometheus-2.54.1.linux-arm64.tar.gz prometheus-2.54.1.linux-arm64

12. Access Prometheus Web UI
cat /etc/prometheus/prometheus.yml
   ...
   static_configs:
     - targets: ["localhost:9090"]


sudo nano /etc/prometheus/prometheus.yml
http://localhost:9090/
http://localhost:9090/metrics
http://localhost:9090/targets?search=

curl http://localhost:9090/metrics

### Introduction Grafana
Grafana is an open-source platform analytics and interactive visualization Web application.

Grafana provides:
- Charts, 
- Graphs, and 
- Alerts.

// Key Features of Grafana
- Visualization options to help you understand your data, beautifully.
- Seamlessly define alerts when it make sense - while you're in a given dataset.

// Other Features
- Discover hundreds of Dashboards and plugins in the Grafana library.
- Share data and Dashboards across teams.
- Support for multiple data sources.

### Installation of Grafana ARM on WSL2
https://grafana.com/grafana/download/11.2.0
https://grafana.com/grafana/download/11.2.0?platform=arm

cd /mnt/d/development/Complete-MLOps-BootCamp/Prometheus-Grafana-Docs/

1. Add Grafana APT repository (Note: Check if ARM packages are available)
echo 'deb https://packages.grafana.com/oss/deb stable main' | sudo tee -a /etc/apt/sources.list.d/grafana.list

2. Add Grafana GPG key
curl https://packages.grafana.com/gpg.key | sudo apt-key add -

3. Update package list and install Grafana
sudo apt update
sudo apt install grafana

4. Check architecture and install appropriate package
ARCH=$(dpkg --print-architecture)
echo $ARCH
   arm64

5. Install Grafana
sudo apt install -y grafana

6. Start and enable Grafana
sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl enable grafana-server.service
sudo systemctl status grafana-server
   ● grafana-server.service - Grafana instance
      Loaded: loaded (/lib/systemd/system/grafana-server.service; enabled; vendor preset: enabled)
      Active: active (running) since Fri 2024-09-06 20:11:46 CST; 16s ago
      ...

http://localhost:3000/
   Username: admin
   Password: admin

Home => Connections => Prometheus => Data Sources => Add Data Source (Prometheus)
   Name: Prometheus
   URL: http://localhost:9090
   Access: Server (Default)
   => Save & Test (Successfully queried the Prometheus API.)

### After Installation
sudo apt-key export 10458545 | sudo gpg --dearmor -o /usr/share/keyrings/grafana-archive-keyring.gpg
sudo nano /etc/apt/sources.list.d/grafana.list
deb [signed-by=/usr/share/keyrings/grafana-archive-keyring.gpg] https://packages.grafana.com/oss/deb stable main
sudo apt-key del 10458545
sudo apt update -y

sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl enable grafana-server.service
sudo systemctl status grafana-server

### Prometheus Configuration file
https://prometheus.io/docs/prometheus/latest/configuration/configuration/
https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config

// Prometheus Configuration
- The Prometheus configuration file is written in YAML format.
- Configuration can be changed and reloaded without restarting the Prometheus server.
- You can also pass parameters to Prometheus using flags when starting the server (./prometheus).
- To scrape metrics from a target, you need to define a job in the configuration file.
- When Installing Prometheus scrapes metrics from itself.

cat /etc/prometheus/prometheus.yml

// k8s ca.crt
grep 'certificate-authority-data' ~/.kube/config | awk '{print $2}' | base64 --decode > ca.crt

// prometheus.yml Conceptual to Scrape Config
sudo nano /etc/prometheus/prometheus.yml 
prometheus --config.file=/etc/prometheus/prometheus.yml
sudo systemctl start prometheus
sudo systemctl status prometheus

### Exploring the Basic Querying Prometheus
https://prometheus.io/docs/prometheus/latest/querying/basics/
https://prometheus.io/docs/prometheus/latest/querying/functions/
https://prometheus.io/docs/prometheus/latest/querying/examples/

- prometheus_http_requests_total > 0
- prometheus_http_requests_total{code="200",handler="/api/v1/query",instance="localhost:9090",job="prometheus"}
- prometheus_http_requests_total{code="200",instance="localhost:9090",job="prometheus"} > 0
- rate(prometheus_http_requests_total[5m])[30m:1m] 
   # 计算过去30分钟内，每5分钟的HTTP请求率，每1分钟计算一次。
- last_over_time(rate(prometheus_http_requests_total[5m])[30m:1m]) > 0
   # 计算过去 30 分钟内，每 5 分钟的 HTTP 请求速率，每分钟计算一次，然后取最新的一个速率值，并只显示大于 0 的结果。
- last_over_time(rate(prometheus_http_requests_total{code="400"}[5m])[30m:1m]) > 0
   # 计算过去 30 分钟内，每 5 分钟的 HTTP 请求速率，每分钟计算一次，然后取最新的一个速率值，并只显示状态码为 400 的结果。
- last_over_time(rate(prometheus_http_requests_total{code="200"}[5m])[30m:1m]) > 0
   # 计算过去 30 分钟内，每 5 分钟的 HTTP 请求速率，每分钟计算一次，然后取最新的一个速率值，并只显示状态码为 200 的结果。

### Monitor the Infrastructure with Prometheus
https://prometheus.io/docs/guides/node-exporter/

// Node Exporter
- Node Exporter is a Prometheus exporter for hardware and OS metrics exposed by *NIX kernels, written in Go with pluggable metric collectors.
- It allows you to monitor various system resources such as CPU, memory, disk, and network usage.
- Node Exporter is an essential component in monitoring the infrastructure of your systems.
- Windows Exporter (WMI Exporter) is available for monitoring Windows systems.
   https://github.com/prometheus-community/windows_exporter

### Monitor the Linux Server with Node Exporter
// Install Node Exporter WSL2
cd /mnt/d/development/Complete-MLOps-BootCamp/Prometheus-Grafana-Docs/
sudo su -
wget https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.linux-arm64.tar.gz

tar -xvf node_exporter-1.8.2.linux-arm64.tar.gz
sudo mv node_exporter-1.8.2.linux-arm64/node_exporter /usr/local/bin/

sudo echo "[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
" > /etc/systemd/system/node_exporter.service

sudo cat /etc/systemd/system/node_exporter.service

sudo useradd -rs /bin/false node_exporter
sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl enable node_exporter
sudo systemctl status node_exporter

http://localhost:9100/metrics

// Prometheus Configuration for Node Exporter
sudo nano /etc/prometheus/prometheus.yml
   - job_name: 'node_exporter'
     static_configs:
       - targets: ['localhost:9100']

sudo systemctl restart prometheus
http://localhost:9090/targets?search=

exit

// Prometheus Query
- go_gc_duration_seconds{quantile="1"}
- go_gc_duration_seconds{quantile="0.99"}
- node_cpu_seconds_total{job="node_exporter", mode="system"} > 0
- node_memory_MemTotal_bytes{job="node_exporter"} > 0

### Monitor the Client Application using Prometheus
https://prometheus.io/docs/instrumenting/clientlibs/#client-libraries
https://github.com/prometheus/client_java/blob/main/pom.xml

// Prometheus Client Libraries
- Prometheus provides client libraries for various programming languages (such as Go, Java, Python, Ruby, and more) to help instrument your code and expose metrics.
   Example: 
      Python https://github.com/prometheus/client_python
         https://prometheus.github.io/client_python/getting-started/three-step-demo/
      Java https://github.com/prometheus/client_java
         https://prometheus.github.io/client_java/getting-started/quickstart/ # Maven

- Client libraries implement the Prometheus metric types.
- Client libraries allow you to collect custom metrics from your applications and services and expose them to Prometheus for monitoring via HTTP.

// Unofficial third-party client libraries
- There are also unofficial third-party client libraries available for other languages and frameworks.
- Example: Node.js prom-client https://github.com/siimon/prom-client

// FastAPI Prometheus
https://github.com/trallnag/prometheus-fastapi-instrumentator

### Monitor the Python Application using Prometheus
cd Continuous-Monitoring-Prometheus-Grafana\Prometheus-Grafana-Learning\fast-api-metrics
pip install -r requirements.txt

// FastAPI Application Test
python main.py
   ...
   Instrumentator().instrument(app).expose(app)

http://127.0.0.1:8005/
http://127.0.0.1:8005/demo

http://127.0.0.1:8005/docs
   - Test Post
http://127.0.0.1:8005/metrics

// Build Docker Image
docker build -t fast-api .
docker run -d -p 8005:8005 fast-api
http://localhost:8005/
http://localhost:8005/metrics

// Prometheus Configuration for FastAPI WSL2
echo "  - job_name: 'app'
    static_configs:
      - targets: ['127.0.0.1:8005']" >> /etc/prometheus/prometheus.yml

sudo systemctl restart prometheus

http://localhost:9090/targets?search=

- http_requests_total
- histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[1m])) > 0.005
   - track requests that take more than 0.005 seconds (5 milliseconds)

### Monitor All EndPoints using Prometheus
https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config
- http_request_duration_seconds_created
- http_request_duration_seconds_sum
- http_request_duration_seconds_count

### Create Visualization (Dashboards) with Grafana
http://localhost:3000/ => Explore => Prometheus => Code => Metrics Browser (// Queries) => Run Query (refresh icon)
- app
- node_exporter
- prometheus

// Queries
- scrape_duration_seconds
- rate(scrape_duration_seconds[5m])
- sum(rate(scrape_duration_seconds[5m]))
- sum(rate(scrape_duration_seconds[5m])) by (job)

http://localhost:3000/ => Dashboards => Create Dashboard => Add Visualization => Prometheus => Code => Metrics Browser (scrape_duration_seconds) => Run Queries

Options => Legend ({{job}}) 

Time series => Title (Scrape Duration Seconds) => Visualization (Graph) => Apply => Save dashboard => Name (Scrape Duration Seconds) => Save

Add => Visualization => Prometheus => Code => Metrics Browser (http_request_duration_seconds_created{handler="/post_demo",method="POST"}) => Run Queries

Time Series => Title (HTTP Request Duration Seconds Created - App Post Demo) => Visualization (Graph) => Apply => Save Dashboard => Save

### Trigger Alerts with Grafana
// Request Bin Web Hook to Test Alerts
https://pipedream.com/requestbin => Create Request Bin => SignUp (Google Account) => Create Request Bin => Invite by URL (https://pipedream.com/@samfire5200/invite?token=81ac1acbe4dbe070af3d3fa7811c2fd6) => Skip => The unique URL (https://eoh9bcl4bko3aji.m.pipedream.net) => See Code Example

curl -d '{
  "test": "event"
}'   -H "Content-Type: application/json"   https://eoh9bcl4bko3aji.m.pipedream.net

http://localhost:3000/ => Alerting => Contact Points => Add Contact Point => 
- Name (Request Bin) 
- Integration (Webhook)
- URL (https://eoh9bcl4bko3aji.m.pipedream.net) => Test => Send test notification => "View Request Bin in the Browser" => Save contact point

// Alerting Rules
Alerting => Alert Rules => New Alert Rule =>
- Name (HTTP Request Duration Seconds Created - App Post Demo)
- Metrics browser (http_request_duration_seconds_created{handler="/post_demo",method="POST"})

Expressions => Delete defaulted Expressions => Add Expression (Classic condition (legacy)) =>
- WHEN (sum())
- OF (A)
- IS ABOUT (0)

Set evaluation behavior => New Folder => Folder Name (Grafana Alerts - App Post Demo) => Create => New evaluation group => 
- Evaluation group (Grafana Alerts - App Post Demo)
- Evaluation interval (10s) => Create

Pending period (10s)
Contact point (Request Bin)
Add annotations (App Post Demo Request Duration Seconds > 0)
=> Save rule and exit

Notification Policies => Default Policy => Edit =>
- Default contact point (Request Bin)
- Timing Options 
   - Group wait (10s)
   - Group interval (10s)
   - Repeat interval (10s)
=> Update default policy

Alert rules => 1 rule/1 firing

// View in Request Bin
- You've exceeded your daily quota (not an issue due to Free Plan)

// Change Notification Policy
Notification Policies => Default Policy => Edit =>
- Default contact point (Request Bin)
- Timing Options 
   - Group wait (2h)
   - Group interval (2h)
   - Repeat interval (2h)
=> Update default policy   

### Hands On folder 'Continuous-Monitoring-ML-Application'
cd Continuous-Monitoring-Prometheus-Grafana\Continuous-Monitoring-ML-Application\src\prediction_model

set PYTHONPATH=D:\development\Complete-MLOps-BootCamp\Continuous-Monitoring-Prometheus-Grafana\Continuous-Monitoring-ML-Application\src

// Edit preprocessing.py
    X[col] = X[col].fillna(self.mode_dict[col])
    X[col] = X[col].fillna(self.mean_dict[col])
    
python training_pipeline.py
    Model has been saved under the name classification.pkl

cd ..\..
docker build --build-arg PYTHONPATH_ARG=/code/src -t loan_pred:v1 .
