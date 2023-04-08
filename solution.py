import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp

chat_id = 543286418 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.05
    pvalue = cramervonmises_2samp(x, y)[1]
    return pvalue < alpha
