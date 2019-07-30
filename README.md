# SPADE Normalization for Face

## How to generate segmentation [1]

First,
`
cd face_parsing
`
and change the `--test_image_path` options in the `face_parsing/run_test_1.sh` to your data set. Then run
`
bash run_test_1.sh 1
`
and you will get the segmented label at `./test_result`.

## How to train SPADE model [2]
`
cd SPADE
python train.py --name [model_name] --dataset_mode custom --label_dir [path_to_seg_img] ---image_dir [path_to_ori_image] --no_instance --label_nc 19
`

Feel free to run `python train.py -h` to twist other options of SPADE, e.g. change the number of GPUs.

The result will be saved at `SPADE/results/[model_name]`

## How to run SPADE Face [3]
Assume the name of the model is `model_name` which is located at `SPADE/results/[model\_name]`. The segmentation of the image is at `[path_to_seg_img]`.
`
cd SPADE
python test.py --name [model_name] --dataset_mode custom --image_dir [path_to_ori_img] --label_dir [path_to_seg_img] --dataroot SPADE --no_instance --label_nc 19
`
Then the generated file will be located at `SPADE/results/[model_name]/test_lastest/images/synthesized_img`

## Link to the Dataset
https://drive.google.com/file/d/1c8S9l5CctAj4vekpxyvD_XsnZ71FRia6/view?usp=sharing

## References
[1]https://github.com/switchablenorms/CelebAMask-HQ

[2]https://github.com/NVlabs/SPADE

[3]https://github.com/nightrome/cocostuff
