
import os
import cv2

class ObstacleDetectionDataset:
    def __init__(self, image_dir, label_dir):
        """
        Initializes the dataset by mapping out the file paths for your 
        images and their corresponding YOLO text labels.
        """
        self.image_dir = image_dir ## here to save the path dirction of image
        self.label_dir = label_dir ## here to save the path dirction of labels
        
        # Sort them to ensure they align
        self.image_files = sorted(os.listdir(image_dir)) 
        self.label_files = sorted(os.listdir(label_dir))
        
        # A quick sanity check to ensure no labels or images are missing
        assert len(self.image_files) == len(self.label_files), "Mismatch in number of images and labels!"

    def __len__(self):
        """Returns the total number of images in the dataset."""
        return len(self.image_files)

    def __getitem__(self, index):
        """
        Fetches the image and label for the requested index on the fly.
        """
        image_name = self.image_files[index]
        label_name = self.label_files[index]
        
        # An extra safety check: ensure the base names match perfectly, 
        # ignoring the file extensions (e.g., 'IMG_00001' == 'IMG_00001')
        assert image_name.split('.')[0] == label_name.split('.')[0], f"Name mismatch: {image_name} vs {label_name}"
        
        # 1. Build the full paths
        image_path = os.path.join(self.image_dir, image_name)
        label_path = os.path.join(self.label_dir, label_name)
        
      
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        ## here the boundry of each image 
        with open(label_path, 'r', encoding='utf-8') as f:
            
            label_data = [line.strip().split() for line in f.readlines() ]
            label_data=[float(elemnts) for elemnts in label_data[0] ]

        return image, label_data