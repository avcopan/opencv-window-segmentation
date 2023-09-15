#### Instructions

I am following along with [this tutorial](https://youtu.be/DMRlOWfRBKU?si=H3yu7fKlFmoUorzu)

#### Set up

Install [poetry](https://python-poetry.org/docs/basic-usage/) and run:
```
poetry install
```
then start the poetry environment using
```
poetry shell
```

#### 1. Download images

Modify the search terms in the image download script `01_download_images.py` as
needed, then run it:
```
python 01_download_images.py
```

#### 2. Label images

Run `labelme` and use the GUI to label all of the images in the download folder.
```
labelme
```

#### 3. Convert the labeled images to YOLO format

```
labelme2yolo --json_dir images
```
Now, create the following directories in the project root:
```
mkdir train
mkdir val
```
And move the results into them:
```
mv images/YOLODataset/images/train/ train/images/
mv images/YOLODataset/labels/train/ train/labels/
mv images/YOLODataset/images/val/ val/images/
mv images/YOLODataset/labels/val/ val/labels/
```
Also, move the dataset YAML into the project root:
```
mv images/YOLODataset/dataset.yaml .
```
And update the paths inside of it, giving absolute paths to your `train/` and `val/` directories:
```
train: /home/avcopan/Documents/Code/prime/opencv-window-segmentation/train
val: /home/avcopan/Documents/Code/prime/opencv-window-segmentation/val
nc: 2
names: ['window-outside', 'window']
```
