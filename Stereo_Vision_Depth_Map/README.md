# Panorama Stitching

![Estimated Depth Map](https://raw.githubusercontent.com/mcculls5/Project-Showcase/master/Stereo_Vision_Depth_Map/output/extended/tentacle_ncc.png)

## Overview
Implemented the two-view plane sweep stereo algorithm. A depth map is generated, given two calibrated images of the same scene. I extended this project to improve the resulting depth map by identifying and reducing erroneous noise in the depth estimations.


Assignment instructions may still be available here:	https://facultyweb.cs.wwu.edu/~wehrwes/courses/csci497p_20s/p3/

## Skills & Experience Gained
- Experience writing efficient python code using numpy.
- Thorough knowledge of the plane sweep stereo algorithm.
- Experience applying statistical techniques to open-ended problems.

## Contents
As this project is related to classwork, code must be omitted.
- **instructions/** : Contains the assignment instructions that outline the learning goals and tasks completed. 
- **input/** : Contains some example input images that were used to calculate depth estimations
- **output/** : Contains the resulting output depth estimations
  - **extended** : The results of my noise reduction extenion to the estimations
  - **original** : The results
- **extension.txt** : A full description of my extension
- **results.pdf** : A side by side comparison the original and extended depth map estimations.