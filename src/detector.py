from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path="yolov8n.pt"):
        """Load the pretrained YOLO model."""
        print("Loading YOLO model...")
        self.model = YOLO(model_path)
        print("YOLO model loaded successfully!")

    def detect(self, image_path):
        """Detect objects in an image."""
        results = self.model.predict(
            source=image_path,
            conf=0.25,
            save=False,
            verbose=False
        )

        return results