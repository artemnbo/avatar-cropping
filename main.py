from PIL import Image

image = Image.open("monro.jpg")
rgb_image = image.convert("RGB")
red_channel, green_channel, blue_channel = rgb_image.split()

red_channel.save('monro_red.jpg')
green_channel.save('monro_green.jpg')
blue_channel.save('monro_blue.jpg')

new_image = Image.merge("RGB", (red_channel, green_channel, blue_channel))
new_image.save('monro_new.jpg')

# red_channel_image = Image.open('monro_red.jpg')

# cropped_1 = red_channel_image.crop(200, )

# blended_channel_image = Image.blend(cropped, red_channel_image, 0.5)
# blended_channel_image.save('monro_red_blended.jpg')

# print(f'Ширина — {red_channel_image.width}')
# print(f'Высота — {red_channel_image.height}')
# print(f'Цветовая модель — {red_channel_image.mode}')