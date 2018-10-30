import sys, os


PATH = r"C:\Users\Bartek\Desktop\test"


def search_for_files(pth):
    list_of_files = []
    for file in os.listdir(pth):
        if os.path.isdir(os.path.join(pth,file)):
            pass
        elif os.path.isfile(os.path.join(pth,file)):
            list_of_files.append(os.path.basename(file))
    return list_of_files

if __name__ == "__main__":
    list_of_files = search_for_files(PATH)
    for i in list_of_files:
        print(i)