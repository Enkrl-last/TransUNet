import synapseclient
import os
import shutil
import zipfile


def get_data():
    syn = synapseclient.Synapse()
    email = 'Enkrllastlegion@gmail.com'
    # input('Input your Synapse email: ')
    api_key = 'lR5G3vZwmHhFhnnSA1Xb09WglhCAt4WTqSX5mHPv3IrLL2S3gz+Rg6lKZuLFKc6WWtKfe4Ct+Gz3yTZiu6vk4w=='
    # input('Input your Synapse apiKey: ')
    syn.login(
        email=email,
        apiKey=api_key)
    syn.get(entity='syn10284975')  # syn3380218

# syn10284975


def copy_and_unzip_data():
    file_path = os.getcwd()
    src_path = file_path + '/' + 'Reg-Training-Testing.zip'
    dst_path = file_path[:-24] + "/" + 'Training-Testing'
    with zipfile.ZipFile(src_path, 'r') as zip_ref:
        zip_ref.extractall(dst_path)
    # os.remove(src_path)


def main():
    get_data()
    copy_and_unzip_data()


if __name__ == "__main__":
    main()
