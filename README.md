# 🔐 StegoCrypt — Image Steganography Tool

> Hide secret messages inside images — completely invisible to the naked eye.

🌐 **Live Site:** [stegocrypt.pythonanywhere.com](https://stegocrypt.pythonanywhere.com)

---

## ✨ About

StegoCrypt is a Flask-based web application that uses **LSB (Least Significant Bit) Steganography** to embed hidden text messages into PNG images. The pixel-level changes are imperceptible to the human eye, making it a practical tool for covert communication and cybersecurity demonstrations.

---

## 🚀 Features

- 🔒 **Hide Messages** — Embed any secret text into an image file
- 🔓 **Reveal Messages** — Extract hidden text from a StegoCrypt-encoded image
- 🖼️ **Image Preview** — Preview uploaded images before processing
- 📥 **Auto Download** — Automatically downloads the output image after hiding
- 🌐 **Web UI** — Clean, dark-themed browser interface, no installation needed

---

## 🧱 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core logic |
| Flask | Web framework |
| Pillow (PIL) | Image processing |
| HTML/CSS/JS | Frontend UI |
| PythonAnywhere | Deployment & hosting |

---

## 🔬 How It Works

1. **Hide:** Each character of the message is converted to binary. The least significant bit of each RGB channel in every pixel is replaced with one bit of the message — making the change invisible.
2. **Reveal:** The LSBs are extracted from each pixel channel, reconstructed into bytes, and decoded back to the original message using custom `STEGO>>>` / `<<<STEGO` markers for integrity verification.

---

## 📁 Project Structure

```
StegoCrypt/
├── app.py          # Flask routes (hide & reveal endpoints)
├── stego.py        # LSB steganography logic
└── templates/
    └── index.html  # Frontend UI
```

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/Pratikjpg/stegocrypt.git
cd stegocrypt

# Install dependencies
pip install flask pillow

# Run the app
python app.py
```

Open [http://localhost:5000](http://localhost:5000)

---

## 📬 Contact

**Pratik Jani** — Cybersecurity Enthusiast  
🔗 [LinkedIn](https://linkedin.com/in/pratik-jani-246178316003aaa12aaa) · 🐙 [GitHub](https://github.com/Pratikjpg) · 🌐 [Portfolio](https://portfolioo1-one.vercel.app)

---

*Built with 🐍 Python + Flask & pixel-level stealth.*
