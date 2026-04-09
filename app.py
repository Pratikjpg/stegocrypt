from flask import Flask, request, jsonify, send_file, render_template
from stego import hide_message, reveal_message
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hide', methods=['POST'])
def hide():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded!'}), 400

    image = request.files['image']
    message = request.form.get('message', '').strip()

    if not message:
        return jsonify({'error': 'Please enter a secret message!'}), 400

    try:
        image_bytes = image.read()
        output = hide_message(image_bytes, message)
        return send_file(
            output,
            mimetype='image/png',
            as_attachment=True,
            download_name='secret_image.png'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reveal', methods=['POST'])
def reveal():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded!'}), 400

    image = request.files['image']

    try:
        image_bytes = image.read()
        message = reveal_message(image_bytes)
        return jsonify({'message': message})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)