import cv2
import os
import argparse
import mediapipe as mp

# Process Image
def process_image(img,face_detection):
    H, W, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    for detection in out.detections:
        bbox = detection.location_data.relative_bounding_box
        x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
        x1 = int(x1 * W)
        y1 = int(y1 * H)
        w = int(w * W)
        h = int(h * H)

        # cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),2)

        # Blur Image
        img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (30, 30))

        return img

# Read image
args = argparse.ArgumentParser()
args.add_argument('--mode',default='webcam')
args.add_argument('--filepath',default=None)
args = args.parse_args()


# Detect face
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0,min_detection_confidence=0.8) as face_detection:

    if args.mode in ["image"]:
        img = cv2.imread(args.filepath)


        img = process_image(img,face_detection)

        # save image
        cv2.imwrite(os.path.join('.','data','anonymized_face.jpg'),img)

    elif args.mode in ["video"]:

        cap = cv2.VideoCapture(args.filepath)
        ret,frame = cap.read()

        output_video = cv2.VideoWriter(os.path.join('.','data','output.mp4'),cv2.VideoWriter_fourcc(*'MP4V'),25,(frame.shape[1],frame.shape[0]))

        while ret:
            frame = process_image(frame,face_detection)
            output_video.write(frame)
            ret,frame = cap.read()

        cap.release()
        output_video.release()

    elif args.mode in ['webcam']:
        cap = cv2.VideoCapture(0)
        ret,frame = cap.read()

        while ret:
            frame = process_image(frame,face_detection)
            cv2.imshow('Face',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            ret,frame = cap.read()
        cap.release()
        cv2.destroyAllWindows()