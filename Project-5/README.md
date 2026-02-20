# 😊 Real-Time Emotion Detection

A real-time facial emotion recognition system built with **OpenCV** and **Deep Learning (Keras/TensorFlow)**. The application detects human faces via webcam and classifies the displayed emotion into one of several categories — live, frame by frame.

---

## 🧠 How It Works

1. **Face Detection** — Uses OpenCV's Haar Cascade Classifier (`haarcascade_frontalface_default.xml`) to detect faces in each video frame.
2. **Preprocessing** — Detected face regions are extracted, converted to grayscale, resized, and normalized before being passed to the model.
3. **Emotion Classification** — A pre-trained Convolutional Neural Network (`emotion_model.hdf5`) predicts the emotion from the face region.
4. **Live Overlay** — The predicted emotion label is drawn directly onto the video feed in real time.

---

## 🎭 Detectable Emotions

| Label     | Emotion     |
|-----------|-------------|
| 😠        | Angry       |
| 🤢        | Disgust     |
| 😨        | Fear        |
| 😄        | Happy       |
| 😐        | Neutral     |
| 😢        | Sad         |
| 😲        | Surprise    |

---

## 🗂️ Project Structure

```
├── emotion_detection.py              # Main script for real-time detection
├── emotion_model.hdf5                # Pre-trained Keras emotion classification model
├── haarcascade_frontalface_default.xml  # OpenCV Haar Cascade for face detection
└── README.md
```

---

## ⚙️ Requirements

- Python 3.7+
- OpenCV
- TensorFlow / Keras
- NumPy

Install dependencies:

```bash
pip install opencv-python tensorflow numpy
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/programmer-shreyajana/<repo-name>.git
cd <repo-name>
```

### 2. Ensure All Files Are Present

Make sure `emotion_model.hdf5` and `haarcascade_frontalface_default.xml` are in the same directory as `emotion_detection.py`.

### 3. Run the Script

```bash
python emotion_detection.py
```

> Your webcam will activate and emotion labels will appear on detected faces in real time. Press **`q`** to quit.

---

## 🧪 Model Details

- **Architecture:** Convolutional Neural Network (CNN)
- **Framework:** Keras with TensorFlow backend
- **Input:** 48×48 grayscale face image
- **Output:** Softmax probabilities over 7 emotion classes
- **Training Dataset:** FER-2013 (Facial Expression Recognition)

---

## 📸 Demo

 <img width="698" height="443" alt="Screenshot 2026-02-20 151955" src="https://github.com/user-attachments/assets/93149101-6595-4d9a-9121-7851017a8c9b" />


---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)

---

## 🙋‍♀️ Author

**Shreya Jana**

[![GitHub](https://img.shields.io/badge/GitHub-programmer--shreyajana-181717?style=for-the-badge&logo=github)](https://github.com/programmer-shreyajana)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Shreya%20Jana-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/shreya-jana-6a20183b2/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
