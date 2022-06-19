from PIL import Image, ImageFilter

img = Image.open('./image-playground/pokedox/pikachu.jpg')

print(img)
print(img.format)
print(img.format_description)
print(img.mode)
print(img.size)

# In this image processing we can rotate our image also.

rotated_img = img.rotate(180)
rotated_img.save('rotate.png', 'png')

# In this image processing we can Re-size our image also.

resize_img = img.resize((200, 200))
resize_img.save('re-size.png', 'png')

# In this image processing we can crop our image also.

box = [100, 100, 400, 400]
crop_img = img.crop(box)
crop_img.save('crop.png', 'png')


# In this image processing we can do some different stuff also like we can add some filter
# or we can converted in grey scal.

filtered_img = img.filter(ImageFilter.MedianFilter)
# While we are using filter like (blur,sharpan,smooth) we need to convert file in to "png".
filtered_img.save('median.png', 'png')

# If we need to convert img in grey scal then we can do that also by using convert command.

converted_img = img.convert('L')  # "L" use to convert img in grey scal.
converted_img.save('grey.png', 'png')
