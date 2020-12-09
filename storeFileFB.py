
import firebase_admin
from firebase_admin import credentials, firestore, storage, db
import os

cred=credentials.Certificate('./sensepi-4e031-firebase-adminsdk-ibkhx-f0de887562.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'sensepi-4e031.appspot.com',
    'databaseURL': 'https://sensepi-4e031.firebaseio.com'
})

bucket = storage.bucket()
ref = db.reference('/')
home_ref = ref.child('file')

def store_file(fileLoc):

    filename=os.path.basename(fileLoc)

    # Store File in FB Bucket
    blob = bucket.blob(filename)
    outfile=fileLoc
    blob.upload_from_filename(outfile)

def push_db(fileLoc, time):

    filename=os.path.basename(fileLoc)

    # Push file reference to image in Realtime DB
    home_ref.push({
        'image': filename,
        'timestamp': time}
    )


#+ Replace the whole  ``if __name__ == "__main__":`` statement with the following:
if __name__ == "__main__":
    f = open("./test.txt", "w")
    f.write("a demo upload file to test Firebase Storage")
    f.close()
    store_file('./test.txt')
