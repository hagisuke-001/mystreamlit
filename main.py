import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image



st.title('Stereamlit 超入門')
st.write('DataFrame')

"""
df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
    })

st.write(df)
st.dataframe(df, width=100, height=100)
"""
# マジックコマンドを使用したマークダウン
"""
# 章
## 節
### 項

''' python
import streamlit as pt
'''

"""

"""
df = pd.DataFrame(np.random.rand(20,3), columns=['a', 'b', 'c'])
st.line_chart(df)
"""
df = pd.DataFrame(np.random.rand(100,2)/[50,50]+[130.6,139.7], columns=['lat', 'lon'])
st.map(df)

