import cv2, requests, time, json, os, winsound
from dotenv import load_dotenv

load_dotenv()

def face_detect(frame):
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
    face = face_classifier.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
        alert_msg(frame)
    return frame

def alert_msg(frame):
    TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
    
    image_path = 'detected_face.jpg'
    cv2.imwrite(image_path, frame)   
    
    files = {'photo': open(image_path, 'rb')}
    caption = "Intruder Alert! Face captured!"
    telegram_url = f'https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendPhoto'
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'caption': caption
        }
        
    try:
        response = requests.post(telegram_url, params=params, files=files)
        print(f"Telegram API Response: {json.dumps(response.json(), indent=4)}")

    except requests.RequestException as e:
        print(f"Error : {e}")

vid = cv2.VideoCapture(0)
while(True): 
	ret, frame = vid.read()
	winsound.Beep(1000,500)
	cv2.imshow('Web Cam', face_detect(frame))
	time.sleep(5)
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break
vid.release()
cv2.destroyAllWindows()
