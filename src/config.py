"""File with configs"""
import os
import torch

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(ROOT_PATH, "models")
DATA_PATH = os.path.join(ROOT_PATH, "data")
LOG_PATH = os.path.join(ROOT_PATH, "logs")

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
