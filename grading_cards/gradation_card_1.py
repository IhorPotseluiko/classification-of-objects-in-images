from PIL import Image
import numpy as np
import os
import random

# створення списку
def photos_in_folders_list(root, photo_folders):
    """

    :param root: C:/Users/ggh76/Desktop/recognition_of_cats_and_dogs/data/test_set/
    :param photo_folders: [cats, dogs]
    :return:
    """
    photos_in_folders_list = []
    for folder in photo_folders:
        photo_folder = root + folder
        for filename in os.listdir(photo_folder):
            dict_list = {}
            dict_list['filename'] = filename
            dict_list['folder_name'] = folder
            photos_in_folders_list.append(dict_list)
    return photos_in_folders_list

# взяття рандомних фотографій з масиву
def random_taking_and_removing(array, number):
    """

    :param array: масив фотографій
    :param number: кількість фотографій які будуть взяті та ремувнуті
    :return: повертає оновлений масив фотогафій та список ремувнутих елементів
    """
    #random_photos = random.sample(array, number)
    random_photos = []
    for i in range(number):
        random_photos.append(array.pop(random.randint(0, len(array)-1)))
    #for photo in random_photos:
    #    array.remove(photo)
    return array, random_photos


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
        print(photo_folder)
        for i in range(len(photo_array)):
            print(i)
            filename = cell['filename']
            print('filename', filename)
            if filename.endswith('.jpg'):
                photo_path = os.path.join(photo_folder, filename)
                print("photo_path", photo_path)
                photo = Image.open(photo_path)
                photo_data = np.array(photo)  # Змінено ім'я змінної на photo_data
                cell['2Darray'] = np.mean(photo_data, axis=2).astype(np.uint8)

    return photo_array


"""qwe = [{'filename': 'cat.1539.jpg', 'folder_name': 'cats'}, {'filename': 'cat.2200.jpg', 'folder_name': 'cats'}]
print(len(qwe))
asd = gradation_card_1('C:/Users/ggh76/Desktop/recognition_of_cats_and_dogs/data/training_set/', qwe)
print(asd)
print(len(asd))"""

"""# Завантажте зображення
img = Image.open("C:/Users/ggh76/Desktop/recognition_of_cats_and_dogs/for_experiments/" + filename)
# Перетворення фотографії у формат NumPy масиву
image_array = np.array(img)
#print("image_array = ", image_array)
# Отримання градаційної картки (яскравості)
return np.mean(image_array, axis=2).astype(np.uint8)"""



#print("grayscale_image = ", gradation_card_1("cat.4001.jpg"))
# Створення градаційної картки з отриманого масиву
#grayscale_image = Image.fromarray(grayscale_image_array)
#print(grayscale_image)

"""# Перетворення в чорно-білий формат
bw_img = img.convert("L")

# Збереження перетвореного зображення
bw_img.save("black_and_white_foto_1.jpg")

# Виведення зображення (необов'язково)
bw_img.show()"""