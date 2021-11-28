import tensorflow as tf
from keras.preprocessing.image import load_img,img_to_array
import  numpy as np
from keras.applications.vgg16 import  preprocess_input
from PIL import Image

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


# 训练并验证模型：
model.fit(x_train, y_train, epochs=60)
# verbose：日志显示
# verbose = 0 为不在标准输出流输出日志信息
# verbose = 1 为输出进度条记录
# verbose = 2 为每个epoch输出一行记录
print('===============')
model.evaluate(x_test,  y_test, verbose=2)


print(x_test.shape,y_test.shape)
print(type(x_test))
print(y_test)
print(x_test)
model.save('hand.h5')


# img_path = '3.bmp'
# img = load_img(img_path,target_size=(28,28))
# img = img_to_array(img)
# x = np.expand_dims(img,axis=0)
# x = preprocess_input(x)
# features = model.predict(x)
#features = features.reshape(1,7*7*512)
#result  =  model.predict_classes(features)
#print(result)


import numpy as np
#显示数据集里的图片
import matplotlib.pyplot as plt
train_data0, train_label_0 = x_train[0], y_train[0]
train_data0 = train_data0.reshape([28,28])
#print(train_data0)
plt.figure(figsize=(2,2))
plt.imshow(train_data0, cmap=plt.cm.binary)
plt.show()
print('train_data0 label is: ' + str(train_label_0))