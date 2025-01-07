# Intruder Alert System using OpenCV in Python

This project builds a real-time face detection system with intruder alerts sent directly to your Telegram! It uses OpenCV to scan your webcam feed for faces, highlighting them with a green box. If a face is detected, it captures an image, sends it to your specified Telegram chat along with a message, and acknowledges whether the message delivery was successful or not.

## Authors
-  Thaarakenth C P - [@cpt1909](https://www.github.com/cpt1909)

## Features

- Real-time Face Detection
- Detects faces using OpenCV Haar cascades classifier.
- Highlights detected faces with a green rectangle.
- Sends an image of the detected face and a message to a specified Telegram chat via the Telegram Bot API.
- Offers visual feedback on successful Telegram message delivery.
## Prerequisites
1. Install Python 3.*

2. Install OpenCV for Python

```bash
  pip install opencv-python
  pip install python-dotenv
```
3. Create a .env file with the necessary credentials

## Deployment

To deploy this project run

```bash
  python face_detection.py
```

## Screenshots

API Response:

[![API Response](https://i.postimg.cc/q70YHQ9J/response.png)](https://postimg.cc/TK7QrjdF)

## Acknowledgements

 - [Telegram APIs](https://core.telegram.org/api/push-updates)
 - [Face Detection - GeeksForGeeks](https://www.geeksforgeeks.org/face-detection-using-python-and-opencv-with-webcam/)
 - [Readme Creator](https://readme.so/editor/)
