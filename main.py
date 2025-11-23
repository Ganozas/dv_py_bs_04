from PIL import Image

image = Image.open('monro.jpg')
red, green, blue = image.split()
new_image = Image.merge('RGB',(red, green, blue))
new_image.save('monro.jpg', format='JPEG')

zeero = 0
size_crop20 = 20
size_crop40 = 40

coordinates = (zeero, zeero, red.width-size_crop40, red.height)
cropped_red_1 = red.crop(coordinates)
coordinates = (size_crop20, zeero, red.width-size_crop20, red.height)
cropped_red_2 = red.crop(coordinates)
monro_connect_red = Image.blend(cropped_red_1, cropped_red_2, 0.5)

coordinates = (size_crop40, zeero, blue.width, blue.height)
cropped_blue_1 = blue.crop(coordinates)
coordinates = (size_crop20, zeero, blue.width-size_crop20, blue.height)
cropped_blue_2 = blue.crop(coordinates)
monro_connect_blue = Image.blend(cropped_blue_1, cropped_blue_2, 0.5)

coordinates = (size_crop20, zeero, green.width-size_crop20, green.height)
monro_connect_green = green.crop(coordinates)

final_monro = Image.merge('RGB',(monro_connect_red, monro_connect_blue, monro_connect_green))
final_monro.save('final_monro.jpg', format='JPEG')

monro_icon = Image.open('final_monro.jpg')
monro_icon.thumbnail((80, 80))
monro_icon.save('monro_icon.jpg', format='JPEG')

