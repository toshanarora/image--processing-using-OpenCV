import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.makedirs("outputs", exist_ok=True)
image = cv2.imread("input.jpeg")
if image is None:
    raise FileNotFoundError("input.jpg not found.")

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
def show_result(title, output, cmap=None):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    if len(image.shape) == 3:
        plt.imshow(image)
    else:
        plt.imshow(image, cmap='gray')
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    if cmap:
        plt.imshow(output, cmap=cmap)
    else:
        plt.imshow(output)
    plt.title(title)
    plt.axis("off")

    plt.tight_layout()
    plt.savefig(f"outputs/{title}.png")
    plt.close()
# 1. Brightness Adjustment
brightness = cv2.convertScaleAbs(image, alpha=1.0, beta=60)
show_result("1_Brightness_Adjustment", brightness)
# 2. Contrast Adjustment
contrast = cv2.convertScaleAbs(image, alpha=1.7, beta=0)
show_result("2_Contrast_Adjustment", contrast)
# 3. Image Negative
negative = 255 - image
show_result("3_Image_Negative", negative)
# 4. Log Transformation
c = 255 / np.log(256)
log_img = c * np.log(1 + image.astype(np.float32))
log_img = np.array(log_img, dtype=np.uint8)
show_result("4_Log_Transformation", log_img)
# 5. Gamma Transformation
gamma = 2.2
gamma_img = np.array(255 * (image / 255.0) ** gamma, dtype=np.uint8)
show_result("5_Gamma_Transformation", gamma_img)
# 6. Thresholding
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(gray,cmap='gray')
plt.title("Original Gray")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(thresh,cmap='gray')
plt.title("Threshold")
plt.axis("off")
plt.tight_layout()
plt.savefig("outputs/6_Thresholding.png")
plt.close()
# 7. Contrast Stretching
minimum = np.min(image)
maximum = np.max(image)
stretch = ((image - minimum) / (maximum - minimum) * 255).astype(np.uint8)
show_result("7_Contrast_Stretching", stretch)
# B. GEOMETRICAL TRANSFORMATIONS
rows, cols = image.shape[:2]
# 8. Translation
tx, ty = 100, 50
M = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv2.warpAffine(image, M, (cols, rows))
show_result("8_Translation", translated)
# 9. Scaling
scaled = cv2.resize(image, None, fx=1.5, fy=1.5)
show_result("9_Scaling", scaled)
# 10. Rotation
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
rotated = cv2.warpAffine(image, M, (cols, rows))
show_result("10_Rotation", rotated)
# 11. Horizontal Reflection
horizontal = cv2.flip(image, 1)
show_result("11_Horizontal_Reflection", horizontal)
# 12. Vertical Reflection
vertical = cv2.flip(image, 0)
show_result("12_Vertical_Reflection", vertical)
# 13. Reflection About Origin
origin = cv2.flip(image, -1)
show_result("13_Reflection_About_Origin", origin)
# 14. Shearing Along X-axis
M = np.float32([[1, 0.5, 0], [0, 1, 0]])
shear_x = cv2.warpAffine(image, M, (cols + 150, rows))
show_result("14_Shear_X", shear_x)
# 15. Shearing Along Y-axis
M = np.float32([[1, 0, 0], [0.5, 1, 0]])
shear_y = cv2.warpAffine(image, M, (cols, rows + 150))
show_result("15_Shear_Y", shear_y)
# 16. Affine Transformation
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
affine = cv2.warpAffine(image, M, (cols, rows))
show_result("16_Affine_Transformation", affine)
print("Done!")
print("All output images are saved in the outputs folder.")
