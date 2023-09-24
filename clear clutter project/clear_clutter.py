import os

class FileRenamer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.counter = 1

    def rename_files(self):
        os.chdir(self.folder_path)
        file_list = os.listdir(self.folder_path)
        png_files = [file for file in file_list if file.endswith(".png")]

        for old_file in png_files:
            new_file = f"{self.counter}.png"
            old_path = os.path.join(os.getcwd(), old_file)
            new_path = os.path.join(os.getcwd(), new_file)
            os.rename(old_path, new_path)
            self.counter += 1

if __name__ == "__main__":
    os.chdir("./clear clutter project")
    folder_path = os.getcwd()
    renamer = FileRenamer(folder_path)
    renamer.rename_files()

