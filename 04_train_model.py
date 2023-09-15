from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')

results = model.train(
    data='./training_config.yaml',
    epochs=150,
    imgsz=640,
    project='./runs',
)

