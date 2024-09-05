# Monitoring and Debugging ML Models

### Why Monitoring ML Models is Important
// Importance of Monitoring

- ML models are now more frequently employed for critical Real-world tasks, ranging from the detection of fraudulent activities to the implementation of automated braking systems in vehicles.

- The responsibilities of ML professionals extend well beyond the deployment of a model into a production environment.

- It is important to constantly oversee the Performance of these models to guarantee their continued effectiveness when confronted with Real-world scenarios.

- Nevertheless, merely adopting 'conventional software monitoring' practices falls short of what's necessary in the context of ML systems. 采用传统的软件监控实践在机器学习系统的背景下是不够的。

// Questions to think
- How do we monitor effectively?
- What metrics to choose?
- What tools are available?

### What is Monitoring of ML models & When to Update Model in Production
// Monitoring of ML Models

- It's important to Note that monitoring is NOT a one-time task that can be completed and then forgotten.
- Monitoring entails the ongoing process of observing a deployed model's behavior to assess its 'Performance'.
- Post-deployment monitoring is crucial because ML models can deteriorate and malfunction when in active use.

// When to Update the Model in Production?

- To determine the appropriate moment for updating a model in a production environment, it's essential to maintain a Real-time perspective that enables stakeholders to Continuously evaluate the model's Performance within the live setting.
- This continuous assessment ensures that the model is operating as anticipated.
- Achieving 'Maximum Visibility' into your deployed model is a necessity for identifying potential issues and their origins before they have a detrimental impact on the business.

### Why Monitoring ML Models is Difficult
// Hidden Technical Debt of ML

- Configuration
- ML Code
    - Data Collection
    - Data Verification
    - Machine Resource Management
    - Feature Extraction
    - Analysis Tools
    - Process Management Tools
- Serving Infrastructure
- Monitoring

// Summary of Hidden Technical Debt of ML
- The hidden technical debt in ML refers to the Unforeseen and often Overlooked challenges and Complexities that arise as ML models are deployed and maintained in Real-world applications.

- This debt can accumulate due to various factors, such as Data Quality issues, Model Performance degradation, Changing environments, and Evolving business requirements.

- It highlights the need for ongoing monitoring, maintenance, and adaptation of ML systems to ensure they Continue to perform effectively and meet their intended objectives.

- Addressing this hidden technical debt is crucial to avoid Unexpected issues and maintain the reliability of ML solutions Over time.

// ML System Behavior

- Data (ML Context): The Performance of a ML system is heavily influenced by both the dataset used for Training the model and the Ongoing data input it receives during production.

- Model (ML Context): In ML, the model is the result of applying a ML algorithm to a dataset. It encapsulates the knowledge gained by the algorithm. It's beneficial to perceive the model as a comprehensive Pipeline, comprising all the necessary steps for managing data flow into and out of the model.

- Code: To construct the ML Pipeline and specify the model Configurations (hyperparameters) for Training, Testing, and Evaluating models, Code is an essential component.

// Challenges in ML Systems

- It's NOT as simple as saying – We have 3 Additional Dimensions on dataset when building ML Model.

- Code and Configuration – introduces further Complexity and Sensitivity into ML system due to Entanglements & Configurations.

- Entanglements: Changes in Input data distributions can significantly affect a model's accuracy and lead to shifts in its predictions, emphasizing the importance of thorough testing for feature engineering and selection code to account for these effects.

- Configurations: Flaws in a model's configuration, including Hyperparameters, Versions, and Features, can dramatically alter the system's behavior. Importantly, such issues may go unnoticed in traditional software testing, allowing a ML system to generate valid yet incorrect outputs without raising exceptions.

### Challenge - Who Owns what (Stakeholders)?

#### From Data Scientists Perspective!!

- Focus on functional objectives, including changes in Input data, the Model, and Model Predictions.

- Monitoring functional objectives entails Visibility into Data Input, Model Metrics, and understanding the Model's Predictions.

- Model Accuracy in a production environment is a primary concern for data scientists.

- Real-time Access to true labels is ideal for insight but is NOT always Available.

- Data scientists often use Proxy values to gain Visibility into their models in the Absence of Real-time true labels.

#### DevOps Engineer’s Perspective

- Engineers are tasked with achieving operational objectives to maintain the health of ML system resources.

- This involves monitoring standard software application metrics, a common practice in traditional software development.

