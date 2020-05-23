from nmt.training import train
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

config_path = 'configs/transformer_en_zh2.yaml'

train(config_path)