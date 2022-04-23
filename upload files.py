from os import access
import dropbox

class TransferData:

    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        db=dropbox.Dropbox(self.access_token)

        e=open(file_from,"rb")
        db.file_upload(f.read(),file_to)
    


def main():
    access_token='sl.BGSdq5QstXmw7IFlo815pmiqB8QzzPrgMm5qWoBqF6_NtIREhqi8QwEmKjQHigWpOxow0zNDDo2lh-4n2acozV6qxBY2Or4oWJcO8C8SuKLKFP5GLcCtiqdRr1fKMDNpjehSaUArh_oi'
    transferdata=TransferData(access_token)



    file_from=input("enter the file path to transfer:")
    file_to=input("enter the path to upload:-")

    transferdata.upload_file(file_from,file_to)
    print("file moved.")


main()