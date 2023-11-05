#!/usr/bin/env python
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import cv2
import numpy as np
  
def doloop():
    global depth, rgb
    while True:
        # Get a fresh frame
        (depth,_), (rgb,_) = get_depth(), get_video()
        
        # Build a two panel color image
        d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
        da = np.hstack((d3,rgb))
        cv2.imwrite('depth'+str(0)+'.jpg',d3)
        # Simple Downsample
        cv2.imshow('both',np.array(d3))
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
doloop()
freenect_shutdown()
cv2.destroyAllWindows()
"""
IPython usage:
 ipython
 [1]: run -i demo_freenect
 #<ctrl -c>  (to interrupt the loop)
 [2]: %timeit -n100 get_depth(), get_rgb() # profile the kinect capture

"""

