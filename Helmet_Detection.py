from ultralytics import YOLO

model_path = 'yolov10n.pt'
model = YOLO(model_path)

yaml_path = 'safety_helmet_dataset\data.yaml'
epochs = 50
img_size = 640
batch_size = 16

trained_model_path = 'best.pt'
model = YOLO(trained_model_path)

model.val(data=yaml_path,
          imgsz=img_size,
          split='test')