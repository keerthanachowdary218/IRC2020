import freenect
import cv2
import numpy as np
import math
import time
from astarsearch import astarsearch
 
#function to get RGB image from kinect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array
 
#function to get depth image from kinect
def get_depth():
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint16)
    array1 = array.astype(np.uint8)
    return array,array1

#cx = 339.7
#cy = 242.7
#fx = 594.21
#fy = 591.04

#def printcloud(depth):
	#c,r = np.meshgrid(np.arange(col), np.arange(rows), sparse = True)
	#valid = ( depth>0 ) & ( depth<255 )
	#z = np.where(valid, depth/256.0, np.nan)
	#x = np.where(valid, z * (c-cx)/fx, 0)
	#y = np.where(valid, z * (r-cy)/fy, 0)
	#return np.dstack((x,y,z))

if __name__ == "__main__":
    while 1:
	#get a frame from RGB camera
        frame = get_video()
 	depth,depth1= get_depth()
	p=depth[240,:]
	#x = 0.1236 * math.tan(p/ 2842.5 + 1.1863)
        z=100/(-0.00307 * p + 3.33)
        print(z) 
	 
	s=[]
	#for i in x:
		#s.append(i)
	 
	#ke=np.array(s)
        #ke=ke.astype(int)
	#print(ke)
	j=0    
	while j<640: 
		for k in range (j+1,640):
			if z[j]>0:
				if z[k]>=z[j]-5 and z[k]<=z[j]+5:
					continue
				else: 	
				
					print(str(j) + ',' + str(k-1)+':'+str(z[k-1]))
					a = [j,k-1,z[k-1]]
					if k-1-j>=10 and a[2]<=500:
						s.append(a)
					j = k
					break
			else:
				j = j+1
      			
		if j==639:
			break
		      
	print(s)
	rows, cols = (5, 640) 
	matrix = np.zeros([5,640] ,dtype = int)
	for i in range(len(s)):
		col1 = s[i][0]
		col2 = s[i][1]
                row = 0
		j = col1
		if s[i][2]<=100:
			row = 0
			while j>=col1 and j<=col2:
				matrix[row][j]=1
				j = j+1
			
		elif s[i][2]<=200 and s[i][2]>100:
			row = 1
			while j>=col1 and j<=col2:
				matrix[row][j]=1
				j = j+1
			
			
		elif s[i][2]<=300 and s[i][2]>200:
			row = 2
			while j>=col1 and j<=col2:
				matrix[row][j]=1
				j = j+1
		
			
		elif s[i][2]<=400 and s[i][2]>300:
			row = 3
			while j>=col1 and j<=col2:
				matrix[row][j]=1
				j = j+1
			
			
		elif s[i][2]<=500 and s[i][2]>400:
			row = 4
			while j>=col1 and j<=col2:
				matrix[row][j]=1
				j = j+1	
	for ro in matrix:
		print(ro)
	
	rows, cols = (5, 10) 
	mat = np.zeros([5,10] ,dtype = int)
	for i in range(0,5):
                #p=0
		a=0
		for j in range(0,64):
			if matrix[i][j]==1:
				a=a+1
			if a>30:
				mat[i][0]=1
		a=0
		for j in range(64,128):
			if matrix[i][j]==1:
				a=a+1
			if a>30:
				mat[i][1]=1
		a=0
		for j in range(128,192):
			if matrix[i][j]==1:
				a=a+1
			if a>30:
				mat[i][2]=1
		a=0
		for j in range(192,256):
			if matrix[i][j]==1:
				a=a+1
			if a>30:
				mat[i][3]=1
		a=0
		for j in range(256,320):
			if matrix[i][j]==1:
				a=a+1
			if a>30:
				mat[i][4]=1
		a=0
		for j in range(320,384):
			if matrix[i][j]==1:
				a=a+1
			if a>30:
				mat[i][5]=1
		a=0
		for j in range(384,448):
			if matrix[i][j]==1:
				a=a+1
			if a>30:
				mat[i][6]=1
		a=0
		for j in range(448,512):
			if matrix[i][j]==1:
				a=a+1
			if a>30:
				mat[i][7]=1
		a=0
		for j in range(512,576):
			if matrix[i][j]==1:
				a=a+1
			if a>30:
				mat[i][8]=1
		a=0
		for j in range(576,640):
			if matrix[i][j]==1:
				a=a+1
			if a>30:
				mat[i][9]=1

				








			#k = 0
			#if p<=9:
			#	while j < (p+1)*64:
			#		print(j)
			#		if matrix[i][j]==1:
			#			k = k + 1
			#		j = j+1
			#	if k>30:
			#		mat[i][p] = 1	
			#	else:
			#		mat[i][p] = 0
			#	p = p+1
			
					
	print(mat)		
	result = astarsearch(mat,(0,0),(9,4))
	print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
	print(result)
	#for i in range(len(result))
	# Draw a diagonal blue line with thickness of 5 px
        depth1=cv2.line(depth1,(0,240),(640,240),(0,255,0),1)
        depth1=cv2.line(depth1,(320,0),(320,480),(0,255,0),1)
        cv2.imshow('Depth image',depth1)		
        cv2.imshow('RGB image',frame)
	#time.sleep(5)
        k = cv2.waitKey(3000)
        if k == 27:
        	break
cv2.destroyAllWindows()

