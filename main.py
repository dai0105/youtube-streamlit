from typing import Text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)


left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.beta_expander('問い合わせ1')
expander.write('問い合わせ1の回答')
expander = st.beta_expander('問い合わせ2')
expander.write('問い合わせ2の回答')
expander = st.beta_expander('問い合わせ3')
expander.write('問い合わせ3の回答')

#text = st.text_input('あなたの趣味を教えてください')
#condition = st.slider('あなたの今の銚子は？', 0, 100, 50)
#'あなたの趣味：', text
#'コンディション：', condition

#if st.checkbox('Show Image'):
#    img = Image.open("2020-05-20.png")
#    st.image(img, caption="Kohei Imanishi", use_column_width=True)

