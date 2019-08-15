# General Purpose of this Project

In this project, we will generate face videos of different styles from our original video using pix2pix model with SPADE normalization layer. We firstly record a video of length 10 seconds and then cut the video into 152 pictures. We then synthesize images of a different person using these 152 images and our model. We resolve the flicker issue and finally synthesize a video of a different person with different styles. 

# Synthesize Faces Using SPADE Normalization
We firstly generate images using pix2pix model with SPADE normalization layer. Notice before we use our model to generate images, we firstly need to generate segmented images.

Here are some samples of our original images, the corresponding segmented images, and the synthesized images. 

![3](https://user-images.githubusercontent.com/53350479/63068878-d65fce00-bee2-11e9-89d3-97f0540cde8d.jpg)
![2](https://user-images.githubusercontent.com/53350479/63068879-d65fce00-bee2-11e9-8edc-fe953c19d70e.jpg)
![1](https://user-images.githubusercontent.com/53350479/63068880-d65fce00-bee2-11e9-9a52-c21de869b4a2.jpg)


# Synthesize Face Video Vsing SPADE Normalization

## Data Preprocessing

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

## Result
We use ean Intersection- over-Union(mIoU) and overall pixel accuracy as the test criteria. The overall accuracy is 93.82%, and mIoU score is 0.82.   

## References
[1]https://github.com/switchablenorms/CelebAMask-HQ

[2]https://github.com/NVlabs/SPADE

[3]https://github.com/nightrome/cocostuff
