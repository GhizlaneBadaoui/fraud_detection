# Fraud Detection Application

## Overview
This repository hosts the code for a state-of-the-art Fraud Detection Application. Our application leverages machine learning, a Flask backend, Instagram API integration, and a user-friendly interface to identify and flag fraudulent activities effectively.

## Branch Structure
This repository is organized into multiple branches, each focusing on a specific aspect of the application:

1. **main**: The primary branch that integrates features from other branches and hosts the final, deployable version of the application.
2. **MLflask**: This branch is dedicated to integrating the machine learning model with a Flask backend. It contains code for model serving and API endpoints.
3. **Prediction**: Here, you'll find the development of our machine learning model used for fraud detection.
4. **instagramAPI**: This branch focuses on integrating the Instagram API to fetch and analyze user data for fraud detection.
5. **userInterface**: Contains the code for the application's frontend, ensuring a seamless and intuitive user experience.

## Getting Started

### Prerequisites
- Python 3.8+
- Pip (Python package installer)
- Access to Instagram API (for the `instagramAPI` branch)
- CORS

### Installation
Clone the repository and navigate to the branch you're interested in. For example, to work on the ML Flask integration:
```bash
git clone https://github.com/yourusername/fraud-detection-app.git
cd fraud-detection-app
git checkout MLflask
