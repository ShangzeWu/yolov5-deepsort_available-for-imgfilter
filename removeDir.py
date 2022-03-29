import os

def remove_empty_dir(path):
    for (root, dirs, files) in os.walk(path, topdown=False):
        for item in dirs:
            dir = os.path.join(root, item)
            try:
                os.rmdir(dir)
                print(dir)
            except Exception as e:
                pass

if __name__ == '__main__':
    path = '/mnt/a'
    remove_empty_dir(path)