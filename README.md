
# Battery Health Monitoring and Risk Notification System 🚗🔋

This project implements a **Battery Health Monitoring System** that predicts the health status of vehicle batteries, provides a risk classification, and integrates real-time data pipelines with Google Cloud Services for notification and visualization.

---


## **Architecture Overview**
![image](https://github.com/user-attachments/assets/f1386001-7f68-4a50-b55d-5e0561923c92)

The system architecture is as follows:

1. **Data Collection**:
   - **Input**: Battery data from a local computer in JSON format.
   - **Parameters**: `state of charge`, `cycle count`, `temperature`, `voltage`, `current`, and `health status`.

2. **Data Pipeline**:
   - Data is sent to **Google Cloud Pub/Sub** for real-time processing.
   - Data is ingested into **Google BigQuery** for storage and analysis using Python BigQuery Client.

3. **Machine Learning Model**:
   - A classification model built with **Scikit-learn** is used to predict battery health (`mid`, `risk`, etc.).
   - Deployed using **Google Cloud Run** with a **Docker** container.

4. **Visualization**:
   - A **Looker Studio Dashboard** is used to visualize battery performance, health, and risk levels.

5. **Risk Notification**:
   - Notifications for risky battery statuses are handled by **Google Cloud Functions**.
   - Notifications currently log in the GCP console (can be extended to third-party email/SMS services).

---

## **System Workflow**

1. **Battery Data Ingestion**:
   - JSON format example:
     ```json
     {
       "timestamp": "2024-09-21 11:48:00",
       "vehicleid": 1,
       "voltage": 400.5,
       "current": 150.0,
       "temperature": 25.3,
       "stateofcharge": 85.0,
       "poweroutput": 75.0
     }
     ```

2. **Cloud Pub/Sub**:
   - Streams data from the local system to Google Cloud.

3. **BigQuery and Python Client**:
   - Processes and stores battery data.
   - Enables querying for model predictions and analytics.

4. **ML Model Deployment**:
   - Predicts health status and risk levels.
   - Model containerized using Docker and deployed on **Google Cloud Run**.

5. **Visualization and Dashboard**:
   - Google BigQuery provides data to **Looker Studio** for creating interactive dashboards.

6. **Risk Notifications**:
   - Triggers alerts using **Google Cloud Functions** based on risk thresholds.

---

## **Technologies Used**

- **Google Cloud Services**:
  - Pub/Sub, BigQuery, Cloud Run, Cloud Functions.
- **Machine Learning**:
  - Scikit-learn.
- **Containerization and Deployment**:
  - Docker.
- **Data Visualization**:
  - Looker Studio.
- **Programming Language**:
  - Python.

---

## **Features**

- **Real-time Data Processing**: Seamless ingestion of live battery data.
- **Health Classification**: Predicts battery status using ML models.
- **Risk Alerts**: Notifies potential issues (expandable to third-party services).
- **Interactive Dashboards**: Visual insights for battery performance and health trends.
- **Scalable Deployment**: Containerized application for flexible deployment.

---

## **Setup and Installation**

### **Pre-requisites**
1. Python 3.8 or above.
2. Docker installed on your system.
3. Google Cloud account with the following enabled:
   - Pub/Sub
   - BigQuery
   - Cloud Run
   - Cloud Functions



## **Future Enhancements**

- Integration with third-party notification services (email/SMS).
- Advanced analytics using AI/ML models.
- Support for additional IoT data sources.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## **Contributors**

- **Your Name** - Developer and Architect.
- Open for contributions! Feel free to create a pull request.

---

Happy Monitoring! 🚀
