import tifffile as tiff
import matplotlib.pyplot as plt
image_path = './ECCO-Darwin_CO2_flux_202001.tif'
image = tiff.imread(image_path)

# Display the image
plt.imshow(image)  # Use 'gray' colormap for grayscale images
plt.axis('off')  # Hide axes
plt.show()