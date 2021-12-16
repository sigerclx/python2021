import paddlex as pdx
import os
# 利用paddlex 2.0.0  训练出的模型

predictor = pdx.deploy.Predictor(r'inference_model')

for root,dirs,files in os.walk(r'yanzheng'):
    file = files


for fpath  in file:
    result = predictor.predict(img_file=os.path.join('yanzheng',fpath))
    #print(result)
    animalname = result[0]['category']
    if animalname != 'dogs':
        print('error!')
