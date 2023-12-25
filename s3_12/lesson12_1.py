import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title('Stereamlit 超入門')
st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


left_colmun, right_colmun = st.columns(2)
button = left_colmun.button('右カラムに文字を表示')
if button:
    right_colmun.write('ここは、右カラム')

expander = st.expander('問い合わせ')
expander.write('鯛合わせ')