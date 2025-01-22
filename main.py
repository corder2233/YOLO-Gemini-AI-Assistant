# this code have more feature like 1-assistant conversation, 2- ask for exit('q', and 'x')

import cv2
from ultralytics import YOLO
import google.generativeai as genai
import os

# Configure Gemini API
api_key = "AIzaSyBSCp3SG9pBiAFvo9e5zVupU4D4Nhoyd-o"
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.1,
    "top_p": 0.9,
    "top_k": 20,
    "max_output_tokens": 512,
    "response_mime_type": "text/plain",
}

# Load Gemini model
model_gemini = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def generate_content(prompt):
    try:
        response = model_gemini.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Error with Gemini API:", str(e))
        return "I encountered an error while processing your request."

# Load YOLO model
model_yolo = YOLO('yolov10n.pt')

def process_frame(frame):
    results = model_yolo(frame)
    detected_objects = []

    for box in results[0].boxes:
        xyxy = box.xyxy.cpu().numpy()
        confidence = float(box.conf.cpu().numpy().item())
        class_id = int(box.cls.cpu().numpy().item())
        label = model_yolo.names[class_id]

        x_min, y_min, x_max, y_max = map(int, xyxy.flatten())
        object_center_x = (x_min + x_max) // 2
        object_center_y = (y_min + y_max) // 2
        horizontal_position = "left" if object_center_x < frame.shape[1] // 2 else "right"
        vertical_position = "up" if object_center_y < frame.shape[0] // 2 else "down"
        position_description = f"{label} ({confidence:.2f}) is {horizontal_position} and {vertical_position}"
        detected_objects.append(position_description)

        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {confidence:.2f}", (x_min, y_min - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    return frame, detected_objects

def start_conversation(detected_objects):
    if detected_objects:
        object_description = ". ".join(detected_objects)
        prompt = (
            f"You are an assistive AI designed to help visually impaired individuals understand their surroundings. "
            f"Your role is to provide clear, concise, and contextually rich descriptions of the detected objects. "
            f"Detected objects include: {object_description}. Provide a detailed and intuitive explanation."
        )

        print("\nPrompt to Gemini API:", prompt)
        content = generate_content(prompt)
        print("\nGemini's Response:\n", content)

        while True:
            user_query = input("Ask a question about the scene (type 'exit' to stop): ")
            if user_query.lower() in ["exit", "quit"]:
                print("Exiting conversation mode.")
                break
            follow_up_prompt = f"{content} User query: {user_query}. Respond naturally."
            follow_up_response = generate_content(follow_up_prompt)
            print("\nGemini's Response:\n", follow_up_response)
    else:
        print("\nNo objects detected.")

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

cv2.namedWindow('YOLO + Gemini', cv2.WINDOW_NORMAL)  # Make window resizable

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    frame, detected_objects = process_frame(frame)
    cv2.imshow('YOLO + Gemini', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):  # Start object detection and conversation mode on 'q'
        print("\nProcessing detected objects and starting conversation...")
        start_conversation(detected_objects)
    elif key == ord('x'):  # Exit the program on 'x'
        print("Exiting program.")
        break

cap.release()
cv2.destroyAllWindows()
