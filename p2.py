import os
def search_files_by_extension(extension,directory):
    file_count=0
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(f'{extension}'):
                file_count += 1
    return file_count

def main():
    desktop_path=os.path.join(os.path.expanduser("~"),"Desktop")
    extension=input("enter the file extension(without the dot,e.g,'py' for python files):").strip()
    count=search_files_by_extension(extension,desktop_path)
    print(f"total number of files with the'{extension}'extension:{count}")
    if __name__ =="__main__":
       main()