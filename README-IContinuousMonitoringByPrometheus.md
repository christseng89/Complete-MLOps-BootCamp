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
