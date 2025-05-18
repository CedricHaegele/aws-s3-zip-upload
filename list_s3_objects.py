import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Nom du bucket S3
bucket_name = "cedric-s3-demo"

# Connexion au service S3
s3 = boto3.client('s3')

try:
    # Récupère la liste des objets dans le bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Vérifie s’il y a des objets
    if 'Contents' in response:
        print(f"📦 Objets présents dans le bucket '{bucket_name}' :\n")
        for obj in response['Contents']:
            name = obj['Key']
            size = obj['Size']
            last_modified = obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S')
            print(f"📁 {name} | 🧾 {size} octets | 🕒 {last_modified}")
    else:
        print(f"⚠️ Le bucket '{bucket_name}' est vide.")
except NoCredentialsError:
    print("❌ Identifiants AWS manquants.")
except ClientError as e:
    print(f"❌ Erreur AWS : {e}")
