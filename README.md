# 🚀 Epass: Digital Personal Wallet
 
**A digital ID/passport manager with fines, visas, and border stamp features built using PyQt5 and FastAPI.**

---

## ⚙️ Features

- View and manage private documents digitaly
- Pay fines issued by authorities
- Get and track visas and stamps
- Built with `PyQt5` and `FastAPI`

---

## 🛠️ Tech Stack

- 🖥️ Frontend: PyQt5
- ⚙️ Backend: FastAPI
- 🗃️ Database: SQLite
- 🔐 Auth: JWT token-based authentication

---

## 🧩 Installation

### 🧬 Clone the repo and set up env
```bash
git clone git@github.com:lazarejan/project.git
cd project
setup.bat

```

### 🔄 Alternative: Download the ZIP

If you don't have Git installed:

1. Go to the repository: https://github.com/lazarejan/project
2. Click **"Code" > "Download ZIP"**
3. Extract the ZIP and open the folder
4. Double-click or run `setup.bat`

---

### ▶️ Run Backend API

Once setup is complete and the virtual environment is activated, start the FastAPI backend server by running:

```bash
uvicorn api.main_api:app --reload

```