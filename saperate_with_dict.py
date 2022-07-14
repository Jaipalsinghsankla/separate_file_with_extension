import os,shutil
dict_extension={
'audio_extension':('.m4a','.flac','.mp3','.wav','.wma','.aac'),
'video_extension':('.mp4','.mkv','.MKV','.flv','.mpeg'),
'document_extension':('.pdf','.txt','.doc')
}
folderpath=input('enter folder path-')
def file_finder(folder_path,fileextension):
    files=[]
    for item in os.listdir(folder_path):
        for extension in fileextension:
            if item.endswith(extension):
                files.append(item)
    return files
for extension_type,ext_tuple in dict_extension.items():
    if len(file_finder(folderpath,ext_tuple))>0:
        folder_name=extension_type.split('_')[0] +'files'
        folder_path=os.path.join(folderpath,folder_name)
        os.mkdir(folder_path)
    for item in file_finder(folderpath,ext_tuple):
        item_path=os.path.join(folderpath,item)
        shutil.move(item_path,folder_path)
    # print('calling file finder')
    # print(file_finder(folder_path,ext_tuple))