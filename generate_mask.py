import numpy as np
from PIL import Image
import math

# Image dimensions
width = 512
height = 512

# Stripe parameters
stripe_width = 20  # pixels
angle = 20  # degrees

# Convert angle to radians
angle_rad = math.radians(angle)

# Create a blank image array
img_array = np.zeros((height, width), dtype=np.uint8)

# Calculate the perpendicular distance from origin for each pixel
# For a line at angle θ, the perpendicular distance from origin is: x*cos(θ) + y*sin(θ)
for y in range(height):
    for x in range(width):
        # Calculate perpendicular distance from the origin
        distance = x * math.cos(angle_rad) + y * math.sin(angle_rad)

        # Determine which stripe this pixel belongs to
        stripe_index = int(distance / stripe_width)

        # Alternate between black (0) and white (255)
        if stripe_index % 2 == 0:
            img_array[y, x] = 255  # White
        else:
            img_array[y, x] = 0  # Black

# Create image from array
img = Image.fromarray(img_array, mode="L")

# Save the image
output_path = "mask.png"
img.save(output_path)

print(f"Image saved successfully to {output_path}")
print(f"Image size: {width}x{height}")
print(f"Stripe width: {stripe_width} pixels")
print(f"Angle: {angle} degrees")
