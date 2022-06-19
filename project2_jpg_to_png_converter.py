from PIL import Image

img = Image.open(
    './image-playground/pokedox/bulbasaur.jpg').convert('RGB')

img.save('bulbasaur.png', 'png')
print('All done!')

img = Image.open(
    './image-playground/pokedox/charmander.jpg').convert('RGB')

img.save('charmander.png', 'png')
print('All done!')


img = Image.open(
    './image-playground/pokedox/squirtle.jpg').convert('RGB')

img.save('squirtle.png', 'png')
print('All done!')
