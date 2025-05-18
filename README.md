# 📦 Script Python – Zipper un dossier et l’envoyer sur AWS S3

Quatrième projet cloud AWS de Cédric Haegele.  
Ce script Python crée une archive `.zip` d’un dossier local, l’envoie dans un bucket S3, et enregistre l'opération dans un fichier log.

---

## 🧰 Technologies utilisées

- Python 3.13  
- Boto3  
- AWS CLI  
- Amazon S3  
- zipfile, os, datetime

---

## 📦 Fonctionnement

1. Crée une archive `.zip` du dossier `fichiers_a_archiver`
2. Envoie cette archive dans le bucket `cedric-s3-demo`
3. Écrit un log local dans `historique_upload.log`

---

## 🔐 Prérequis

- Avoir un compte AWS  
- Avoir configuré AWS CLI (`aws configure`)  
- Avoir créé un bucket S3 (`cedric-s3-demo`)  
- Installer la bibliothèque Boto3 :
```bash
pip install boto3
```

---

## ▶️ Lancer le script

```bash
python archive_and_upload.py
```

---

## ✍️ Auteur

**Cédric Haegele**  
🔗 [LinkedIn](https://www.linkedin.com/in/cedric-haegele)  
📂 [GitHub](https://github.com/CedricHaegele)
