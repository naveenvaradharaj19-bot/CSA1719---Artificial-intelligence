
# Image Segmentation

image = [
    [20, 30, 40, 200],
    [25, 35, 45, 210],
    [30, 40, 50, 220],
    [35, 45, 55, 230]
]

threshold = 100

segmented = []

for row in image:

    new_row = []

    for pixel in row:

        if pixel > threshold:
            new_row.append(1)
        else:
            new_row.append(0)

    segmented.append(new_row)

print("Segmented Image:")

for row in segmented:
    print(row)
