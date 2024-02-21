# Intruder Alert System using OpenCV in Python

This project builds a real-time face detection system with intruder alerts sent directly to your Telegram! It uses OpenCV to scan your webcam feed for faces, highlighting them with a green box. If a face is detected, it captures an image, sends it to your specified Telegram chat along with an "Intruder Alert!" message, and even acknowledges whether the message delivery was successful or not.

## Authors
-  Thaarakenth C P - [@cpt2004](https://www.github.com/cpt2004)

## Features

- Real-time Face Detection
- Detects faces using OpenCV Haar cascades classifier.
- Highlights detected faces with a green rectangle.
- Sends an image of the detected face and a "Intruder Alert!" message to a specified Telegram chat via the Telegram Bot API.
- Offers visual feedback on successful Telegram message delivery.
## Prerequisites

Install OpenCV for Python

```bash
  pip install opencv-python
```
    
## Deployment

To deploy this project run

```bash
  python -m face_detection.py
```

## Screenshots

API Response:

[![API Response](https://i.postimg.cc/q70YHQ9J/response.png)](https://postimg.cc/TK7QrjdF)

Sample Output Message:

[![intruder-face.jpg](https://i.postimg.cc/qBtr5THs/intruder-face.jpg)](https://postimg.cc/HjCFrFxn)

Telegram Chat:

[![Telegram Chat.png](https://i.postimg.cc/vBqK2tQ7/chat.png)](https://postimg.cc/2bWTVvL3)


## Acknowledgements

 - [Telegram APIs](https://core.telegram.org/api/push-updates)
 - [Face Detection - GeeksForGeeks](https://www.geeksforgeeks.org/face-detection-using-python-and-opencv-with-webcam/)
 - [Readme Creator](https://readme.so/editor/)
