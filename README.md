Requirements:
-Panoramic Image created from your VR task
-Data in a csv format
-Timestamps included in your data
-Anaconda Python Development Environment

Step 1 Panoramic Image
Let's assume that we have created a task in VR and from this task we generated a panoramic image of the whole 3D environment. For this tutorial I created a task in Unity in VR and I generated from Unity a panoramic image. From the task I generated a panoramic image.

Step 2 Data
Let's assume that we have pupil labs eye tracker and we collected a large volume of data from users eyes and we also have the panoramic image. We want now to generate the heatmap from fixations data. Heatmaps are generated during fixations.

The fixations file has two important variables that we will use which are: "norm_pos_x" and "norm_pos_y" Those variable are x y position in the world image frame in normalized coordinates. We will need the normalized coordinates to intersect those with image coordinates. 

Step 3 Python Setup
To write a python script we need a platform. We can use Spyder although there are other platforms to write python scripts. To have access to Spyder it is recommended to download first Anaconda. After the download has been completed, you can run Anaconda and lunch Spyder. If the launch button does not show but an Install button shows instead, make sure to install Spyder and then run it. After you open Spyder, you can create a new file and save the file in the same directory where your data and panoramic image is located. Now we are ready to start coding.

Step 4 Generate heatmap into panoramic image from fixations data.
Now we can write a python script that utilizes the norm_pos_x and norm_pos_y to generate the heatmap. IMPORTANT: The two lines of the code below: gaze_on_surf_x = dataGaze.norm_pos_x + 0.12 , gaze_on_surf_y = dataGaze.norm_pos_y + .15 Need to be changed according to the part of the image that was in front of the user in VR. Therefore you need to change those coordinates 0.12 and .15 to position the heatmap in the area or part of the image that was in front of the user in VR.
