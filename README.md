# 🔐 StegoCrypt

**Image Steganography Web Application** — Hide secret messages inside images, completely invisible to the naked eye.

---

## 📖 About

StegoCrypt is a Flask-based web application that uses **LSB (Least Significant Bit) Steganography** to embed hidden text messages into PNG images. The changes to the image are imperceptible, making it a fun and practical tool for covert communication.

---

## ✨ Features

- 🔒 **Hide Messages** — Embed any secret text into an image file
- 🔓 **Reveal Messages** — Extract hidden text from a steganographic image
- 🖼️ **Image Preview** — Preview uploaded images before processing
- 📥 **Auto Download** — Automatically downloads the output image after hiding
- 🌐 **Web UI** — Clean, dark-themed browser interface, no installation needed for the user

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| Steganography | Pillow (PIL) — LSB encoding |
| Frontend | HTML, CSS, Vanilla JavaScript |

---

## 📁 Project Structure

```
stegocrypt/
├── app.py              # Flask routes: /hide and /reveal
├── stego.py            # Core LSB steganography logic
└── templates/
    └── index.html      # Frontend UI
```

---

## ⚙️ How It Works

### Hiding a Message
1. The message is wrapped with a header/footer marker: `STEGO>>>message<<<STEGO`
2. It's encoded to bytes with a 4-byte length prefix
3. Each bit of the payload is stored in the **Least Significant Bit** of R, G, B channels of each pixel
4. The modified image is saved and returned as a PNG

### Revealing a Message
1. LSBs are extracted from each pixel channel
2. Bytes are reassembled and the length prefix is read
3. The marker (`STEGO>>>` / `<<<STEGO`) is used to validate and extract the original message

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Pratikjpg/stegocrypt.git
cd stegocrypt

# Install dependencies
pip install flask pillow

# Run the app
python app.py
```

Then open your browser and go to: `http://127.0.0.1:5000`

---

## 🖥️ Usage

### Hide a Message
1. Go to the **Hide Message** tab
2. Upload any PNG/JPG image
3. Type your secret message
4. Click **Hide & Download Image** — a new PNG with your message embedded will be downloaded

### Reveal a Message
1. Go to the **Reveal Message** tab
2. Upload an image that was previously processed by StegoCrypt
3. Click **Reveal Secret Message** — the hidden text will be displayed

---

## ⚠️ Limitations

- The output image is always saved as **PNG** (lossless) — JPEG re-encoding would destroy the hidden bits
- Message size is limited by image resolution (more pixels = more capacity)
- Only works with images encoded using StegoCrypt (uses custom markers for validation)

---

## 📜 License

This project is open source. Feel free to use, modify, and distribute.

---

## 👤 Author

**Pratikjpg** — [github.com/Pratikjpg/stegocrypt](https://github.com/Pratikjpg/stegocrypt)
