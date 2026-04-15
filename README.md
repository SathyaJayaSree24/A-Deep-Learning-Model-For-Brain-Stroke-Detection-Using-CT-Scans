Brain Stroke Detection Using Deep Learning
This repository contains a Deep Learning-based solution designed to detect brain strokes from CT Scan images. By leveraging convolutional neural networks, the project aims to assist medical professionals in providing rapid and accurate diagnostic support.

🚀 Features
Deep Learning Model: A trained model optimized for classifying stroke vs. non-stroke CT scans.

Streamlit Web App: An interactive user interface for uploading images and viewing real-time predictions.

Containerized Environment: Fully Dockerized for easy deployment and consistency across different environments.

Automated Workflow: Includes a Makefile for common tasks and pre-commit hooks for code quality.

📁 Project Structure
Plaintext
├── app.py                # Streamlit web application
├── train.py              # Script to train the Deep Learning model
├── predict.py            # Inference logic for single/batch images
├── notebook.ipynb        # Exploratory Data Analysis and Model Development
├── Dockerfile            # Docker configuration for the app
├── docker-compose.yml    # Multi-container orchestration
├── Pipfile & .lock       # Python dependency management (Pipenv)
└── Makefile              # Shortcut commands for setup and execution
🛠️ Installation & Setup
Prerequisites
Python 3.9+

Pipenv (Optional, but recommended)

Docker (For containerized execution)

Local Development
Clone the Repository:

Bash
git clone https://github.com/SathyaJayaSree24/A-Deep-Learning-Model-For-Brain-Stroke-Detection-Using-CT-Scans.git
cd A-Deep-Learning-Model-For-Brain-Stroke-Detection-Using-CT-Scans
Install Dependencies:
Using Pipenv:

Bash
pipenv install
Or using pip:

Bash
pip install -r requirements.txt
Run the Streamlit App:

Bash
python -m streamlit run app.py
Running with Docker
To build and run the application using Docker, simply use:

Bash
docker-compose up --build
The app will be accessible at http://localhost:8501.

🧠 Model & Training
The model is developed using deep learning frameworks (TensorFlow/Keras or PyTorch). You can find the experimental results and layer architecture in notebook.ipynb.

To retrain the model, run: python train.py

To test the inference script directly: python predict.py

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any suggestions or bug reports.
