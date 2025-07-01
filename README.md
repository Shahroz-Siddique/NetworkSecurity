### Network Security Projects for Phising Data
Built an end-to-end machine learning and deep learning-based solution to detect phishing websites as part of a network security initiative. The project focuses on identifying malicious URLs using a fully modular ML pipeline, supported by modern MLOps and deployment best practices.

###🚀 Key Contributions:
Machine Learning Models: Implemented and compared multiple classification algorithms including XGBoost, Random Forest, Decision Tree, and K-Nearest Neighbors for phishing detection.

Deep Learning Integration: Designed and trained deep learning models for advanced pattern recognition in malicious site features.

MongoDB-Based ELT Pipeline: Built an ELT workflow using MongoDB for real-time phishing data ingestion, preprocessing, and loading into ML pipeline.

Modular Architecture: Structured the system into reusable components (data ingestion, validation, transformation, training, evaluation, model pusher), each generating its own config and artifact outputs.

MLflow + Dagshub: Used MLflow for experiment tracking, parameter logging, and model registry. Integrated with Dagshub for remote version control of data and models.

Web App Deployment: Developed and deployed web applications using Flask and FastAPI, containerized with Docker, and hosted using Gunicorn.

###AWS Cloud Deployment:

Stored datasets and models in S3.

Deployed the full production pipeline on EC2 with custom environment setup.

CI/CD Automation: Implemented GitHub Actions for automated testing, model retraining, and deployment.

###📈 Outcome:
Delivered a scalable and fully automated phishing detection pipeline with high classification accuracy.

Enabled real-time phishing detection via secure API endpoints.

Built a reproducible MLOps workflow integrating data, code, and model versioning.

