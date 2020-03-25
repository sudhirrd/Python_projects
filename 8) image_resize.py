from PIL import Image
import os

def ImageResizer(path, size=(200, 200), new_name=None, new_location=None, quality=90):
    if(os.path.isfile(path)):
        image = Image.open(path)
        image_name, image_ext = os.path.splitext(path)
        image_resized = image.resize(size, Image.ANTIALIAS)
        
        location = image_name.split("\\")[:-1]
        location = "\\".join(location)
        if(new_location):
             location = new_location
        
        if(new_name):
            final_location = location + "\\" + new_name
        else:
            final_location = image_name + "_new size"
        image_resized.save(final_location + image_ext, quality=quality)
        print("IMAGE HAS BEEN RESIZED SUCCESSFULLY.....")
    else:
        print("This is not a address of file")
    

path = "C:\\Users\\Game Changer\\Desktop\\Spyder\\IMAGES\\solo photo.jpg"
ImageResizer(path, size=(500, 500), new_name="NEW PHOTO", new_location="C:\Intel")



def ImageResizer_Bunch(path, size=(200, 200), new_location=None, quality=90):
    items = os.listdir(path)
    # listing all image items names into items
    for item in items: # iterate rhrough all items
        image_path = path + item
        # get full path of image
        if(os.path.isfile(image_path)):
            # checking image_name is existing regular file or not
            image = Image.open(image_path)
            image_name, image_ext = os.path.splitext(image_path)
            image_resized = image.resize(size, Image.ANTIALIAS)
            image_resized.save(image_name + "_new size." + image_ext, quality=90)
    print("ALL IMAGES HAVE BEEN RESIZED SUCCESSFULLY.....")

path = "C:\\Users\\Game Changer\\Desktop\\Spyder\\IMAGES\\"
ImageResizer_Bunch(path)












