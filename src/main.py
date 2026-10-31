import cv2
from pathlib import Path
from detector import ObjectDetector


def main():
    # Project paths
    project_dir = Path(__file__).resolve().parent.parent
    image_path = project_dir / "data" / "images" / "test.jpg"
    output_dir = project_dir / "outputs" / "images"

    output_dir.mkdir(parents=True, exist_ok=True)

    # Check image
    if not image_path.exists():
        print(f"Image not found: {image_path}")
        return

    # Load detector
    detector = ObjectDetector()

    # Detect objects
    print("\nDetecting objects...")
    results = detector.detect(str(image_path))

    # Process results
    for result in results:
        detected_image = result.plot()

        # Save output image
        output_path = output_dir / "detection_result.jpg"
        cv2.imwrite(str(output_path), detected_image)

        # Display detections
        print("\nDetected objects:")

        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = result.names[class_id]

            print(
                f"{class_name}: {confidence:.2%}"
            )

    print(f"\nResult saved at: {output_path}")


if __name__ == "__main__":
    main()
