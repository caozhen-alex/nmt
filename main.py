from nmt.training import train
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

config_path = 'configs/transformer_en_zh.yaml'

train(config_path)