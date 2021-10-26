import os
import numpy as np
import nibabel as nib
import h5py


def preprocess_data():
    file_p = os.getcwd()
    dst_path = file_p[:-24] + "/" + 'Training-Testing/Reg-Training-Testing/Training-Testing'
    folders = os.listdir(dst_path + "/" + "img")

    for sub_folder in folders[:1]:
        temp_pwd = dst_path + "/" + "img" + "/" + sub_folder
        files = os.listdir(temp_pwd)
        for filename in files:
            right_text = filename[3:]  # get the part "XXXX-XXXX.nii.gz"
            subject = right_text[:4]
            img = nib.load(dst_path + "/" + "img" + "/" + sub_folder + "/" + 'img' + right_text)
            label = nib.load(dst_path + "/" + "label" + "/" + sub_folder + "/" + 'label' + right_text)

            # Convert them to numpy format,
            data = img.get_fdata()
            label_data = label.get_fdata()

            # clip the images within [-125, 275],
            data_clipped = np.clip(data, -125, 275)

            # normalize each 3D image to [0, 1], and
            data_normalised = (data_clipped - (-125)) / (275 - (-125))

            # extract 2D slices from 3D volume for training cases while
            # e.g. slice 000
            for i in range(data_normalised.shape[2]):
                formatted_data = "{:03d}".format(i)
                slice000 = data_normalised[:, :, i]
                label_slice000 = label_data[:, :, i]
                np.savez(file_p[:-24] + "/data/Synapse/train_npz/case" + subject + "_slice" + formatted_data + ".npz",
                         image=slice000,
                         label=label_slice000)

            # keep the 3D volume in h5 format for testing cases.
            fn = file_p[:-24] + "/data/Synapse/train_npz/case" + subject + '.npy.h5'
            f = h5py.File(fn, 'w')
            dataset = f.create_dataset("image", data=data_normalised)
            dataset = f.create_dataset("label", data=label_data)
            f.close()
    print("Preprocessing complete")


def main():
    preprocess_data()


if __name__ == "__main__":
    main()
