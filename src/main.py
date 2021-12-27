import os
import shutil


def sortFiles():

    path = input("Enter file path:")
    files = os.listdir(path)

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path+"/"+extension):
            shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
            print("Moved "+file + " to " + extension + " folder.")

        else:
            os.makedirs(path+"/"+extension)
            print("Made new folder called " + extension)
            shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
            print("Moved "+file + " to " + extension + " folder.")


if __name__ == "__main__":
    sortFiles()
