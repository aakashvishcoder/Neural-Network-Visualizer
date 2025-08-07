import os
import json
import subprocess
from flask import Flask, request, render_template, url_for, send_from_directory, abort

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MANIM_SCRIPT = os.path.join(BASE_DIR, "manim", "NeuralNetwork.py")
CONFIG_PATH = os.path.join(BASE_DIR, "static", "manim", "config.json")

VIDEO_DIR = os.path.join(BASE_DIR, "media", "videos", "NeuralNetwork", "480p15")
VIDEO_FILENAME = "NeuralNetwork.mp4"

import time

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    video_url = None
    neurons_input = ""

    if request.method == "POST":
        neurons_input = request.form.get("neurons", "").strip()
        try:
            neurons = [int(n) for n in neurons_input.split() if n.isdigit()]
            if not neurons or len(neurons) > 6:
                raise ValueError("Enter between 1 and 6 neuron counts.")

            os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
            with open(CONFIG_PATH, "w") as f:
                json.dump({"neurons": neurons, "layers": len(neurons)}, f)

            subprocess.run(
                ["manim", "-ql", MANIM_SCRIPT, "NeuralNetwork"],
                check=True,
                capture_output=True,
                text=True
            )

            # Add timestamp to bust browser cache
            video_url = url_for('serve_video', t=int(time.time()))
            neurons_input = ""  # clear input on success

        except subprocess.CalledProcessError as e:
            error = f"Manim rendering failed: {e.stderr or e.stdout}"
        except Exception as e:
            error = str(e)

    return render_template("index.html", error=error, video_url=video_url, neurons=neurons_input)


@app.route("/video")
def serve_video():
    # Check if video file exists before serving
    if not os.path.exists(os.path.join(VIDEO_DIR, VIDEO_FILENAME)):
        abort(404, description="Video file not found")
    return send_from_directory(VIDEO_DIR, VIDEO_FILENAME)

if __name__ == "__main__":
    app.run(debug=True)
