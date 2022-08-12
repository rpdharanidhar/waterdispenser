import kivy_code
from kivy_code import SecondWindow

def New_Folder(name):
    import os

    # Directory
    directory = name

    # Parent Directory path
    parent_dir = 'D:\WaterDispenserRecord\{}'.format(directory)


    # Path
    #path = os.path.join(parent_dir)

    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    os.mkdir(parent_dir)
    print("Directory '% s' created" % directory)

#name = SecondWindow.a
#New_Folder(name)
