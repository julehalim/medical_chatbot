# 🩺 Medical Chatbot

A lightweight medical information chatbot built with **FastAPI**, **Azure OpenAI (via Azure AI Foundry)**, and **Docker** — deployed on **Render**.

⚠️ **Disclaimer:**  
This chatbot does *not* diagnose or provide medical treatment. It only gives general health-related information and always recommends consulting a qualified healthcare professional.

---

## 🚀 Features

- 💬 Uses **Azure OpenAI GPT-4o** through a secure deployment on Azure AI Foundry.
- ⚡ FastAPI backend serving a minimal HTML + JavaScript chat interface.
- 📦 Containerized with **Docker** for portability and easy deployment.
- 🌐 Hosted live on **Render**, with secure environment-based authentication.

---

## 🌐 Live deployment

🔗 [Visit the chatbot on Render]([https://your-render-url.onrender.com](https://medical-chatbot-7jx3.onrender.com))  

---

## 🖼️ Screenshot

![Chatbot Screenshot](./screenshot.png)

---

## 🔧 Running locally

### 1️⃣ Clone the repo

```bash
git clone https://github.com/yourusername/medical-chatbot.git
cd medical-chatbot
```

### 2️⃣ Build & run with Docker

```bash
docker build -t medical-chatbot .
docker run -p 8000:8000 \
  -e AZURE_CLIENT_ID=your-client-id \
  -e AZURE_TENANT_ID=your-tenant-id \
  -e AZURE_CLIENT_SECRET=your-client-secret \
  medical-chatbot
```

Then visit: [http://localhost:8000](http://localhost:8000)

---

## ⚙️ Tech stack

- **FastAPI** for the backend API
- **Azure OpenAI (GPT-4o)** via Azure AI Foundry
- **HTML / JavaScript** chat UI
- **Docker** for containerization
- **Render** for live cloud hosting

---

## 🌍 Deploying on Render

1. Push this project to a GitHub repository.
2. Create a **new Web Service** on [Render](https://render.com).
3. Connect your GitHub repo.
4. In the Render dashboard, set these **Environment Variables**:
    - `AZURE_CLIENT_ID`
    - `AZURE_TENANT_ID`
    - `AZURE_CLIENT_SECRET`
5. Deploy — Render will build your Docker container and start serving your app.

---

## ✍️ License

MIT

---

### ✅ Notes

- This project uses **Microsoft Entra ID (formerly Azure Active Directory)** for secure credential management.  
- All medical content is informational only.

---

📌 **Questions or improvements?**  
Open an issue or submit a PR!
