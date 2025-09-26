
## Student Exam Performance Prediction

This is an **end-to-end Machine Learning web application** that predicts a student’s Math exam score based on details like gender, ethnicity, parental education, lunch type, test preparation course, reading and writing scores.  

The project uses **Flask, Scikit-learn, Docker, AWS (EC2 + ECR), and GitHub Actions (CI/CD)**.

## 🚀 Features
- Web app built with **Flask** and simple HTML templates  
- Predicts Math score instantly  
- Containerized with **Docker**  
- Deployed on **AWS EC2** using images from **AWS ECR**  
- Automated build & deployment with **GitHub Actions**


## ⚙️ Tech Stack
- **Backend:** Flask  
- **ML:** Scikit-learn, Pandas, NumPy  
- **Deployment:** Docker, AWS EC2, AWS ECR  
- **Server:** Gunicorn  
- **CI/CD:** GitHub Actions  


## 📂 Project Structure
```

MLPROJECT/  
│── src/                     # ML pipeline and helper modules  
│   │── pipeline/            # Training & preprocessing modules  
│   │── components/          # Reusable ML components  
│   │── utils.py             # Utility functions  
│   │── exception.py         # Custom exceptions  
│   │── logger.py            # Logging setup  
│   │── predict_pipeline.py  # ML prediction pipeline  
│  
│── templates/               # HTML files (index.html, home.html)  
│   │── index.html           # Input form page  
│   │── home.html            # Prediction results page  
│  
│── application.py           # Flask app entry point  
│── requirements.txt         # Python dependencies  
│── Dockerfile               # Docker setup  
│── .github/workflows/       # CI/CD pipeline (main.yaml)  
│   │── main.yaml            # GitHub Actions workflow  
│── README.md                # Project documentation  

```


## ▶️ Run Locally

1. Clone the repo  
```bash
git clone https://github.com/<your-username>/mlproject.git
cd mlproject
````

````
2. Create environment & install requirements

````bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
````

3. Run the app

```bash
python application.py
```

App runs at: `http://127.0.0.1:5000/`



## 🐳 Run with Docker

```bash
docker build -t studentperformance-app .
docker run -d -p 5000:5000 studentperformance-app
```

Visit: `http://localhost:5000`



## ☁️ AWS Deployment

1. Push Docker image to AWS ECR
2. Run container on AWS EC2:

```bash
docker run -d --name mltest -p 80:5000 <ECR-URI>:latest
```

App will be available at:
`http://<EC2-Public-IP>/predictdata`

---

## 📸 Screenshots

* Prediction Form
<img width="1901" height="893" alt="Screenshot 2025-09-25 185521" src="https://github.com/user-attachments/assets/4341ab99-58a0-4d41-8ebb-5a82c0d0c3ae" />


## ✅ Results

* Working ML web app deployed on AWS
* CI/CD pipeline with GitHub Actions
* Real-time predictions accessible via browser

