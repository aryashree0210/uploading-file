import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                   
                local_path = os.path.join(root, filename)

                    
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = 'sl.AzlvEgQS-3Mv76AywasVRuwp2qSGxK0qtWfbIUb1j2kRLNxEgLlUPcp9AP4oM2brGyaFG4t7g6k1g-4HOpklDbC-L9K05_NYmQBRI7cXecm1iTXS1F2sACRHS9DBwYCPUB-mJ6UN'
    transferData = TransferData(access_token)

    file_from = str(input("Enter your  path to transfer : "))
    file_to = input("enter  your path to upload it to the dropbox:")  

    
    transferData.upload_file(file_from,file_to)
    print(" your file is moved ")

main()
