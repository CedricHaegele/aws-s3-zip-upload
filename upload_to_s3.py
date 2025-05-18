import boto3
from botocore.exceptions import NoCredentialsError

# Nom du fichier local
file_name = "test.txt"

# Crée un fichier texte local
with open(file_name, 'w') as f:
    f.write("Bonjour depuis Python vers S3 – signé Cédric !")

# Nom de ton bucket S3
bucket_name = "cedric-s3-demo"

# Nom du fichier dans le bucket
object_name = "test-cedric-s3.txt"

# Connexion à S3
s3 = boto3.client('s3')

try:
    s3.upload_file(file_name, bucket_name, object_name)
    print(f"✅ Fichier '{file_name}' envoyé dans le bucket '{bucket_name}' avec le nom '{object_name}'")
except FileNotFoundError:
    print("❌ Le fichier local est introuvable.")
except NoCredentialsError:
    print("❌ Identifiants AWS manquants ou incorrects.")
