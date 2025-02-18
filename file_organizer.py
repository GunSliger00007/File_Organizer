import os
import shutil

# define the directory you want tpo 
TARGET_DIRECTORY='/home/gehendrachaudhary/Downloads/'

#deifne the file type of with categories
FILE_TYPES = {
    'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.ppt', '.pptx', '.xls', '.xlsx', '.csv'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    'Music': ['.mp3', '.wav', '.flac', '.aac'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'Scripts': ['.py', '.sh', '.js', '.php', '.html', '.css'],
    'Others': []
}

#create necessary folders if doesnt exists

def create_folders(directory):
    for folder in FILE_TYPES.keys():
        folder_path=os.path.join(directory,folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
#move files to respective folders based on their file extemsion

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path=os.path.join(directory,filename)
        
        if os.path.isdir(file_path):
            continue
        
        file_extension=os.path.splitext(filename)[1].lower()
        moved=False
        for folder,extensions in FILE_TYPES.items():
            if file_extension in extensions:
                shutil.move(file_path,os.path.join(directory,folder,filename))
                print(f"Moved: {filename}->{folder}")
                moved=True
                break

        if not moved:
            shutil.move(file_path, os.path.join(directory, 'Others', filename))
            print(f"Moved: {filename} -> Others")
if __name__ == "__main__":
    # Step 1: Create the folders (Images, Documents, Videos, etc.)
    create_folders(TARGET_DIRECTORY)

    # Step 2: Organize files into the corresponding folders
    organize_files(TARGET_DIRECTORY)

    print("File organization complete!")