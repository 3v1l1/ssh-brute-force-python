# 🔐 SSH Brute Force Detection using Python

## 📌 Overview

This project detects SSH brute force attacks by analyzing Linux authentication logs. It identifies patterns where multiple failed login attempts are followed by a successful login from the same IP address.

---

## 🎯 Objective

Detect suspicious login behavior:
FAILED → FAILED → FAILED → SUCCESS

---

## ⚙️ How It Works

* Parses SSH logs (`auth.log`)
* Extracts failed and successful login attempts
* Tracks attempts per IP address
* Triggers alert when:

  * ≥ 3 failed attempts
  * Followed by a successful login

---

## 🚨 Sample Output

![Detection Output](output.png)

---

## 🛠️ Technologies Used

* Python
* Regex (log parsing)
* Linux SSH logs

---

## 📂 Project Structure

```
ssh-brute-force-python/
│── detect_bruteforce.py
│── ssh_logs.txt
│── screenshots/
│   └── output.png
│── README.md
```

---

## 🧠 Key Concepts Demonstrated

* Log analysis
* Event correlation
* Threat detection logic
* Security monitoring

---

## 🔥 Why This Project Matters

This project simulates real SOC (Security Operations Center) workflows where analysts detect brute-force attacks using log data.

---

## 🚀 Future Improvements

* Export alerts to CSV
* Add severity levels
* Real-time monitoring
