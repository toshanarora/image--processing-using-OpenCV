# Image Processing with OpenCV

A small Python project that runs a bunch of classic image processing operations on a single input image and saves a "before vs after" comparison for each one.

I built this to get a hands-on feel for how pixel values and image coordinates actually get manipulated under the hood :instead of just reading about it. It covers both intensity-based operations (brightness, contrast, thresholding, etc.) and geometric transformations (rotation, scaling, shearing, and so on) — 16 operations in total.

---

## What it does

Feed it an image called `input.jpeg`, and it runs through:

- Brightness adjustment
- Contrast adjustment
- Image negative
- Log transformation
- Gamma transformation
- Thresholding
- Contrast stretching
- Translation
- Scaling
- Rotation
- Horizontal reflection
- Vertical reflection
- Reflection about origin
- Shear (X-axis)
- Shear (Y-axis)
- Affine transformation

Every operation gets its own output image with the original and the processed version side by side, so you can actually see what changed. Everything lands in an `outputs/` folder that the script creates for you.

---

## Built with

- Python
- OpenCV (`cv2`)
- NumPy
- Matplotlib

---

## Project layout

```
Image_Processing/
│
├── input.jpeg
├── image_processing.py
├── README.md
│
└── outputs/
    ├── 1_Brightness_Adjustment.png
    ├── 2_Contrast_Adjustment.png
    ├── 3_Image_Negative.png
    ├── 4_Log_Transformation.png
    ├── 5_Gamma_Transformation.png
    ├── 6_Thresholding.png
    ├── 7_Contrast_Stretching.png
    ├── 8_Translation.png
    ├── 9_Scaling.png
    ├── 10_Rotation.png
    ├── 11_Horizontal_Reflection.png
    ├── 12_Vertical_Reflection.png
    ├── 13_Reflection_About_Origin.png
    ├── 14_Shear_X.png
    ├── 15_Shear_Y.png
    └── 16_Affine_Transformation.png
```

---

## Setup

You'll need Python installed. Then grab the dependencies:

```bash
pip install opencv-python numpy matplotlib
```

Prefer a virtual environment? Here's the quick version:

```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
pip install opencv-python numpy matplotlib
```

**macOS / Linux**
```bash
source venv/bin/activate
pip install opencv-python numpy matplotlib
```

---

## Running it

1. Drop your image into the project folder and rename it to `input.jpeg`.
2. Run:
   ```bash
   python image_processing.py
   ```
3. That's it — an `outputs/` folder gets created automatically, and every processed image ends up in there.

You'll know it worked when you see:

```
Done!
All output images are saved in the outputs folder.
```

---

## How each operation works

### Intensity transformations

**1. Brightness adjustment**
Adds a constant value to every pixel to make the image brighter.
```python
cv2.convertScaleAbs(image, alpha=1.0, beta=60)
```
`beta` controls how much brighter it gets.

**2. Contrast adjustment**
Multiplies pixel values by a scaling factor instead of adding to them.
```python
cv2.convertScaleAbs(image, alpha=1.7, beta=0)
```
Bumping `alpha` up to 1.7 pushes the contrast higher.

**3. Image negative**
Straightforward inversion — dark becomes light and vice versa.
```python
negative = 255 - image
```

**4. Log transformation**
Pulls out detail that's hiding in the darker parts of the image, following:
```
s = c × log(1 + r)
```
where `r` is the input pixel value and `c` is a scaling constant.

**5. Gamma transformation**
Non-linear brightness correction, defined as:
```
s = 255 × (r / 255)^γ
```
This project uses `gamma = 2.2`, which is a common value for correcting how brightness is perceived.

**6. Thresholding**
Turns a grayscale image into pure black and white.
```python
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
```
Anything above 127 goes white, anything below goes black.

**7. Contrast stretching**
Finds the darkest and brightest pixels in the image and stretches that range out to the full 0–255 scale — useful for images that look washed out or flat.

### Geometric transformations

**8. Translation**
Shifts the whole image — 100 pixels along X, 50 pixels along Y in this case.
```python
tx = 100
ty = 50
```

**9. Scaling**
Resizes the image by a factor of 1.5 in both directions.
```python
cv2.resize(image, None, fx=1.5, fy=1.5)
```

**10. Rotation**
Rotates the image 45° around its center point.
```python
cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
```

**11–13. Reflections**
Three flavors of flipping the image:
```python
cv2.flip(image, 1)   # horizontal
cv2.flip(image, 0)   # vertical
cv2.flip(image, -1)  # both — equivalent to reflecting about the origin
```

**14. Shear (X-axis)**
Shifts pixels sideways based on how high or low they are.
```
[ 1   0.5   0 ]
[ 0    1    0 ]
```

**15. Shear (Y-axis)**
Same idea, flipped — shifts pixels up/down based on horizontal position.
```
[ 1    0    0 ]
[ 0.5  1    0 ]
```

**16. Affine transformation**
Maps three points from the original image to three new points, which preserves straight lines, parallel lines, and the ratios of distances along a line — even though angles and lengths can change.
```python
cv2.getAffineTransform(pts1, pts2)
cv2.warpAffine(image, matrix, (cols, rows))
```

---

## Output

Every single operation writes out one PNG with the original image next to the processed one, so the effect is easy to compare at a glance.

---

## Takeaway

This was mostly an exercise in getting comfortable with how images are represented as arrays of numbers, and how simple math on those numbers — adding, multiplying, remapping coordinates — produces effects that look complex on the surface. Intensity transformations change *what the pixel values are*; geometric transformations change *where those pixels end up*. Once that distinction clicks, most of image processing starts to feel a lot less like magic.

---

## Author

**Toshan Arora**
B.Tech – Artificial Intelligence & Machine Learning
