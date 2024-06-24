from PIL import Image

image = Image.open('python-favicon.ico')

new_image = image.resize((256,256), resample=Image.Resampling.LANCZOS, reducing_gap=4)
new_image.save('python-favicon512x.ico')