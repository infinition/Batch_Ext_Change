#change l'extension de tous les fichiers d'un dossier et de ses sous-dossiers
#test
import os

def change_extension_all_files(dossier):
    for root, dirs, files in os.walk(dossier):
        for file in files:
                new_name = file + extension1
                os.rename(os.path.join(root, file), os.path.join(root, new_name))
                print(os.path.join(root, file))
                print(os.path.join(root, new_name))

def revert_extension_all_files(dossier):
    for root, dirs, files in os.walk(dossier):
        for file in files:
            if file.endswith(extension1):
                new_name = file.replace(extension2, '')
                os.rename(os.path.join(root, file), os.path.join(root, new_name))
                print(os.path.join(root, file))
                print(os.path.join(root, new_name))

if __name__ == '__main__':
    extension2 = input("Extensions cibles : ")
    extension1 = input("à changer en : ")
    dossier = input('Chemin : ')
    change_extension_all_files(dossier)
    #ask if user wants to revert extension
    revert = input('Voulez vous revenir à l\'extension originale ? (y/n) : ')
    if revert == 'y':
        revert_extension_all_files(dossier)
        print('Extensions rétablies')
    else:
        print('Terminé avoir rétabli l\'extension originale')

