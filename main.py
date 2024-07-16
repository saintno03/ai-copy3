#from dotenv import load_dotenv

#load_dotenv()

import streamlit as st

from langchain.chat_models import ChatOpenAI

from PIL import Image



#Stream 받아 줄 Hander 만들기

from langchain.callbacks.base import BaseCallbackHandler

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler







st.title(':money_with_wings: 돈버는 :red[USP 카피라이팅] 제작소 ')



st.text('■ 사용 가이드 안내 ■')

st.text('1.빈칸에 키워드를 입력해주세요')

st.text('2.카피 작성요청하기 버튼을 눌러주세요') 



content = st.text_input(':blue[->제품고유의 강점, USP]를 :red[딱 3개]를 뽑아드립니다')





class StreamHandler(BaseCallbackHandler):

        def __init__(self, container, initial_text=""):

            self.container = container

            self.text=initial_text

            

        def on_llm_new_token(self, token: str, **kwargs) -> None:

            self.text+=token

            self.container.markdown(self.text)







if st.button('카피 작성 요청하기'):

    with st.spinner('AI가 카피를 작성중...'):

        chat_box = st.empty()

        stream_hander = StreamHandler(chat_box)

        chat_model = ChatOpenAI(streaming=True, callbacks=[stream_hander])



        result = chat_model.predict(content + "에 대한 카피라이팅을 USP를 뽑아서 1줄로 3개의 예시를 한글로 작성해줘")

        # st.write(result)

        

st.markdown("""

    <table style='border: none;'>
        <tr>         
        <td><a href="https://blog.naver.com/a_long_break"><img src='https://i.postimg.cc/qMsSq3PF/v2-002.png' style='width: 100%'></a></td>
        <td><a href="https://0one2.ulog.kr/769627#_PA"><img src='https://i.postimg.cc/G2fzgcZG/v2-001.png' style='width: 100%'></a></td>
        </tr>
    </table>

    """, unsafe_allow_html=True)

