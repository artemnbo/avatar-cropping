
from PIL import Image

image = Image.open("monro.jpg")
rgb_image = image.convert("RGB")
red_channel, green_channel, blue_channel = rgb_image.split()
image_width, image_height = rgb_image.size

cropping_size = 50
transparency = 0.3

left_cropped_red_channel = red_channel.crop((cropping_size, 0, image_width, image_height))

cropped_left_and_right_red_channel = red_channel.crop((cropping_size / 2, 0, image_width - cropping_size / 2, image_height))

left_shifted_red_channel = Image.blend(left_cropped_red_channel, cropped_left_and_right_red_channel, transparency)

right_cropped_red_channel = blue_channel.crop((0, 0, image_width - cropping_size, image_height))
cropped_left_and_right_blue_channel = blue_channel.crop((cropping_size / 2, 0, image_width - cropping_size / 2, image_height))
right_shifted_red_channel = Image.blend(right_cropped_red_channel, cropped_left_and_right_blue_channel, transparency)

cropped_left_and_right_green_channel = green_channel.crop((cropping_size / 2, 0, image_width - cropping_size / 2, image_height))

styled_avatar = Image.merge("RGB", (left_shifted_red_channel, cropped_left_and_right_green_channel, right_shifted_red_channel))
styled_avatar.thumbnail((80, 80))
styled_avatar.save('styled_avatar.jpg')