

# Object Detection using Pre-trained Model

import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Select image
root = Tk()
root.withdraw()

image_path = askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
)

root.destroy()

if image_path == "":
    print("No image selected")

else:
    # Load pre-trained model
    model_path = (
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    face_model = cv2.CascadeClassifier(model_path)

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Image could not be loaded")

    elif face_model.empty():
        print("Model could not be loaded")

    else:
        # Convert to grayscale
        gray = cv2.cvtColor(
            image, cv2.COLOR_BGR2GRAY
        )

        # Detect faces
        faces = face_model.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5
        )

        # Draw rectangle around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(
                image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        print("Object Detection Result")
        print("Faces detected:", len(faces))

        # Save result
        cv2.imwrite("detected.jpg", image)

        print("Result saved as detected.jpg")
