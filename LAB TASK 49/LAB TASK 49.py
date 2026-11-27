# Face Recognition using DeepFace

from deepface import DeepFace

# Compare two face images
result = DeepFace.verify(
    img1_path="person1.jpg",
    img2_path="person2.jpg",
    model_name="Facenet"
)

# Display result
print("Face Recognition Result:")

if result["verified"]:
    print("Both images belong to the same person.")
else:
    print("Both images belong to different persons.")

print("Similarity distance:",
      round(result["distance"], 4))
