from config.settings import FILE_PATH

def write(content, fileAdapter):
    path = FILE_PATH
    fileAdapter.write(content, path)