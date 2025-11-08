import streamlit as st

def write():
    st.markdown("# 나의 소개 페이지")
    st.markdown("## 자기소개")
    st.text("안녕하세요. 저는 국문과 김수빈입니다.")
    st.markdown("## 관심사")
    st.write("저는 **라임과 운율**에 *매우* 관심이 많습니다.")
    st.markdown("라임을 잘 설명할 수 있는 [에미넴의 음악 하나](https://www.youtube.com/watch?v=mwGtM-o1ynE)를 공유하겠습니다. ")
    st.markdown("## 앞으로의 목표")
    st.text("운율의 아름다움을 알릴 수 있는 연구와 창작물 제작을 하고 싶습니다.다음은 제가 gemini의 라임 인식 향상 연구를 진행하며 쓴 함수 중 일부입니다.")
    st.code("def get_rhyme_candidates_with_score(target_word: str):", language="python") 


write()