import tensorflow as tf
from keras.preprocessing.image import load_img,img_to_array
import  numpy as np
from keras.applications.vgg16 import  preprocess_input
from PIL import Image
import matplotlib.pyplot as plt
# 手写单图验证


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
# 将模型的各层堆叠起来，以搭建 tf.keras.Sequential 模型。为训练选择优化器和损失函数：
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# 读取已经训练好的模型：
model.load_weights('hand.h5')


def predict_handwrite_image(imgpath):
    # 读取从网上下载的任意图片，构建验证使用的矩阵。即待验证图像的矩阵（1,28,28）和对应数字的矩阵(1,),这里的1是1张图
    imm = np.array(Image.open(imgpath).convert('L'))  #灰度图(L)
    imm = 255 - imm  # 把白底黑字反向
    imm = imm / 255  # 转化为0-1,归一化
    imm1 = Image.fromarray(imm)  # 转化为图像
    imm2 = imm1.resize([28, 28])  # 压缩
    im_array = np.array(imm2)
    #img_shape = np.reshape(im_array, 784)
    #real_x = np.array([1 - img_shape])
    #x_test1 = real_x.reshape((1, 28, 28))  # 转化成可以用model.evaluate验证的矩阵
    x_test = im_array.reshape((1, 28, 28))  # 转化成可以用model.evaluate验证的矩阵
    return x_test,im_array

#x_test = predict_handwrite_image('3.jpg')
#imgpath = '6.png'
imgpath = '3.jpg'
x_test,im_array = predict_handwrite_image(imgpath)

plt.figure(figsize=(2,2))
plt.imshow(im_array, cmap=plt.cm.binary)
plt.show()



y_test = np.array([6])  # y_test.shape = (1,)
# 用模型评估
model.evaluate(x_test,  y_test, verbose=2)


# 单张图片验证
num = model.predict(x_test)
print(num)
# np.argmax 取出num的最大值所在的位置
print(imgpath +' 验证结果为：',np.argmax(num[0]))



