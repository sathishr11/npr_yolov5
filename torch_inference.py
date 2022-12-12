import torch

# Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

# Images
imgs = ['yolov5/infer.jpg']  # batch of images
# imgs = ['./test/images/Hello.8b2540a6-a6d1-11ec-a828-84a93ea18ae6.jpg']

# Inference
results = model(imgs)

# Results
# results.print()
# results.print()
# results.save()  # or .show()
results.show()

startX, startY, endX, endY, conf , class_name = results.xyxy[0].numpy()
startX = results.xyxy[0].numpy()[0][0]
startY = results.xyxy[0].numpy()[0][1]
endX = results.xyxy[0].numpy()[0][2]
endY = results.xyxy[0].numpy()[0][3]
conf = results.xyxy[0].numpy()[0][4]
class_name = results.xyxy[0].numpy()[0][5]
# results.xyxy[0]  # img1 predictions (tensor)
# results.pandas().xyxy[0]  # img1 predictions (pandas)
#      xmin    ymin    xmax   ymax  confidence  class    name
# 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# 1  433.50  433.50   517.5  714.5    0.687988     27     tie
from PIL import Image
original_image  = Image.open(imgs[0])
for idx, result in enumerate(results.xyxy[0].numpy()):
    print(result[0])
    # startX, startY, endX, endY, conf , class_name = result[0]
    startX = result[0]
    startY = result[1]
    endX = result[2]
    endY = result[3]
    conf = result[4]
    class_name = result[5]
    original_image.crop((startX, startY, endX, endY)).save(f'cropped_{idx}.jpeg')