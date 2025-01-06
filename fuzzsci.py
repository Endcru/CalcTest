from hypothesis import given, strategies as st, settings, Verbosity
from skimage import data
from skimage.color import rgb2gray
from skimage.color import rgb2hsv
from skimage.exposure import match_histograms
import numpy as np

@given(st.lists(st.lists(st.lists(st.integers(min_value=0, max_value=256), min_size=3, max_size=3), min_size=3, max_size=3), min_size=1))
@settings(verbosity=Verbosity.verbose, max_examples=100000)  # Включает подробный вывод
def test_rgb2gray_with_processed_input(input_data):
    try:
        inp = np.array(input_data)
        grayscale = rgb2gray(inp)
    except OverflowError:
        pass

@given(st.lists(st.lists(st.lists(st.integers(min_value=0, max_value=256), min_size=3, max_size=3), min_size=3, max_size=3), min_size=1))
@settings(verbosity=Verbosity.verbose, max_examples=100000)  # Включает подробный вывод
def test_rgb2hsv_with_processed_input(input_data):
    try:
        inp = np.array(input_data)
        grayscale = rgb2hsv(inp)
    except OverflowError:
        pass

@given(st.lists(st.lists(st.lists(st.integers(min_value=0, max_value=256), min_size=3, max_size=3), min_size=3, max_size=3), min_size=1), st.lists(st.lists(st.lists(st.integers(min_value=0, max_value=256), min_size=3, max_size=3), min_size=3, max_size=3), min_size=1))
@settings(verbosity=Verbosity.verbose, max_examples=100000)  # Включает подробный вывод
def test_match_histograms_with_processed_input(input_data1, input_data2):
    try:
        inp1 = np.array(input_data1)
        inp2 = np.array(input_data2)
        matched = match_histograms(inp1, inp2, channel_axis=-1)
    except OverflowError:
        pass

if __name__ == "__main__":
    test_rgb2gray_with_processed_input()
    test_rgb2hsv_with_processed_input()
    test_match_histograms_with_processed_input()
    

