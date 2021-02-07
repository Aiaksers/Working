import os

filenum=0

def renamefiles(folder,extens,pattern):
    global filenum
    folder+='\\'

    for i in os.listdir(folder):
        infilepath=os.path.join(folder, i)
        if os.path.isfile(infilepath)==False:
            continue
        filenum+=1
        newname=folder+pattern+str(filenum)+'.'+extens
        os.rename(infilepath, newname)


flag=True
while flag==True:
    folder=input("Укажите путь к папке: ")
    extens=input("Укажите новое расширение файлов: ")
    pattern=input("Укажите шаблон, по которому нужно переименовывать: ")
    renamefiles(folder,extens,pattern)
    continuerunning=input("Хотите переименовать файлы в еще одной папке(напишите 'да' или что-либо другое): ")
    if continuerunning.lower()=='да':
        continue
    else:
        flag=False