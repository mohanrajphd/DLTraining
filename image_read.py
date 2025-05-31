import cv2

image_path = '20.png'

image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Image at path '{image_path}' could not be read. Please check the file path.")

print(image.shape)
image_color = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_resize = cv2.resize(image, (299, 299))
cv2.imshow('Processed Image', image_resize)
cv2.waitKey(0)