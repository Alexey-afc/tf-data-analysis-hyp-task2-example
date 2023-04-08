import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 543286418 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.05
    statistic,pvalue = ks_2samp(x, y)
    return pvalue < alpha
