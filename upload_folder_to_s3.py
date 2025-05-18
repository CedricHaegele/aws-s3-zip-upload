import boto3
import os
from botocore.exceptions import NoCredentialsError

# Nom du bucket S3
bucket_name = "cedric-s3-demo"

# Dossier local à parcourir
local_folder = "fichiers_a_uploader"  # <-- Crée ce dossier dans ton projet

# Connexion à AWS S3
s3 = boto3.client('s3')

# Liste les fichiers du dossier local
try:
    fichiers = os.listdir(local_folder)
    if not fichiers:
        print("⚠️ Le dossier est vide.")
    else:
        compteur = 0
        for fichier in fichiers:
            chemin_complet = os.path.join(local_folder, fichier)
            if os.path.isfile(chemin_complet):
                try:
                    s3.upload_file(chemin_complet, bucket_name, fichier)
                    print(f"✅ Envoyé : {fichier}")
                    compteur += 1
                except Exception as e:
                    print(f"❌ Erreur avec le fichier {fichier} : {e}")
        print(f"\n📦 Total des fichiers envoyés : {compteur}")
except FileNotFoundError:
    print(f"❌ Le dossier '{local_folder}' est introuvable.")
except NoCredentialsError:
    print("❌ Identifiants AWS manquants ou incorrects.")
