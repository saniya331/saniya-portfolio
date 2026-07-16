# 🎓 Student Portfolio Website — Flask

A clean, modern portfolio website built with **Python Flask**, **HTML5**, and **CSS3**.

---

## 📁 Folder Structure

```
student_portfolio/
├── app.py                  ← Flask application (routes)
├── requirements.txt        ← Python dependencies
├── templates/
│   ├── index.html          ← Main portfolio page
│   └── thankyou.html       ← Thank-you page after form submit
└── static/
    ├── style.css           ← All styling
    └── resume.pdf          ← (Add your own resume PDF here)
```

---

## 🚀 How to Run

### Step 1 — Install Python
Make sure Python 3.8+ is installed:
```bash
python --version
```

### Step 2 — Create a virtual environment (recommended)
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 3 — Install Flask
```bash
pip install -r requirements.txt
```

### Step 4 — Run the app
```bash
python app.py
```

### Step 5 — Open in browser
Visit: **http://127.0.0.1:5000**

---

## ✨ Features

| Feature | Details |
|---|---|
| **Home** | Name, title, CTA buttons |
| **About** | Bio, stats (years coding, projects, certs) |
| **Skills** | 6 skill cards with animated progress bars |
| **Projects** | 3 project cards with tags & links |
| **Contact** | Form posts to `/contact` → thank-you page |
| **Download Resume** | Button links to `static/resume.pdf` |
| **Hover effects** | Cards lift, buttons animate, nav links highlight |
| **Responsive** | Mobile-friendly layout |

---

## 🎨 Customisation

1. **Change your name/title** → edit `templates/index.html` (hero section)
2. **Update skills/projects** → edit the respective sections in `index.html`
3. **Add resume** → drop your `resume.pdf` into the `static/` folder
4. **Change colours** → edit CSS variables at the top of `static/style.css`

---

## 🛠 Tech Stack

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3 (no frameworks)
- **Fonts**: Playfair Display + DM Sans (Google Fonts)
