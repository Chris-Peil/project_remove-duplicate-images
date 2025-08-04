import cv2
import numpy as np
import os
from pathlib import Path


#Function to collect the file names of a specific directory
def data_Collection(directory):
    count = 0                                   # Manual loop counter
    file_Names = []                             # Array for file name storage  

# loop to extract the file names from the specified directory path    
    for file in Path(directory).iterdir():      
        if file.is_file:
            file_Names.append(file)

# loop to convert the data with in the file_Names array to string    
    for word in file_Names:
        file_Names[count] = str(word)
        count += 1
          
    return(file_Names)


#Function to compare two images via their array values
def data_Comparison(file_Data):
    duplicate = 0
    position = 0
    
    # Getting the array value for the first image
    for file_a in file_Data:
        image_a = cv2.imread(file_a)
        position += 1
        
        # Getting the array value for the image to compare
        for file_b in file_Data[position:]:
            image_b = cv2.imread(file_b)
            #print(file_b)
            
            #Checks the both arrays against each other
            compare = np.array_equal(image_a, image_b)
            
            # Counter for amount of duplicates
            if compare == True:
                #print('duplicate')
                os.remove(file_a)
                break
            else:
                continue
        
        completed_Feedback = position/len(file_Data)*100
        print(round(completed_Feedback, 1), '%  Completed')



path = 'C:\\compare'
file_Names = data_Collection(path)
data_Comparison(file_Names)
