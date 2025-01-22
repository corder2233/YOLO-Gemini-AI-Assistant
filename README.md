# YOLO + Gemini AI Assistant

This project combines the power of the YOLOv10 object detection model and Gemini API to create an interactive assistant that helps visually impaired individuals understand their surroundings through real-time video analysis and intelligent conversational responses.

## Features

- **Real-Time Object Detection**: Uses the YOLOv10 model to detect objects in video streams, providing positional information (e.g., left, right, up, down).
- **Interactive Assistant**: Engages users in natural language conversations about the detected objects using the Gemini API.
- **Configurable Settings**: Includes settings for Gemini's generative model, such as temperature, top_p, and max_output_tokens.
- **User-Friendly Commands**:
  - Press `q` to start the assistant conversation mode.
  - Press `x` to exit the program.

## Prerequisites

Before running this project, ensure you have the following:

- Python 3.8 or higher
- Required Python libraries (included in `requirements.txt`)
- Generate Google Gemini API key

## Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Generate Gemini API key:
   ```bash
   https://aistudio.google.com/app/apikey
   ```
3. Navigate to the project directory:
   ```bash
   cd yolo_gemini_assistant
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Ensure your Gemini API key is valid and replace the placeholder in the code with your key.

## How to Run

1. Execute the script:
   ```bash
   python main.py
   ```
2. Use the following controls during runtime:
   - Press `q` to analyze detected objects and start the assistant conversation.
   - Press `x` to exit the application.

## Code Overview

1. **Gemini API Integration**:
   - Configures the generative model for conversational responses.
   - Generates intuitive descriptions and responds to user queries.
2. **YOLOv10 Object Detection**:
   - Detects objects in real-time using a lightweight YOLOv10 model.
   - Draws bounding boxes and positional details on the video feed.
   - ![image](https://github.com/user-attachments/assets/e3576d59-7804-4c34-8502-52d3ccee5f84)

3. **Interactive Assistant**:
   - Processes detected objects and engages users with natural language explanations.
   - Allows follow-up queries to enhance user experience.

## Example Use Case

- Assist visually impaired individuals by providing detailed descriptions of detected objects in their environment.
- Enable intuitive interactions for understanding spatial context.

## Future Enhancements

- Add support for additional object detection models.
- Extend functionality for multi-language support.
- Optimize response times and enhance user interface.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- **YOLOv10**: [Ultralytics](https://github.com/ultralytics/yolov5)
- **Gemini API**: Generative AI model by Google

---

Feel free to reach out for any queries or support!
