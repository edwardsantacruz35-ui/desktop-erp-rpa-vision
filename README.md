# 🤖 Zero-API Desktop ERP RPA Bot with Computer Vision
### Enterprise Robotic Process Automation for Legacy Desktop Financial Systems

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?style=for-the-badge&logo=python&logoColor=white)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](#)
[![RPA](https://img.shields.io/badge/RPA-PyAutoGUI-red?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#)

An enterprise-grade, autonomous Robotic Process Automation (RPA) agent engineered to register high-volume micro-transactions into legacy desktop ERP software (e.g., Galeón, Profit Plus) that lack public APIs or webhooks.

By combining **OpenCV multi-scale template matching** with **screen-level coordinate calibration** and **real-time pre-submission auditing**, this bot eliminates manual data-entry bottlenecks while guaranteeing 100% data integrity.

---

## 🎯 The Engineering Challenge

In many enterprise financial environments, critical desktop ERPs operate strictly as Windows native applications with no API access, strict licensing constraints, and custom UI components that standard OS accessibility trees fail to inspect.

Manual entry of hundreds of daily micro-transactions (e.g., FinTech installment payments, POS batches) leads to:
- Severe human data-entry fatigue and typing errors.
- Delays in order release and accounts receivable balance updates.
- Inability to scale transaction volume without hiring dedicated clerical personnel.

---

## 💡 The Solution & Architecture

```
   ┌──────────────────────┐
   │ Cloud Data Source    │ (Google Sheets / Webhook / REST API)
   └──────────┬───────────┘
              │  1. Fetch pending batch records
              ▼
   ┌──────────────────────────────────────────────┐
   │ Autonomous RPA Controller (Python)           │
   │                                              │
   │ 2. OpenCV Multi-Scale Template Matching      │
   │    -> Detect ERP window position & zoom      │
   │    -> Calibrate field coordinates            │
   │                                              │
   │ 3. Automated Safe Keystroke Injection        │
   │    -> Focus, fill Date, Ref, Amount, Ledger  │
   │                                              │
   │ 4. Computer Vision Pre-Commit Audit          │
   │    -> Read back rendered text from UI        │
   │    -> Verify (Read == Expected)              │
   │                                              │
   │ 5. Save & Capture Generated Voucher ID       │
   └──────────┬───────────────────────────────────┘
              │  6. Asynchronous cloud update callback
              ▼
   ┌──────────────────────┐
   │ Synchronized Ledger  │ (Status: Success + Generated Voucher #)
   └──────────────────────┘
```

---

## 🚀 Key Engineering Features

1. **Multi-Scale Template Matching (`cv2.matchTemplate`):**  
   Dynamically locates the target ERP window across varying screen resolutions (1080p, 2K, 4K) and DPI scaling factors (50% to 140%), calculating exact relative pixel offsets on the fly.
2. **Real-Time Pre-Submission Visual Audit:**  
   Before dispatching the save shortcut (`Ctrl + G`), the bot reads back all populated input fields from screen memory and validates them against expected payload values. If a single character or comma differs, execution halts immediately with visual diagnostic dumps.
3. **Safe Clipboard Shading & Injection:**  
   Bypasses native input mask quirks by using directional mouse drags and sanitized clipboard pasting, avoiding OS keyboard latency drops.
4. **Asynchronous Cloud Sync (Non-Blocking):**  
   Dispatches generated accounting voucher numbers back to cloud sheets via asynchronous background worker threads (`threading.Thread`), preventing UI freeze.
5. **Interactive Tkinter Command GUI:**  
   Features live logging, single-row diagnostic test mode, bulk execution, emergency abort hotkeys (`PyAutoGUI FAILSAFE`), and sound alert feedback.

---

## 🛠️ Tech Stack & Requirements

- **Python 3.10+**
- **OpenCV (`opencv-python`):** Multi-scale computer vision & image processing.
- **PyAutoGUI & PyPerClip:** Headless OS input control and clipboard buffer manipulation.
- **Tkinter & ScrolledText:** Real-time diagnostics dashboard.
- **Requests:** Asynchronous cloud REST synchronization.
- **NumPy:** Multi-dimensional matrix operations for template matching.

---

## 📦 Quickstart & Installation

```bash
# Clone the repository
git clone https://github.com/edwardsantacruz35-ui/desktop-erp-rpa-vision.git
cd desktop-erp-rpa-vision

# Install dependencies
pip install -r requirements.txt

# Run the diagnostic controller
python main.py
```

---

## 👤 Author

**Edward Santacruz**  
*Finance Automation Specialist & Analytics Engineer*  
- GitHub: [@edwardsantacruz35-ui](https://github.com/edwardsantacruz35-ui)
