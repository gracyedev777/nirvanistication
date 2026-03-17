# 🧬 Nirvanistication

[![Built with Flet](https://img.shields.io/badge/Built%20with-Flet%20(HTML5)-cyan)](https://flet.dev)
[![Core Vision](https://img.shields.io/badge/Vision-OpenCV-green)](https://opencv.org)
[![Processing](https://img.shields.io/badge/Logic-NumPy-blue)](https://numpy.org)

**Nirvanistication** is a specialized image processing engine designed to reconstruct any source visual using the "DNA" of Nirvana's *Nevermind* aesthetic. The software performs a deep structural analysis to reassemble user data through discrete mathematical mapping and luma synchronization.

## 🛠 The "Discrete Reconstruction" Method

The engine operates on a four-stage computational pipeline to ensure the output preserves both the structural integrity of the user's image and the chromatic soul of the reference material.

### 1. Spatial Decomposition
The input image is mathematically dismantled. The engine segments the source into a grid of **10x10 pixel sub-matrices**. 
* Each segment is analyzed for its local variance and texture.
* These segments form a dynamic **texture dictionary** used to rebuild the target image from the ground up.

### 2. Perceptual LAB Processing (Luma Mapping)
To maintain human-eye recognition of the subject, the engine utilizes the **BT.601 Recommendation** for Luma ($Y'$) calculation:

$$Y' = 0.299R + 0.587G + 0.114B$$

By converting RGB channels into luminance values, the software ensures that the "depth" and "shadows" of the original photo are perfectly translated into the blue-toned Nirvana palette.

### 3. Nearest Neighbor Search (MSE Optimization)
The core of the reconstruction uses a **Mean Squared Error (MSE)** algorithm. 
* The engine compares the brightness of every 10x10 block in the *Nevermind* cover against the dictionary created from your photo.
* It performs a high-speed search to find the "Nearest Neighbor"—the block that best fits the geometry and light intensity of the target area.

### 4. Final Alpha Blending Composition
To avoid a "pixelated" look and ensure smooth transitions, the blocks are fused using **32-bit Linear Alpha Blending**.
* This process overlays the source textures onto the reference geometry at a **40/60 ratio**.
* The result is a high-integrity chromatic fusion that keeps the colors of the ocean-blue cover while revealing the details of the uploaded image.

---

## 💻 Tech Stack & Architecture
* **Interface:** Modern SPA architecture rendered via **HTML5/Web-UI Stack**.
* **Engine:** Python 3.13.
* **Core Libraries:** OpenCV, NumPy, and Flet.
* **Database:** SQLite3 for process logging.

---

## 🚀 How to Run
1. Launch `Nirvanistication.exe`.
2. Wait for the initialization (The engine loads the UI and the soundtrack).
3. Click **UPLOAD** to select your image.
4. The system will output a rendered `.jpg` file in the same directory.

## 👤 Credits & Authorship
This project was conceptualized and developed by:
**Gracye**

*Developed as a high-performance custom gift for Alisson - 2026.*
*Audio powered by: "Something In The Way" - Nirvana.*
