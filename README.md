## Day 1 — Project Setup and Environment Configuration

### Objectives
- Establish the development environment.
- Create the project directory structure.
- Install and configure the required Python libraries.
- Prepare the project for AI-based object detection.

### Work Completed
- Created the Real-Time Intelligent Object Detection System project.
- Configured a Python virtual environment.
- Installed OpenCV, NumPy, Ultralytics, PyTorch and Matplotlib.
- Created the source code, data, models and output directories.
- Configured Git and GitHub.
- Created a public GitHub repository.
- Uploaded the initial project files.

### Technologies
- Python
- OpenCV
- NumPy
- PyTorch
- Ultralytics YOLO
- Git and GitHub

### Outcome
Successfully configured the development environment and prepared the project for implementing an AI-powered object detection system.## Day 2 — YOLO Fundamentals and Object Detection Experiments

### Concepts Learned
- Computer Vision
- Object Detection
- YOLO architecture and pretrained models
- Bounding Boxes
- Confidence Scores
- Frames Per Second (FPS)

### Practical Implementation
- Loaded the pretrained YOLOv8n model.
- Performed image-based object detection.
- Extracted object classes and confidence scores.
- Experimented with different confidence thresholds.
- Observed how confidence thresholds affect detection results.

### Confidence Threshold Experiments

| Confidence Threshold | Detected Objects |
|---|---:|
| 0.25 | 6 |
| 0.50 | 4 |
| 0.75 | Experiment completed |

##Day 2 — YOLO Fundamentals and Confidence Threshold Experiments
Concepts Learned

    Computer Vision
    Object Detection
    YOLO (You Only Look Once)
    Pretrained YOLO models
    Bounding Boxes
    Confidence Scores
    Frames Per Second (FPS)

Practical Implementation

    Loaded the pretrained YOLOv8n model.
    Performed image-based object detection.
    Extracted object class names and confidence scores.
    Generated bounding boxes around detected objects.
    Experimented with different confidence thresholds.

Confidence Threshold Experiments
Confidence Threshold	Detected Objects
0.25	6
0.50	4
0.75	Experiment completed
Outcome

Understood how YOLO identifies objects and how confidence thresholds filter detection predictions.

##Day 3 — Multiple Image Object Detection

Objectives
Extend the system to process multiple images.
Automatically identify images inside a directory.
Perform object detection on each image.
Save detection results separately.
Practical Implementation
Downloaded multiple test images.
Implemented automatic image discovery using Python's pathlib.
Added support for JPG, JPEG and PNG images.
Loaded the YOLO model only once per execution.

Processed images sequentially.
Detected multiple objects in individual images.
Generated bounding boxes and confidence scores.
Saved each processed image separately.
Technologies and Libraries

Python
OpenCV
Ultralytics YOLOv8
pathlib
Output

Detection results are saved inside:
outputs/images/
Example output filenames:
detected_bus.jpg
detected_test.jpg
detected_zidane.jpg

Outcome
Successfully extended the object detection system from processing a single fixed image to automatically processing multiple images from a directory.
Next Step
Implement real-time object detection using a webcam.

## Day 4 — Enhanced Image-Based Object Detection

### Objectives
- Allow users to select an image using its file path.
- Detect objects in the selected image.
- Extract object names and confidence scores.
- Calculate bounding-box coordinates.
- Count the total number of detected objects.
- Save the detection results.

### Practical Implementation
- Updated the YOLO object detector.
- Implemented user input for selecting an image.
- Added image path validation.
- Extracted object class names and confidence scores.
- Extracted bounding-box coordinates (x1, y1, x2, y2).
- Implemented total object counting.
- Generated annotated images with bounding boxes.
- Saved detection results automatically.

### Technologies and Libraries
- Python
- OpenCV
- Ultralytics YOLOv8
- pathlib

### Testing
Tested the system using:
- bus.jpg
- test.jpg
- zidane.jpg

Example result from zidane.jpg:
- Person: 83.60% confidence
- Person: 81.90% confidence
- Tie: 29.10% confidence
- Total detected objects: 3

### Output
Detection images are saved in:

`outputs/images/`

Example:
- detected_bus.jpg
- detected_test.jpg
- detected_zidane.jpg

### Outcome
Successfully developed an enhanced image-based object detection system that allows users to select images, identify objects, extract confidence scores and bounding-box coordinates, count detected objects, and save annotated results.

