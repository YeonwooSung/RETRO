import torch
from packaging import version
from torch import _softmax_backward_data

from .utils import logging


logger = logging.get_logger(__name__)

is_torch_less_than_1_8 = version.parse(torch.__version__) < version.parse("1.8.0")
is_torch_less_than_1_11 = version.parse(torch.__version__) < version.parse("1.11")


def torch_int_div(tensor1, tensor2):
    """
    A function that performs integer division across different versions of PyTorch.
    """
    if is_torch_less_than_1_8:
        return tensor1 // tensor2
    else:
        return torch.div(tensor1, tensor2, rounding_mode="floor")


def softmax_backward_data(parent, grad_output, output, dim, self):
    """
    A function that calls the internal `_softmax_backward_data` PyTorch method and that adjusts the arguments according
    to the torch version detected.
    """

    if is_torch_less_than_1_11:
        return _softmax_backward_data(grad_output, output, parent.dim, self)
    else:
        return _softmax_backward_data(grad_output, output, parent.dim, self.dtype)