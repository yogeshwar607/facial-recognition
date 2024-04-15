# import cv2


# def capture_images():
#     cam = cv2.VideoCapture(0)
#     face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#     # For each person, enter one numeric face ID.
#     face_id = input("\nPlease enter user ID/name end press <return> ==> ").strip()
#     print("\n[INFO] Initializing face capture. Look at the camera and wait...")

#     # Initialize individual sampling face count.
#     count = 0

#     while True:
#         ret, img = cam.read()
#         img = cv2.flip(img, 1)  # Flip video image vertically.
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = face_detector.detectMultiScale(gray, 1.3, 5)

#         for (x, y, w, h) in faces:
#             cv2.rectangle(img, (x, y), (x + w + 50, y + h + 50), (255, 0, 0), 2)
#             count += 1

#             # Save the captured image into the images/ folder.
#             gray = gray[y : y + h, x : x + w]

#             cv2.imwrite(f"images/{face_id}.{count}.jpg", gray)
#             cv2.imshow("image", img)

#         k = cv2.waitKey(100) & 0xFF  # Press 'ESC' for exiting video.
#         if k == 27:
#             break
#         elif count >= 70:  # Take 70 face sample and stop video.
#             break

#     # Do a bit of cleanup.
#     print("\n[INFO] Exiting program and cleanup stuff")
#     cam.release()
#     cv2.destroyAllWindows()


# if __name__ == "__main__":
#     capture_images()


import cv2
import os
import time


def initialize():
    cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id
    face_id = input('\n pls enter user id/name end press <return> ==>  ')

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0

    return cam, face_detector, face_id, count


def create_input(cam, face_detector, face_id, count):
    loop_count = count

    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            print('inside for')

            cv2.rectangle(img, (x,y), (x+w+50,y+h+50), (255,0,0), 2)     
            loop_count += 1

            # Save the captured image into the datasets folder
            gray = gray[y:y+h,x:x+w]

            f_name = f"images/{face_id}.{loop_count}.jpg"
            cv2.imwrite(f_name, gray)
            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        if loop_count >= count + 10: # Take 70 face sample and stop video
            break

    return loop_count





if __name__ == '__main__':
    cam, face_detector, face_id, count = initialize()
    
    print("input NORMAL face\n")
    normal_count = create_input(cam, face_detector, face_id, count)
    print("10 seconds waiting... Prepare for face with HAT\n")
    time.sleep(10)
    hat_count = create_input(cam, face_detector, face_id, normal_count)
    
    print("10 seconds waiting... Prepare for face with MASK\n")
    time.sleep(10)
    mask_count = create_input(cam, face_detector, face_id, hat_count)

    print("10 seconds waiting... Prepare for face with SPECS\n")
    time.sleep(10)
    specs_count = create_input(cam, face_detector, face_id, mask_count)

    print("10 seconds waiting... Prepare for WIERD face\n")
    time.sleep(10)
    wierd_face_count = create_input(cam, face_detector, face_id, specs_count)

    print("10 seconds waiting... Prepare for face with GOGGLES\n")
    time.sleep(10)
    goggles_count = create_input(cam, face_detector, face_id, wierd_face_count)


    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
    

    