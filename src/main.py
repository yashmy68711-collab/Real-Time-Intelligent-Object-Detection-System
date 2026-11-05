import cv2
from pathlib import Path
from detector import ObjectDetector

def main():

    # Get project directory
    project_dir = Path(__file__).resolve().parent.parent

    # Output directory
    output_dir = project_dir / "outputs" / "images"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load YOLO model
    detector = ObjectDetector()

    # Ask user for image path
    image_input = input("\nEnter image path: ").strip()

    image_path = Path(image_input).expanduser()

    # Handle relative paths
    if not image_path.is_absolute():
        image_path = project_dir / image_path

    # Check whether image exists
    if not image_path.exists():
        print("Error: Image not found!")
        return

    # Check image format
    supported_formats = {".jpg", ".jpeg", ".png"}

    if image_path.suffix.lower() not in supported_formats:
        print("Error: Unsupported image format!")
        return

    # Detect objects
    print("\nDetecting objects...")

    results = detector.detect(
        str(image_path),
        confidence=0.25
    )

    # Process detection results
    for result in results:

        # Draw bounding boxes
        detected_image = result.plot()

        # Count objects
        total_objects = len(result.boxes)

        print("\n========== DETECTION RESULTS ==========")

        print(f"Image: {image_path.name}")
        print(f"Total objects detected: {total_objects}")

        # Extract object information
        for index, box in enumerate(result.boxes, start=1):

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = result.names[class_id]

            # Extract bounding box coordinates
            x1, y1, x2, y2 = map(
                int, box.xyxy[0].tolist()
            )

            print(f"\nObject {index}: {class_name}")
            print(f"Confidence: {confidence:.2%}")
            print(f"Bounding Box: ({x1}, {y1}, {x2}, {y2})")

        # Save detection result
        output_path = output_dir / f"detected_{image_path.name}"

        success = cv2.imwrite(
            str(output_path),
            detected_image
        )

        if success:
            print(f"\nDetection image saved: {output_path}")
        else:
            print("\nError: Could not save detection image!")

        print("\n=======================================")


if __name__ == "__main__":
    main()
