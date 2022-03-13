from typing import List, Union

import numpy as np
import tensorflow as tf

from .utils import logging


logger = logging.get_logger(__name__)


def set_tensor_by_indices_to_value(tensor: tf.Tensor, indices: tf.Tensor, value: Union[tf.Tensor, int, float]):
    # create value_tensor since tensor value assignment is not possible in TF
    return tf.where(indices, value, tensor)


def shape_list(tensor: Union[tf.Tensor, np.ndarray]) -> List[int]:
    """
    Deal with dynamic shape in tensorflow cleanly.
    Args:
        tensor (`tf.Tensor` or `np.ndarray`): The tensor we want the shape of.
    Returns:
        `List[int]`: The shape of the tensor as a list.
    """
    if isinstance(tensor, np.ndarray):
        return list(tensor.shape)

    dynamic = tf.shape(tensor)

    if tensor.shape == tf.TensorShape(None):
        return dynamic

    static = tensor.shape.as_list()

    return [dynamic[i] if s is None else s for i, s in enumerate(static)]
