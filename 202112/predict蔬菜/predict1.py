import paddlex as pdx
predictor = pdx.deploy.Predictor(r'inference_model')
result = predictor.predict(img_file=r'imgs/qiezi1.png')
print(result)