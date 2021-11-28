# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# 标签	类
# 0	T恤/上衣
# 1	裤子
# 2	套头衫
# 3	连衣裙
# 4	外套
# 5	凉鞋
# 6	衬衫
# 7	运动鞋
# 8	包
# 9	短靴

class_names = ['T恤/上衣', '裤子', '套头衫', '连衣裙', '外套',
               '凉鞋', '衬衫', '运动鞋', '包', '短靴']

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images = train_images / 255.0

test_images = test_images / 255.0


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

#model.fit(train_images, train_labels, epochs=10)

model.load_weights('fashion.h5')


# 评估准确率
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model,
                                         tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)

print(np.argmax(predictions[0]))



#验证预测结果
#在模型经过训练后，您可以使用它对一些图像进行预测。


#使用训练好的模型
#最后，使用训练好的模型对单个图像进行预测。
# Grab an image from the test dataset.
img = test_images[2]
print(img.shape)

plt.figure()
plt.imshow(img)
plt.colorbar()
plt.grid(False)
plt.show()
#tf.keras 模型经过了优化，可同时对一个批或一组样本进行预测。因此，即便您只使用一个图像，您也需要将其添加到列表中：
# Add the image to a batch where it's the only member.
img = (np.expand_dims(img,0))
print(img.shape)

#现在预测这个图像的正确标签：
predictions_single = probability_model.predict(img)
print(predictions_single)

print(np.argmax(predictions_single[0]))
print(class_names[np.argmax(predictions_single[0])])