- Examples metrics: 
  - Latency
  - IO/memory/disk usage
  - System reliability (uptime)
  - Auditability

#### Best Practice!!

- Effective Monitoring of ML systems incorporates both data scientist and DevOps engineer perspectives.

- A comprehensive understanding of the system is essential for success.

- Collaboration among all Stakeholders is crucial to establish Clear and Consistent definitions of terms, fostering Effective Communication within the team.

### Functional Level Monitoring
2 levels of monitoring
- Functional: Input, Model, and Output Prediction (Data Scientist)
- Operational: System Performance, Pipeline, and Costs (DevOps)

#### Functional Level Monitoring – Input Data
- Models rely on the Input data they receive, and Unexpected inputs can lead to model breakage. 

- Monitoring Input data is essential for detecting functional Performance issues before they affect the ML system.

- Key items to monitor from an Input data perspective include:
  - Data quality: Validate production data to ensure data integrity and equivalence of data types, addressing issues like schema changes or data loss. (pydantic to validate Input data or OAS schema)

  - Data drift: Monitor changes in data distribution between Training data and production data, detecting shifts in statistical properties of feature values Over time.

- Real-world data is constantly Changing, and as Behavior and Business context evolve, it may be necessary to update the ML model.

#### Functional Level Monitoring – The Model
- The core of a ML system is the ML model, which must consistently perform above a certain threshold to deliver business value.

- Ongoing monitoring is required to address factors that can impact the model's Performance, including model drift and version management.
    - Model drift is the decline in a model's predictive accuracy caused by changes in the Real-world environment, and it should be detected using statistical tests and monitored for predictive Performance Over time.

    - Tracking versions is crucial to ensure the correct model is in production, involving the management of version history and prediction records.

#### Functional Level Monitoring – The Output
- Understanding the Performance of a ML model in production entails monitoring its output, ensuring it aligns with key Performance metrics.

- Ground truth: In cases where ground truth labels are available, such as in ad click prediction, model predictions can be compared directly to the actual outcomes to assess Performance.
    - However, evaluating model predictions against ground truth is challenging in most ML scenarios, necessitating alternative methods.

- Prediction drift: When ground truth labels are unavailable, monitoring predictions is crucial. A significant shift in prediction distribution can indicate potential issues, like changes in Input data structure, system misbehavior, or shifts in the Real-world environment, as seen in fraud detection with a sudden Increase in flagged Transactions.

### Model Drift
Drift in ML

- Model Drift is a scenario where ML Models is NOT performing as per the SLA (Service Level Agreement). 
- Model Performance degrade after deploying it to production, as the model can receive data that was NOT introduced during model training.

3 Types of Drift in ML:

- Data Drift
- Prediction Drift
- Concept Shift

#### Data Drift

- Data drift, also known as feature drift, population drift, or covariate shift, occurs when the distribution or characteristics of input features change in relation to the Training data. (模型训练和实际应用过程中，数据输入特征的分布发生了变化 例如年齡分布改變等)

- Such changes can affect model predictions because the model isn't prepared for the new data distribution.

- For example, if a new category is introduced as a feature post-deployment, it can lead to prediction errors since the model wasn't trained with this category.

- Changes in critical features, like Credit Rating, can substantially impact the model output. For instance, switching from S&P to Moody's credit rating alters the Input data distribution, affecting model Performance.

In summary, data drift highlights the importance of ensuring that the distribution of Training data matches the distribution of reference (production) data to maintain model accuracy.

#### Prediction Drift
- Data drift can lead to changes in the target or prediction variable Over time, resulting in Prediction drift.

- Prediction drift is also known as Prior probability shift, Label drift, or Unconditional class shift.

- It can occur due to the removal or addition of new classes in the data.

- Retraining the model is a strategy to mitigate the impact of Prediction drift on model Performance.

In summary, Prediction drift signifies changes in predictions as Input data evolves, and it can be addressed through model retraining to maintain accuracy.

#### Concept Shift
- Concept shift, also called Posterior class shift, Conditional change, or Real concept drift, occurs when the relationship between independent variables and dependent variables changes.

- It involves alterations in the connection between input and target variables.

- Significant Concept shifts can lead to unreliable model predictions.

- The concept in Concept shift refers to the relationship between independent and dependent variables.

