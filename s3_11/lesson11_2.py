import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image



st.title('Stereamlit 超入門')
st.write('Interactionve Widgets')

left_colmun, right_colmun = st.columns(2)
button = left_colmun.button('右カラムに文字を表示')
if button:
    right_colmun.write('ここは、右カラム')

expander = st.expander('問い合わせ')
expander.write('鯛合わせ')