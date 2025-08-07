# Neural Network Visualizer

## General Process & Overview

<p>Neural Networks were, and still are, a big interest of mine. Ever since I learned TensorFlow, I would go on Kaggle and create Neural Networks to predict outcomes based on data. However, I have noticed that visualizing Neural Networks was also a big part of understanding how they work. For this reason, I set my goals towards making a simple visualizer to show what Neural Network architectures generally look like.</p>

<p>To create this project, I first started by creating a Manim script to create the visualization videos. Using a class structure and various methods, I created a Python file that can take a user's input and output a high-quality Neural Network video that the user can then download. The next step would be to create a frontend website to allow the user to input their specifications. To do this, I simply created an HTML page to structure the website, then used CSS to style the website. Finally, I created a Flask script to be able to not only deploy the website, but be able to connect the frontend with the manim script to create and post the Neural Network videos. </p>

## Complications

<p>Originally, this project was created using a JavaScript, HTML, CSS, and Python tech stack. However, to connect the frontend to the backend, I had to use a Flask backend. The issue with this process is that the JavaScript code had trouble fetching the data from the Flask backend, and could not add the video to the website for the user to download. As a result, I transitioned into the architecture I use now, by simply removing the JavaScript portion of this project and purely relying on Flask backend. </p>

## Tech Stack

- <a href="https://www.manim.community/" target="_blank">Manim</a>
- <a href="https://flask.palletsprojects.com/en/stable/" target="_blank">Flask</a>
- CSS
- HTML
- Python
- <a href="https://render.com/">Render</a>

## How to Use

<p>To use the Neural Network Visualizer, <a href="https://neural-network-visualizer-zbv8.onrender.com">click here</a>! However, please note that this website is deployed using a tool known as render, and after 15 minutes of remaining idle, the render website will temporarily shut down until it's opened up again. Additionally, the manim script can take 1-2 minutes to generate your video.</p>
