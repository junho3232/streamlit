import streamlit as st

st.set_page_config(
    page_title='공동교육과정',
    page_icon='👀'
)

menu = st.sidebar.selectbox('MENU', ['BMI 지수 계산기', '원의 넓이 계산기','계산기'])

if menu == 'BMI 지수 계산기':
    st.subheader('BMI 지수 계산기')


    키 = st.number_input('키를 입력하세요.(cm)', step=1)
    체중 = st.number_input('몸무게를 입력하세요.(kg)', step=1)
    btn = st.button('계산하기')
    if btn:
        st.write('당신의 BMI지수는,',체중/(키*키), '입니다.')
    if btn:
        체중/(키*키) > 20
        st.write('저체중 입니다')
    elif btn:
        20 < 체중/(키*키) < 24
        st.write('정상입니다')



elif menu == '원의 넓이 계산기':
    st.subheader('원의 넓이 계산기')

    반지름 = st.number_input('반지름을 입력하세요.', step=1)
    btn = st.button('계산하기')
    if btn:
        st.write('원의 넓이는',(반지름*반지름) ,'π 입니다')


elif menu == '계산기':
    st.subheader('계산기')

    수1 = st.number_input('숫자를 입력하세요')
    수2 = st.number_input('두번째 숫자를 입력하세요')
    연 = st.text_input('연산자를 입력하세요')
    btn = st.button('계산하기')
    if 연 == '+':st.write((수1+수2),'입니다')
    if 연 == '-':st.write((수1-수2),'입니다')
    if 연 == '*':st.write((수1*수2),'입니다')

