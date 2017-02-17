import pandas as pd
import numpy as np

rng1 = pd.date_range('1/1/2017', periods=12, freq='D')
rng2 = pd.date_range('1/11/2017', periods=3, freq='D')
ts = pd.Series(np.random.randn(len(rng1)), index=rng1)
ts2 = pd.Series(np.random.randn(len(rng2)), index=rng2)

ts4 = ts2.index.isin(ts.index)

print(ts)
print(ts.values)
print(ts.values[-1])
print(ts4)
