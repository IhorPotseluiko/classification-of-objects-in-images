"""black and white"""
import numpy as np
######################################################to the test#########################################
import os
from PIL import Image
def gradation_card_1(root, photo_array):
    """
    black and white

    :param root: C:/Users/ggh76/Desktop/recognition_of_cats_and_dogs/data/test_set/
    :param photo_array: [{'filename': 'cat.3269.jpg', 'folder_name': 'cats'}, ... ]
    :return:
    """

    # Перебрати всі файли у папці
    for cell in photo_array:
        photo_folder = root + cell['folder_name'] + '/'
        for i in range(len(photo_array)):
            filename = cell['filename']
            if filename.endswith('.jpg'):
                photo_path = os.path.join(photo_folder, filename)
                photo = Image.open(photo_path)
                photo_data = np.array(photo)  # Змінено ім'я змінної на photo_data
                cell['2Darray'] = np.mean(photo_data, axis=2).astype(np.uint8)

    return photo_array
qwe = [{'filename': 'cat.1539.jpg', 'folder_name': 'cats'}, {'filename': 'cat.2200.jpg', 'folder_name': 'cats'}]
asd = gradation_card_1('C:/Users/ggh76/Desktop/recognition_of_cats_and_dogs/data/training_set/', qwe)
print(asd)


############################################################################################################

def model_CNN(portion):


    for i in range(len(portion)):
        arr = portion[i]['2Darray']
        shape = arr.shape - [1, 1]
        for y in range(1, shape[0]):
            for x in range(1, shape[1]):

                a = 1
    return 1


# Припустимо, що у нас є вхідне зображення (представлене у вигляді NumPy-масиву)
input_image = np.array([[1, 1, 1, 0, 0],
                       [0, 1, 1, 1, 0],
                       [0, 0, 1, 1, 1],
                       [0, 0, 1, 1, 0],
                       [0, 1, 1, 0, 0]])

# Згорткове ядро (фільтр)
kernel = np.array([[1, 0, -1],
                   [1, 0, -1],
                   [1, 0, -1]])

# Згортка (конволюція)
def convolution(image, kernel):
    i_h, i_w = image.shape
    k_h, k_w = kernel.shape
    o_h, o_w = i_h - k_h + 1, i_w - k_w + 1
    output = np.zeros((o_h, o_w))
    for i in range(o_h):
        for j in range(o_w):
            output[i, j] = np.sum(image[i:i+k_h, j:j+k_w] * kernel)
    return output

# Застосуємо згортку до вхідного зображення
conv_result = convolution(input_image, kernel)
print("Результат згортки:")
print(conv_result)

# Пулінг (максимальне значення)
def max_pooling(image, pool_size):
    i_h, i_w = image.shape
    p_h, p_w = i_h // pool_size, i_w // pool_size
    output = np.zeros((p_h, p_w))
    for i in range(p_h):
        for j in range(p_w):
            output[i, j] = np.max(image[i*pool_size:(i+1)*pool_size, j*pool_size:(j+1)*pool_size])
    return output

# Застосуємо пулінг до результату згортки
pool_size = 2
pool_result = max_pooling(conv_result, pool_size)
print("Результат пулінгу:")
print(pool_result)