For Example, changes in a car insurance company's claim policy can result in a Concept shift, where the mapping between input features and target features changes, even if the Input data distribution remains the same.

1. 車險理賠政策變更
2. 信用評級變更
3. 新的類別特徵
4. 消費者行為的變化

#### Techniques to detect drift in ML
- Statistical Distance metrics are valuable for detecting drift in ML.

- For datasets with numerous independent variables, dimensionality reduction techniques like PCA can be employed.

- Monitoring many features can strain the system, making it challenging to address drift by focusing on specific features.

- Basic statistical metrics such as Mean, Standard deviation, Correlation, and Comparisons of minimum and maximum values can gauge drift between training and current independent variables.

- Distance measures like Population Stability Index (PSI), Characteristic Stability Index (CSI), Kullback–Leibler divergence (KL-Divergence), Jensen–Shannon divergence (JS-Divergence), and Kolmogorov-Smirnov (KS) statistics are suitable for continuous features when assessing drift.

- Cardinality Checks, Chi-Squared Test, and Entropy can be used for Categorical variables

- Control Charts and Histogram intersections can be used to detect a drift in data

- Use the Platforms like WhyLabs, and libraries like DeepChecks, and Alibi Detect, which comes with easy integrations, and a ready framework for drift detection

####　Addressing the Drift Issues

1. Data quality issues can be resolved if there are problems with Input data. For example, transitioning from high-resolution training images to low-resolution deployment images can be addressed.

2. Retraining the model is a strategy to enhance its Performance after detecting data or concept shifts.

3. When production data is insufficient for training, you can combine historical data with recent production data, giving more weight to recent information.

4. Four strategies for retraining the model include 
    - Periodic retraining at scheduled times, 
    - Event-driven retraining when new data becomes available, 
    - Model or metric-driven retraining based on accuracy or SLA thresholds, and 
    - Online learning for continuous Real-time or near Real-time model improvement.

5. If retraining doesn't yield satisfactory results, rebuilding or tuning the model on recent data may be necessary, and this process can be automated using a Pipeline.

### Operational Level Monitoring
Operational Level Monitoring – The System Performance
1. Continuous monitoring of the ML model within the application stack is essential to stay informed about its performance.

2. Problems in this context can have wide-ranging effects on the entire system.

3. System performance metrics that offer insights into model performance encompass:
   - Memory usage
   - Latency
   - CPU/GPU utilization

Operational Level Monitoring – The Pipelines
1. Essential Pipelines for monitoring in ML are the Data Pipeline and the Model Pipeline.

2. Neglecting Data Pipeline monitoring can result in data quality problems that disrupt the system.

3. For the Model Pipeline, it's vital to track and monitor factors that could lead to model failure in production, including dependencies and associated issues.

Operational Level Monitoring – The Costs
1. ML involves financial costs spanning from data storage to model training.

2. While ML can deliver substantial value, it can also become expensive, making continuous cost monitoring crucial.

3. Setting Budgets through Cloud vendors like AWS or GCP, with bill and spending tracking, allows for timely alerts when Budgets are exceeded.

4. For on-premises ML applications, monitoring system usage and cost provides insight into cost breakdown and potential cost-cutting measures.

### Tools and Best Practices of ML Model Monitoring
#### Best Practices for Machine Learning Model Monitoring

1. Monitoring starts during model development and is NOT limited to the deployment phase.

2. Tracking and monitoring metrics and logs are essential throughout the iterative process of building a ML model.

3. Sudden major performance degradation in a model is a red flag, requiring immediate investigation.

4. Teams should establish a troubleshooting framework to guide them from alert to resolution during model maintenance.

5. A well-defined plan of action is crucial for responding to system failures, ensuring a prompt transition from alert to problem-solving and effective model maintenance.

#### Monitoring Tools
Monitoring the performance of ML (ML) models is crucial for ensuring that models continue to perform well over time, particularly in production environments. Here are some common tools and frameworks that are used for ML performance monitoring:

MAJOR TOOLS
1. Prometheus
  - Type: Open-source monitoring and alerting toolkit.
  - Use Case: Tracks and stores metrics over time, which can be used to monitor system metrics, model inference latency, and throughput.
  - Features: Time series database, flexible query language, and alerting capabilities.
  - Integration: Can be integrated with Grafana for powerful visualization and alerting.

