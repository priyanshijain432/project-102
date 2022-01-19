def upload_file(self, file_from,  file_to):
    dbx = dropbox.Dropbox(self.access_token)

    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to)

def main():
    access_token = "YtbD9pduGlMAAAAAAAAAAVBwRRB9Omkq3BSu5eh9rx73E1xvz8wi5g4ljhQwnSae"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:- ")
    file_to = input("enter the full path to upload to dropbox:- ")

    transferDta.upload_file(file_from, file_to)
    print("file has been moved !!!")
    
    
