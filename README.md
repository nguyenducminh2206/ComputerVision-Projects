# YOLOv10 Helmet and Person Detection

This project uses the YOLOv10 model to detect persons and helmets in images. The model is trained on a dataset that includes labeled images of persons and helmets. This README provides an overview of how to set up, train, and test the model.

## Table of Contents
- [Setup](#setup)
- [Training the Model](#training-the-model)
- [Testing the Model](#testing-the-model)
- [Inference](#inference)
- [Visualization](#visualization)

## Setup

1. **Clone the Repository**

    ```
    git clone https://github.com/THU-MIG/yolov10.git
    cd yolov10
    ```

2. **Install Requirements**

    ```
    pip install -r requirements.txt
    pip install -e .
    ```

3. **Download Pre-trained Weights**

    ```
    wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt
    ```

4. **Prepare the Dataset**

    ```
    gdown '1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R'
    mkdir safety_helmet_dataset
    unzip -q 'Safety_Helmet_Dataset.zip' -d 'safety_helmet_dataset'
    ```

## Training the Model

To train the model, run the following script:

```
from ultralytics import YOLOv10

# Load the model
model_path = 'yolov10n.pt'
model = YOLOv10(model_path)

# Set training parameters
yaml_path = 'safety_helmet_dataset/data.yaml'
epochs = 30
img_size = 640
batch_size = 16

# Train the model
model.train(data=yaml_path, epochs=epochs, imgsz=img_size)
