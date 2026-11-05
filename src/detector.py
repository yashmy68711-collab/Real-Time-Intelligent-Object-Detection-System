from ultralytics import YOLO

class ObjectDetector:

    def __init__(self, model_path="yolov8n.pt"):
        """
        Initialize the YOLO object detection model.
        """
        print("Loading YOLO model...")

        self.model = YOLO(model_path)

        print("YOLO model loaded successfully!")

    def detect(self, image_path, confidence=0.25):
        """
        Detect objects in the given image.
        """

        results = self.model.predict(
            source=image_path,
            conf=confidence,
            save=False,
            verbose=False
        )

        return results