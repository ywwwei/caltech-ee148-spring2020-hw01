import os
import numpy as np
import json
from PIL import Image

def detect_red_light_simple(I):
    '''
    This function takes a numpy array <I> and returns a list <bounding_boxes>.
    The list <bounding_boxes> should have one element for each red light in the 
    image. Each element of <bounding_boxes> should itself be a list, containing 
    four integers that specify a bounding box: the row and column index of the 
    top left corner and the row and column index of the bottom right corner (in
    that order). See the code below for an example.
    
    Note that PIL loads images in RGB order, so:
    I[:,:,0] is the red channel
    I[:,:,1] is the green channel
    I[:,:,2] is the blue channel
    '''
    
    
    bounding_boxes = [] # This should be a list of lists, each of length 4. See format example below. 
    
    '''
    BEGIN YOUR CODE
    '''
    data_path = 'data/kernel'
    kernel = Image.open(os.path.join(data_path,'kernel1.jpg'))
    kernel = np.asarray(kernel)
    box_height = kernel.shape[0]
    box_width = kernel.shape[1]

    r_kernel = kernel[:,:,0]
    r_kernel = r_kernel / np.linalg.norm(r_kernel) # normalize
    r_I = I[:,:,0]

    threshold = 0.96
    for row in range(r_I.shape[0]-box_height):
        for col in range(r_I.shape[1]-box_width):
            r_I_part = r_I[row:row+box_height,col:col+box_width]
            r_I_part = r_I_part / np.linalg.norm(r_I_part) # normalize
            convolution = np.sum(np.multiply(r_kernel,r_I_part))
            # to avoid overlapped boxes
            if convolution > threshold and (not bounding_boxes or (row > tl_row + 5 and col > tl_col+5)):
                tl_row = row
                tl_col = col
                br_row = tl_row + box_height
                br_col = tl_col + box_width
                bounding_boxes.append([tl_row,tl_col,br_row,br_col])

    # '''
    # As an example, here's code that generates between 1 and 5 random boxes
    # of fixed size and returns the results in the proper format.
    # '''
    #
    # box_height = 8
    # box_width = 6
    #
    # num_boxes = np.random.randint(1,5)
    #
    # for i in range(num_boxes):
    #     (n_rows,n_cols,n_channels) = np.shape(I)
    #
    #     tl_row = np.random.randint(n_rows - box_height)
    #     tl_col = np.random.randint(n_cols - box_width)
    #     br_row = tl_row + box_height
    #     br_col = tl_col + box_width
    #
    #     bounding_boxes.append([tl_row,tl_col,br_row,br_col])
    
    '''
    END YOUR CODE
    '''
    
    for i in range(len(bounding_boxes)):
        assert len(bounding_boxes[i]) == 4
    
    return bounding_boxes


def detect_red_light_random(I):
    '''
    This function takes a numpy array <I> and returns a list <bounding_boxes>.
    The list <bounding_boxes> should have one element for each red light in the
    image. Each element of <bounding_boxes> should itself be a list, containing
    four integers that specify a bounding box: the row and column index of the
    top left corner and the row and column index of the bottom right corner (in
    that order). See the code below for an example.

    Note that PIL loads images in RGB order, so:
    I[:,:,0] is the red channel
    I[:,:,1] is the green channel
    I[:,:,2] is the blue channel
    '''


    bounding_boxes = [] # This should be a list of lists, each of length 4. See format example below.

    '''
    BEGIN YOUR CODE
    '''
    data_path = 'data/kernel'
    idx = np.random.randint(172)
    kernel = Image.open(os.path.join(data_path,'kernel'+str(idx+1)+'.jpg'))
    kernel = np.asarray(kernel)
    box_height = kernel.shape[0]
    box_width = kernel.shape[1]

    r_kernel = kernel[:,:,0]
    r_kernel = r_kernel / np.linalg.norm(r_kernel) # normalize
    r_I = I[:,:,0]

    threshold = 0.9
    for row in range(r_I.shape[0]-box_height):
        for col in range(r_I.shape[1]-box_width):
            r_I_part = r_I[row:row+box_height,col:col+box_width]
            r_I_part = r_I_part / np.linalg.norm(r_I_part) # normalize
            convolution = np.sum(np.multiply(r_kernel,r_I_part))
            # to avoid overlapped boxes
            if convolution > threshold and (not bounding_boxes or (row > tl_row + 5 and col > tl_col+5)):
                tl_row = row
                tl_col = col
                br_row = tl_row + box_height
                br_col = tl_col + box_width
                bounding_boxes.append([tl_row,tl_col,br_row,br_col])

    '''
    END YOUR CODE
    '''

    for i in range(len(bounding_boxes)):
        assert len(bounding_boxes[i]) == 4

    return bounding_boxes

def detect_red_light_average(I):
    '''
    This function takes a numpy array <I> and returns a list <bounding_boxes>.
    The list <bounding_boxes> should have one element for each red light in the
    image. Each element of <bounding_boxes> should itself be a list, containing
    four integers that specify a bounding box: the row and column index of the
    top left corner and the row and column index of the bottom right corner (in
    that order). See the code below for an example.

    Note that PIL loads images in RGB order, so:
    I[:,:,0] is the red channel
    I[:,:,1] is the green channel
    I[:,:,2] is the blue channel
    '''


    bounding_boxes = [] # This should be a list of lists, each of length 4. See format example below.

    '''
    BEGIN YOUR CODE
    '''
    data_path = 'data/kernel_resized'
    kernel = Image.open(os.path.join(data_path,'kernel_ave.jpg'))
    kernel = np.asarray(kernel)
    box_height = kernel.shape[0]
    box_width = kernel.shape[1]

    r_kernel = kernel[:,:,0]
    r_kernel = r_kernel / np.linalg.norm(r_kernel) # normalize
    r_I = I[:,:,0]

    threshold = 0.96
    for row in range(r_I.shape[0]-box_height):
        for col in range(r_I.shape[1]-box_width):
            r_I_part = r_I[row:row+box_height,col:col+box_width]
            r_I_part = r_I_part / np.linalg.norm(r_I_part) # normalize
            convolution = np.sum(np.multiply(r_kernel,r_I_part))
            # to avoid overlapped boxes
            if convolution > threshold and (not bounding_boxes or (row > tl_row + 5 and col > tl_col+5)):
                tl_row = row
                tl_col = col
                br_row = tl_row + box_height
                br_col = tl_col + box_width
                bounding_boxes.append([tl_row,tl_col,br_row,br_col])

    '''
    END YOUR CODE
    '''

    for i in range(len(bounding_boxes)):
        assert len(bounding_boxes[i]) == 4

    return bounding_boxes

# set the path to the downloaded data: 
data_path = 'data/RedLights2011_Medium'

# set a path for saving predictions: 
preds_path = 'data/hw01_preds'
os.makedirs(preds_path,exist_ok=True) # create directory if needed 

# get sorted list of files: 
file_names = sorted(os.listdir(data_path)) 

# remove any non-JPEG files: 
file_names = [f for f in file_names if '.jpg' in f] 

preds = {}
for i in range(len(file_names)):
    print(i)
    
    # read image using PIL:
    I = Image.open(os.path.join(data_path,file_names[i]))
    
    # convert to numpy array:
    I = np.asarray(I)
    
    preds[file_names[i]] = detect_red_light_average(I)
    print(preds[file_names[i]])

# save preds (overwrites any previous predictions!)
with open(os.path.join(preds_path,'preds_average.json'),'w') as f:
    json.dump(preds,f)




# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)
