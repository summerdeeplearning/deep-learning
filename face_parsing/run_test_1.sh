CUDA_VISIBLE_DEVICES=$1 python -u main.py --batch_size 16 --imsize 512 --version parsenet --train False --test_image_path ~/SPADE/results/ffhq/test_latest/images/synthesized_image --test_size 100

