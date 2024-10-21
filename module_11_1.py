# Библиотека Pillow

from PIL import Image, ImageFilter


im = Image.open('pauchya_liliya.png')
print(f'ИЗОБРАЖЕНИЕ ДО ИЗМЕНЕНИЙ:\n'
      f'Расширение: {im.format}\n'
      f'Размер (в пикселях): ширина: {im.size[0]} , высота: {im.size[1]}\n'
      f'Формат: {im.mode}\n')


def change_image(image_path):
    with Image.open(image_path) as image:
        image = image.convert('RGB')                            # Преобразование изображения в «RGB»
        r, g, b = image.split()
        image = Image.merge('RGB', (b, g, r))      # Изменение цвета
        image = image.resize((2400, 1600))                      # Изменение размера
        image = image.filter(ImageFilter.DETAIL)                # Улучшение изображения
        image = image.point(lambda i: i * 2)                    # Применение точечных преобразований
        image.save('pauchya_liliya_1.jpg')                      # Сохранение нового изображения + изменение расширения

    print(f'ИЗОБРАЖЕНИЕ ПОСЛЕ ИЗМЕНЕНИЙ:\n'
          f'Расширение: {image.format}\n'
          f'Размер (в пикселях): ширина: {image.size[0]} , высота: {image.size[1]}\n'
          f'Формат: {image.mode}')


print(change_image('pauchya_liliya.png'))
