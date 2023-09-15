from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')

results = model.train(data='dataset.yaml', epochs=100, imgsz=640)
