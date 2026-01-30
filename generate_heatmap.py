"""
@author: Fjorda
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter
import pandas as pd
pd.options.display.float_format = '{:.3f}'.format
##################     Original Image  #######################
cover_img = plt.imread('PanoramaSc1.jpg')

print("Cover Reference Image")
plt.figure(figsize=(8,8))
plt.imshow(cover_img)
plt.axis('off');

##################     Heat mapp image  #######################
dataGaze = pd.read_csv('fixations.csv')
heads    = dataGaze .columns

gaze_on_surf_x = dataGaze.norm_pos_x + 0.12 # gaze_point_3d_x
gaze_on_surf_y = dataGaze.norm_pos_y + .15 #norm_pos_y

grid = cover_img.shape[0:2] # height, width of the loaded image
heatmap_detail = 0.05 # this will determine the gaussian blur kerner of the image (higher number = more blur)

# flip the fixation points
# from the original coordinate system,
# where the origin is at botton left,
# to the image coordinate system,
# where the origin is at top left
gaze_on_surf_y = 1 - gaze_on_surf_y

# make the histogram
hist, x_edges, y_edges = np.histogram2d(
    gaze_on_surf_y,
    gaze_on_surf_x,
    range=[[0, 1.0], [0, 1.0]],
    normed=False,
    bins=grid
)

# gaussian blur kernel as a function of grid/surface size
filter_h = int(heatmap_detail * grid[0])# // 2 * 2 + 1
filter_w = int(heatmap_detail * grid[1])# // 2 * 2 + 1
heatmap = gaussian_filter(hist, sigma=(filter_w, filter_h), order=0)

# display the histogram and reference image
print("Cover image with heatmap overlay")
plt.figure(figsize=(20,20))
plt.imshow(cover_img)
plt.imshow(heatmap, cmap='jet', alpha=0.5)
plt.axis('off');