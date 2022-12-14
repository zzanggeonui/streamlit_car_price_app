import streamlit as st


def run_home_app():
    st.text('환영합니다')
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다. 데이터 분석 및 고객 정보를 넣으면, 얼마정도의 차를 구매할지 예측해 줍니다. ')
    url = 'https://p4.wallpaperbetter.com/wallpaper/122/597/209/2019-cars-4k-dodge-challenger-rt-widebody-wallpaper-preview.jpg'
    st.image(url)

