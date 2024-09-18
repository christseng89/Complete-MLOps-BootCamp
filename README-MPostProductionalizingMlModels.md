# Post Productionalizing ML Models

### Post-Productionalizing ML Models - What Next?
// Learning Journey
- Packaged ML Models
- Build & Test the ML Package using various tools
- Deploy the ML Models
- Monitor the ML Models
- Learnt the various ways of creating the ML Application

// Important Part - Keys to success
- Getting the Business Value out of the ML Models
- Security of ML models

// Building the Gap Between ML Models and Business Value
- Business users utilize ML model predictions for strategic decision making
- High accuracy of ML models does not necessarily mean high business value
- Bridging the gap between ML models and business value is crucial
- Data scientists must translate the ML model predictions into business actionable insights
- Classification models can be optimized by organizing results into ranked probability-based categories
- After deploying the ML models, ensuring its benefit to the business is crucial through monitoring and optimization MLOps practices.
- Obtaining feedback from stakeholders helps refine the model's performance in a production environment.
- Adjusting models based on user feedback enhances their utility for business users.
- Data scientists should communicate the ML model's functionality and limitations to business users at a high level.
- Building trust in the model outputs is important, especially for business users who may not understand the technical aspects of the model.
- Providing output in a readable from, such as through dashboards or chatbot, is preferred by business users and customers.
- Business intelligence tools like Tableau, Power BI, and Looker can be used to visualize the ML model outputs and create interactive dashboards.

### Model Security
- Security is a critical aspect of ML models.
- Data privacy and security are important for protecting sensitive information.
- Data encryption and secure data storage are essential for protecting data.
- Attacks can be launched against ML models to access sensitive data, at different stages of the ML model lifecycle (from development to production).

// Terms related to model security include
- Poisoning: Introducing malicious data during Training to alter the model output.
- Extraction: Building a new model mirroring the targeted model's functionality.
- Evasion: Trying to manipulate the label to a specific class through minor input variations.
- Inference: Determining if a particular dataset was part of the training data.
- Inversion: Extracting information about training data from the trained model by reverse engineering.

与模型安全相关的术语包括：
- 中毒攻击（Poisoning）： 在训练期间引入恶意数据以改变模型输出。 Training Stage
- 提取攻击（Extraction）： 构建一个新模型，模仿目标模型的功能。 Production Stage
- 规避攻击（Evasion）： 通过细微的输入变化，尝试操纵标签到特定类别。Example: 绕过垃圾邮件过滤器 Protection Stage
- 推断攻击（Inference）： 判断某个特定数据集是否是训练数据的一部分。Example: 黑客通过生成与'目标用户'特征相似的输入数据与模型交互。Production Stage
- 反转攻击（Inversion）： 通过逆向工程从训练后的模型中提取有关训练数据的信息。Example: 从模型输出中重构图像 Production Stage

### Adversarial Attack - Production Stage
- Hostile data input generation is a technique employed by attackers.
- Attackers deliberately supply malicious data to the model to induce inaccurate predictions.
- This intentional introduction of hostile data disrupts the model's prediction accuracy as it adapts to new patterns.
- The impact of this attack is significant, as even slight alterations in input data can lead to substantial changes in model predictions.
- Despite appearing normal to humans, the malicious input data adversely affects the model's learning process and subsequent predictions.

Example: 熊猫图片添加了极小的对抗性扰动后，模型将这张熊猫图片错误地分类为长臂猿，尽管扰动的幅度如此之小，以至于人类无法察觉图片的任何变化。建模時，應該考慮到對抗性攻擊，以確保模型的鲁棒性。

- Targeted Attacks
    - Objective: Change the label to a specific target.
    - Method: Alter the input data source to a predefined target.
    - Resource Intensity: Demands more resources and knowledge about the model.
    - Example: Changing the label of a panda image to a gibbon.

- Non-Targeted Attacks
    - Objective: Alter the model's output without a specific target.
    - Method: Modify the label without a predefined target.
    - Resource Intensity: Requires fewer resources and knowledge about the model.
    - Example: Adding noise to a panda image to disrupt the model's classification.

