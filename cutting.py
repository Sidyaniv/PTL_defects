import cv2
import os

def crop_images(input_dir, crop_width=280, crop_height=1024):
    # Убедимся, что папка для сохранения существует
    # os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        # Проверка, что файл является изображением
        if not (filename.endswith('.jpg') or filename.endswith('.png')
                or filename.endswith('.jpeg') or filename.endswith('.tiff')
                or filename.endswith('.tif')):
            continue

        # Чтение изображения
        img = cv2.imread(file_path)

        if img.shape != (1024, 280, 3):  
            if img is None:
                print(f"Ошибка чтения {file_path}")
                continue

            # Получение размеров исходного изображения
            height, width, _ = img.shape

            # Проверка, что изображение достаточно велико для обрезки
            if width < crop_width or height < crop_height:
                print(f"Изображение {filename} меньше целевого размера обрезки.")
                continue

            # Вычисление координат для обрезки
            x_center = width // 2
            y_center = height // 2
            x_start = x_center - crop_width // 2
            y_start = y_center - crop_height // 2

            # Выполнение обрезки
            cropped_img = img[y_start:y_start+crop_height, x_start:x_start+crop_width]

            # Сохранение обрезанного изображения
            # output_path = os.path.join(output_dir, filename)
            # cv2.imwrite(output_path, cropped_img)

            cv2.imwrite(file_path, cropped_img)
            print(f"Изображение {filename} успешно обработано и сохранено в {file_path}")
            # break # delete this



input_directory = "/home/asilyanov/Desktop/defects"
# output_directory = "/home/asilyanov/Desktop/defects/cropped"
crop_images(input_directory, crop_width=280, crop_height=1024)
