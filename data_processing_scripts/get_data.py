import synapseclient
import os
import shutil
import zipfile


def get_data():
    syn = synapseclient.Synapse()
    email = input('Input your Synapse email: ')
    api_key = input('Input your Synapse apiKey: ')
    syn.login(
        email=email,
        apiKey=api_key)
    syn.get(entity='syn3380218')


def copy_and_unzip_data():
    file_path = os.getcwd()
    src_path = file_path + '/' + '1.zip'  # + 'Reg-Training-Testing.zip'
    dst_path = file_path[:-24] + "/" + 'Training-Testing'
    with zipfile.ZipFile(src_path, 'r') as zip_ref:
        zip_ref.extractall(dst_path)
    os.remove(src_path)


def main():
    get_data()
    copy_and_unzip_data()


if __name__ == "__main__":
    main()
