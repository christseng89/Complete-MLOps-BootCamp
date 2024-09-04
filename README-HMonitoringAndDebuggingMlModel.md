# Monitoring and Debugging ML Models

### Why Monitoring Machine Learning Models is Important
// Importance of Monitoring

- Machine learning models are now more frequently employed for critical real-world tasks, ranging from the detection of fraudulent activities to the implementation of automated braking systems in vehicles.

- The responsibilities of ML professionals extend well beyond the deployment of a model into a production environment.

- It is important to constantly oversee the performance of these models to guarantee their continued effectiveness when confronted with real-world scenarios.

- Nevertheless, merely adopting 'conventional software monitoring' practices falls short of what's necessary in the context of ML systems. 采用传统的软件监控实践在机器学习系统的背景下是不够的。

// Questions to think
- How do we monitor effectively?
- What metrics to choose?
- What tools are available?

### What is Monitoring of ML models & When to Update Model in Production
// Monitoring of Machine Learning Models

- It's important to note that monitoring is NOT a one-time task that can be completed and then forgotten.
- Monitoring entails the ongoing process of observing a deployed model's behavior to assess its 'Performance'.
- Post-deployment monitoring is crucial because ML models can deteriorate and malfunction when in active use.

// When to Update the Model in Production?

- To determine the appropriate moment for updating a model in a production environment, it's essential to maintain a real-time perspective that enables stakeholders to Continuously evaluate the model's Performance within the live setting.
- This continuous assessment ensures that the model is operating as anticipated.
- Achieving 'Maximum Visibility' into your deployed model is a necessity for identifying potential issues and their origins before they have a detrimental impact on the business.

### Why Monitoring Machine Learning Models is Difficult
// Hidden Technical Debt of Machine Learning

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

// Summary of Hidden Technical Debt of Machine Learning
- The hidden technical debt in ML refers to the Unforeseen and often Overlooked challenges and Complexities that arise as ML models are deployed and maintained in real-world applications.

- This debt can accumulate due to various factors, such as Data Quality issues, Model Performance degradation, Changing environments, and Evolving business requirements.

- It highlights the need for ongoing monitoring, maintenance, and adaptation of ML systems to ensure they Continue to perform effectively and meet their intended objectives.

- Addressing this hidden technical debt is crucial to avoid Unexpected issues and maintain the reliability of ML solutions over time.

// Machine Learning System Behavior

- Data (Machine Learning Context): The performance of a ML system is heavily influenced by both the dataset used for Training the model and the Ongoing data input it receives during production.

- Model (Machine Learning Context): In ML, the model is the result of applying a ML algorithm to a dataset. It encapsulates the knowledge gained by the algorithm. It's beneficial to perceive the model as a comprehensive pipeline, comprising all the necessary steps for managing data flow into and out of the model.

- Code: To construct the ML Pipeline and specify the model Configurations (hyperparameters) for Training, Testing, and Evaluating models, Code is an essential component.

// Challenges in Machine Learning Systems

- It's not as simple as saying – We have 3 Additional Dimensions on dataset when building ML Model.

- Code and Configuration – introduces further Complexity and Sensitivity into ML system due to Entanglements & Configurations.

- Entanglements: Changes in input data distributions can significantly affect a model's accuracy and lead to shifts in its predictions, emphasizing the importance of thorough testing for feature engineering and selection code to account for these effects.

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
