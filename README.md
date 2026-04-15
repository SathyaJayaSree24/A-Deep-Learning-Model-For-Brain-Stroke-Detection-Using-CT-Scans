# Brain Stroke Detection Using Deep Learning

This repository contains a Deep Learning-based solution designed to detect brain strokes from CT Scan images. By leveraging convolutional neural networks, the project aims to assist medical professionals in providing rapid and accurate diagnostic support.

## 🚀 Features
- **Deep Learning Model**: A trained model optimized for classifying stroke vs. non-stroke CT scans.
- **Streamlit Web App**: An interactive user interface for uploading images and viewing real-time predictions.
- **Containerized Environment**: Fully Dockerized for easy deployment and consistency across different environments.
- **Automated Workflow**: Includes a `Makefile` for common tasks and pre-commit hooks for code quality.

## 📁 Project Structure
```text
├── app.py                # Streamlit web application
├── train.py              # Script to train the Deep Learning model
├── predict.py            # Inference logic for single/batch images
├── notebook.ipynb        # Exploratory Data Analysis and Model Development
├── Dockerfile            # Docker configuration for the app
├── docker-compose.yml    # Multi-container orchestration
├── Pipfile & .lock       # Python dependency management (Pipenv)
└── Makefile              # Shortcut commands for setup and execution
