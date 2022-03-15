import torch
from packaging import version
from torch import _softmax_backward_data
import torch.nn.functional as F
from torch import nn, einsum

from pyretro.retrieval import BERT_VOCAB_SIZE
from einops import rearrange, repeat

