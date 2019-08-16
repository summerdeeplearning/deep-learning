# General Purpose of this Project

In this project, we will generate face videos of different styles from our original video using pix2pix model with SPADE normalization layer. We firstly record a video of length 10 seconds and then cut the video into 152 pictures. We then synthesize images of a different person using these 152 images and our model. We resolve the flicker issue and finally synthesize a video of a different person with different styles. 

# Synthesize Faces Using SPADE Normalization
We firstly generate images using pix2pix model with SPADE normalization layer. Notice before we use our model to generate images, we firstly need to generate segmented images.

Here are some samples of our original images, the corresponding segmented images, and the synthesized images. 

![3](https://user-images.githubusercontent.com/53350479/63068878-d65fce00-bee2-11e9-89d3-97f0540cde8d.jpg?v=4&s=100)
![2](https://user-images.githubusercontent.com/53350479/63068879-d65fce00-bee2-11e9-8edc-fe953c19d70e.jpg?v=4&s=100)
![1](https://user-images.githubusercontent.com/53350479/63068880-d65fce00-bee2-11e9-9a52-c21de869b4a2.jpg?v=4&s=100)


# Synthesize Face Video Vsing SPADE Normalization

We remove the noise in our segmented images and use temporal consistency loss to optimize our result. We have different styles of videos as follows:

![v13](https://user-images.githubusercontent.com/53350479/63070183-30af5d80-bee8-11e9-8003-585c49cf31b0.gif)
![v15](https://user-images.githubusercontent.com/53350479/63070687-3d34b580-beea-11e9-92f7-d1d84b6fc16c.gif)
![v16](https://user-images.githubusercontent.com/53350479/63080189-7ed75780-bf0e-11e9-9139-3d913bd90a8c.gif)

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

## How to synthesize videos of different style with temporal consistency [4]
The model is in the folder generate stylized video with temporal consistency, we can run follow the code below
`
python transform_video.py --in-path path/to/input/vid.mp4 \
  --checkpoint path/to/style/model.ckpt \
  --out-path out/video.mp4 \
  --device /gpu:0 \
  --batch-size 4
`
## Link to the Dataset
https://drive.google.com/file/d/1c8S9l5CctAj4vekpxyvD_XsnZ71FRia6/view?usp=sharing

## References
[1]https://github.com/switchablenorms/CelebAMask-HQ

[2]https://github.com/NVlabs/SPADE

[3]https://github.com/nightrome/cocostuff

[4] https://github.com/lengstrom/fast-style-transfer