2. Grafana
  - Type: Open-source analytics and monitoring Platform.
  - Use Case: Visualizes data from Prometheus, InfluxDB, and other sources to create dashboards for monitoring ML model performance.
  - Features: Customizable dashboards, alerting, and support for multiple data sources.
  - Integration: Works seamlessly with Prometheus and other metrics sources.

3. WhyLabs (WhyLogs)
   - Type: AI observability Platform.
   - Use Case: Monitors data and model drift, data quality issues, and provides automated reports.
   - Features: Real-time monitoring, drift detection, anomaly detection, and integration with existing ML pipelines.

OTHERS TOOLS
4. Alibi Detect
  - Type: Open-source Python library.
  - Use Case: Detects outliers, adversarial instances, and concept drift in ML models.
  - Features: Drift detection methods (like KS Test, Chi-Square Test), outlier detection, and metrics for evaluating performance.
5. DeepChecks
  - Type: Open-source Python library.
  - Use Case: Performs checks on data and models, including model evaluation and validation for ML models.
  - Features: Pre-built checks for data validation, model drift detection, and performance degradation.
  - Integration: Can be integrated with CI/CD pipelines to automate monitoring.
6. Evidently
  - Type: Open-source Python library.
  - Use Case: Analyzes and monitors ML models in production, particularly focused on detecting model drift.
  - Features: Data drift detection, visualization, and reporting tools.
  - Integration: Works well in Jupyter Notebooks and production monitoring setups.
7. Seldon Deploy
  - Type: MLOps Platform.
  - Use Case: Deploys and monitors ML models in Kubernetes, with built-in metrics and monitoring tools.
  - Features: Model deployment, logging, monitoring, and scaling.
  - Integration: Integrates with Prometheus, Grafana, and other Kubernetes-native tools.
8. Neptune.ai
  - Type: Experiment tracking and model registry tool.
  - Use Case: Tracks experiments, models, and their performance metrics across the ML lifecycle.
  - Features: Custom dashboards, model monitoring, and metadata management.
  - Integration: Integrates with popular ML libraries like TensorFlow, PyTorch, and scikit-learn.
9. MLflow
  - Type: Open-source Platform for managing the ML lifecycle.
  - Use Case: Tracks experiments, deploys models, and manages model versioning.
  - Features: Experiment tracking, model registry, and support for monitoring performance over time.
  - Integration: Supports integration with various Cloud and on-premise storage solutions.
10. Kubeflow Pipelines
  - Type: Open-source Kubernetes-native Platform for orchestrating ML workflows.
  - Use Case: Automates ML workflows, including monitoring and logging.
  - Features: Workflow management, artifact tracking, and integration with Prometheus and Grafana for monitoring.
  - Integration: Runs on Kubernetes, integrates with other MLOps tools.
11. Tecton
  - Type: Feature store Platform.
  - Use Case: Manages feature pipelines and provides monitoring for data and model performance.
  - Features: Real-time feature monitoring, drift detection, and integration with existing ML infrastructure.
12. Datadog
  - Type: Cloud monitoring Platform.
  - Use Case: Monitors ML model performance, infrastructure, and application logs.
  - Features: Metrics collection, anomaly detection, and alerting.
  - Integration: Works with Cloud providers, containers, and on-premise infrastructure.
13. Azure Monitor
  - Type: Cloud-native monitoring service (part of Azure).
  - Use Case: Monitors ML models deployed on Azure, provides alerts, and tracks custom metrics.
  - Features: Application insights, log analytics, and integration with Azure ML.
  - Integration: Deep integration with Azure services.

14. AWS CloudWatch
  - Type: Cloud monitoring service (part of AWS).
  - Use Case: Monitors ML models deployed on AWS, including tracking metrics and setting up alarms.
  - Features: Log monitoring, metric tracking, and alerts.
  - Integration: Integrates with SageMaker and other AWS services.

15. Google Cloud Monitoring (formerly StackDriver)
  - Type: Cloud-native monitoring service (part of Google Cloud).
  - Use Case: Monitors ML models and infrastructure on Google Cloud Platform.
  - Features: Log-based metrics, uptime checks, and alerting.
  - Integration: Integrates with Vertex AI and other GCP services.

These tools and frameworks help ensure that your ML models remain performant, reliable, and free from issues like drift, anomalies, or infrastructure failures. Depending on your specific needs, you might choose one or a combination of these tools to monitor different aspects of your ML pipelines and deployments.