// Methods for Adversarial Attacks
- Black-box Attacks
    - Processes: Attackers send input data to the model and observe the output.
- White-box Attacks
    - Information: Attackers process comprehensive knowledge about the model's architecture and parameters including training data and feature weights.

### Data Poisoning Attack - Training Stage
- Access: Attackers gain access to the training data and introduce malicious data.
- Objective: Influence the model's learning process to produce inaccurate predictions.
- Method: Injecting malicious data into the training dataset to induce incorrect and unreliable model prediction.
- Focus: Targeted at the training data to manipulate the model's learning process for deceptive predictions.

### Distributed Denial of Service Attack (DDOS)
// Resource-intensive attacks
- Definition: Involves supplying a large volume of traffic to overwhelm the target system, prolonging the response time or rendering it unavailable.
- Implication: Limits the utility of models for users.
- Method: Attackers may introduce malware to manipulate the system or server for disruptive effects.
- Prevention: Implementing security measures like firewalls, intrusion detection systems, and secure network configurations.

### Data Privacy Attack
- Scope: Encompasses the confidentiality of Personally identifiable information (PII) and sensitive data such as Personal Health Information (PHI).
- Target: Attackers aim to access sensitive information, including details about the model or its training data.
- ML Model Vulnerability: Example, Support Vector Machine (SVM) models are susceptible to data privacy attacks due to their reliance on the support vectors for classification.
- Categories: Data privacy attacks can be classified as 
    - Model extraction, 通过向模型提供一系列输入并收集相应的输出，攻击者可以训练一个新模型，模仿原始模型的决策方式。
    - Model inversion: 一个人脸识别系统的输出可能会泄露输入的脸部特征，攻击者可以利用模型输出反向推测出用户的脸部图像。
    - Membership inference, 健康诊断模型中，攻击者可以通过向模型提交患者数据并观察输出，推测该患者的健康数据是否用于训练模型。
    - Attribute/Input inference attacks. 攻击者可以通过分析模型对不同用户的推荐内容，推断出用户的偏好、兴趣，甚至某些敏感属性（如宗教信仰或健康状况）。

### How to Mitigate Risk of Model Attacks
// ML Pipeline Security
- Secure Data Storage: Encrypting data at rest and in transit.
- Secure Data Access: Implementing access controls and authentication/authorization mechanisms.
- Secure Model Training: Ensuring the integrity of the training data and model.
- Secure Model Deployment: Monitoring model performance and access.
- Secure Model Inference: Protecting the model from adversarial attacks during inference.

// Training Phase
- Tasks: Data scientists engage in activities such as data gathering, data cleaning, feature engineering, algorithm selection, hyperparameter tuning, and model building.
- Training Phase Vulnerabilities: Attackers can exploit vulnerabilities in the phase through data poisoning, compromising the reliability of model predictions.
- Mitigation Strategies Techniques: 
    - Data encryption
    - Safeguarding the integrity of the training data
    - Employing robust statistics
    - Data sanitization
        - 移除敏感信息： 删除或屏蔽数据中包含的个人身份信息（PII），如姓名、地址、电话号码等，以防止敏感数据泄露。
        - 数据格式化： 确保数据遵循某种标准格式，便于进一步处理和分析，同时避免格式不规范带来的错误。
        - 去除冗余数据： 删除重复或无效的数据信息，以优化数据存储和处理效率。
        - 数据变形： 通过加密、哈希或其他技术，将原始数据转换为不可识别的形式，以保护数据隐私。
    - Regularly updating the model

// Tools for Model Security
- TensorFlow Privacy: A library for training machine learning models with differential privacy.
- Python libraries like CleverHans and Adversarial Robustness Toolbox (ART) for adversarial attacks.
- Features: These tools provide robustness against common ML attacks, offer support for various ML frameworks, libraries, and data types to enhance the security of ML models.
