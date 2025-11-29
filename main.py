from PIL import Image

image = Image.open('monro.jpg')
red, green, blue = image.split()

zeero = 0
size_crop30 = 30
size_crop60 = 60

coordinates = (size_crop60, zeero, red.width, red.height)
cropped_red_1 = red.crop(coordinates)
coordinates = (size_crop30, zeero, red.width-size_crop30, red.height)
cropped_red_2 = red.crop(coordinates)
monro_connect_red = Image.blend(cropped_red_1, cropped_red_2, 0.5)

coordinates = (zeero, zeero, blue.width-size_crop60, blue.height)
cropped_blue_1 = blue.crop(coordinates)
coordinates = (size_crop30, zeero, blue.width-size_crop30, blue.height)
cropped_blue_2 = blue.crop(coordinates)
monro_connect_blue = Image.blend(cropped_blue_1, cropped_blue_2, 0.5)

coordinates = (size_crop30, zeero, green.width-size_crop30, green.height)
monro_connect_green = green.crop(coordinates)

final_monro = Image.merge('RGB',(monro_connect_red, monro_connect_green, monro_connect_blue))
final_monro.save('final_monro.jpg', format='JPEG')

monro_icon = Image.open('final_monro.jpg')
monro_icon.thumbnail((80, 80))
monro_icon.save('monro_icon.jpg', format='JPEG')

