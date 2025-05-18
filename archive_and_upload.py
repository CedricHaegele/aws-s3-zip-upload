import os
import zipfile
import boto3
from datetime import datetime

# --- Paramètres ---
bucket_name = "cedric-s3-demo"
dossier_source = "fichiers_a_archiver"
nom_archive = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
fichier_log = "historique_upload.log"

# --- Création de l'archive ZIP ---
def creer_archive(source_folder, archive_name):
    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for dossier_racine, _, fichiers in os.walk(source_folder):
            for fichier in fichiers:
                chemin_complet = os.path.join(dossier_racine, fichier)
                chemin_relatif = os.path.relpath(chemin_complet, source_folder)
                zipf.write(chemin_complet, chemin_relatif)
    print(f"✅ Archive créée : {archive_name}")

# --- Upload vers S3 ---
def envoyer_archive_vers_s3(archive_name, bucket):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(archive_name, bucket, archive_name)
        print(f"📤 Fichier '{archive_name}' envoyé dans le bucket '{bucket}'")
        return True
    except Exception as e:
        print(f"❌ Erreur d’envoi : {e}")
        return False

# --- Enregistrement du log ---
def ecrire_log(archive_name, fichier_log):
    with open(fichier_log, 'a') as log:
        horodatage = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log.write(f"[{horodatage}] Envoi réussi : {archive_name}\n")

# --- Script principal ---
if not os.path.exists(dossier_source):
    print(f"❌ Le dossier source '{dossier_source}' est introuvable.")
else:
    creer_archive(dossier_source, nom_archive)
    if envoyer_archive_vers_s3(nom_archive, bucket_name):
        ecrire_log(nom_archive, fichier_log)
