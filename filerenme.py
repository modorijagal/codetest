import os


file_path = "F:\\torrent_download\\[멜론] 2021년 12월 16일 실시간 TOP100 [320Kbps]"
file_names = os.listdir(file_path)
file_names

#print (file_names[0])
#print("Hello world")

for fname in file_names:
    #print(fname)
    path, ext = os.path.splitext(fname)
    ''' print(path)
    print("================")
    print(path.replace(" -  - 구글검색 토렌트노리", ""))
    print("================")
    print(ext) '''

    new_string = path.replace(" -  - 구글검색 토렌트노리", "")
    new_fileName = new_string + ext

    file_oldName = os.path.join(file_path, fname)
    file_newName = os.path.join(file_path, new_fileName)

    print(file_oldName)
    print("================")
    print(file_newName)
    

    os.rename(file_oldName, file_newName)


