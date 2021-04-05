import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import math
from tqdm import tqdm_notebook as tqdm
import time
import matplotlib as mpl


def tcga_paired_purification(input_data_cancer, input_data_normal, purity_df):
    # purity analysis
    common_columns = set(input_data_cancer) & set(purity_df.index)

    mi = input_data_normal['mean']
    std = input_data_normal['std']

    xi = input_data_cancer.loc[mi.index, common_columns]
    pi = purity_df

    # multiple mi and pi to form matrix dataframe
    mi_pi = pd.DataFrame(np.outer(2**(mi+2*std), 1-pi),
                         index=mi.index, columns=pi.index)

    # populate purity
    pi_ready = pd.DataFrame(np.repeat(pd.DataFrame(
        pi).T.values, mi_pi.shape[0], axis=0), index=mi_pi.index, columns=mi_pi.columns)

    # calculate cancer porportion
    ci = (xi-mi_pi)

    return ci
