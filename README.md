# Validation_id Project

A project built with **Django + Django REST Framework** to validate Egyptian National IDs with API Key Authentication and Request Throttling.

---

## 📌 Features

- **National ID Validation:**  
  Validate Egyptian National IDs (14 digits) following official structure rules.
- **API Key Authentication:**  
  Secure access using API keys (each client can have a unique key).
- **Rate Limiting / Throttling:**  
  Control the number of requests allowed per user/system over a time period.
- **Easy Integrations:**  
  Easily integrate with external systems (Web or Mobile apps).
- **Logging & Request Tracking:**  
  Each request is logged with a `Request ID` for debugging and tracking.

---

## ⚙️ Installation

```bash
git clone <repo-url>
cd Validation_id
python -m venv env
source env/bin/activate
pip install -r requirements.txt
