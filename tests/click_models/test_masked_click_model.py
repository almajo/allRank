import numpy as np

from allrank.click_models.base import FixedClickModel, RandomClickModel
from allrank.click_models.click_utils import MaskedRemainMasked
from allrank.data.dataset_loading import PADDED_Y_VALUE


def test_masked_should_remain_masked():
    click_model = MaskedRemainMasked(FixedClickModel(click_positions=[1]))
    assert click_model.click((np.ones((3, 1)), np.array([0, 0, PADDED_Y_VALUE]))).tolist() == [0, 1, PADDED_Y_VALUE]


def test_inner_click_model_should_just_get_unmasked_docs():
    np.random.seed(42)
    click_model = MaskedRemainMasked(RandomClickModel(n_clicks=1))
    clicks = click_model.click((np.ones((5, 1)), np.array([0, PADDED_Y_VALUE, PADDED_Y_VALUE, PADDED_Y_VALUE, PADDED_Y_VALUE]))).tolist()
    assert clicks == [1, PADDED_Y_VALUE, PADDED_Y_VALUE, PADDED_Y_VALUE, PADDED_Y_VALUE]
