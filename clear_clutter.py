import os

class FileRenamer:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def rename_files(self):
        files = os.listdir(self.folder_path)
        i=1
        for file in files:
            if file.endswith(".pdf"):
                print(file)
                os.rename(f"{file}", f"{i}.pdf")
                i = i + 1
        

if __name__ == "__main__":
    folder_path = os.getcwd()
    renamer = FileRenamer(folder_path)
    renamer.rename_files()

