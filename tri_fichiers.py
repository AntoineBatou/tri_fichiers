"""
Trier les fichiers contenus dans un dossier pour les classer dans des sous-dossier en fonction de leur extension :
"""

from pathlib import Path

# Je définis un dictionnaire pour les extensions (à compléter en fonction)

extension = {".mp3": "Musique",
            ".wav": "Musique",
            ".flac": "Musique",
            ".avi": "Videos",
            ".mp4": "Videos",
            ".gif": "Videos",
            ".bmp": "Images",
            ".png": "Images",
            ".jpg": "Images",
            ".txt": "Documents",
            ".pptx": "Documents",
            ".csv": "Documents",
            ".xls": "Documents",
            ".odp": "Documents",
            ".pages": "Documents"}


### Je détermine le chemin du dossier dans lequel se trouve les fichiers à trier
chemin_fichiers = Path(###Insérer ici le chemin)
    
### Je récupère tous les fichiers dans un objet Pathosix dans une variable    
liste_fichiers = chemin_fichiers.iterdir()

### Je boucle sur l'objet (chacun des fichiers)
for i in liste_fichiers:

### Pour chacun des fichier je recupère l'extension
    extension_recup = i.suffix

### Je vérifie pour chacun des fichiers son extension et récupère le dossier correspond
    dossier = extension.get(extension_recup, "Autres")

### Je concatène le chemin et le nom du dossier
    creation = chemin_fichiers / dossier

### Je crée chacun des dossiers
    creation.mkdir(exist_ok=True)

### Je déplace chacun des fichiers dans le dossier qui corresponds
    i.rename(creation/i.name)