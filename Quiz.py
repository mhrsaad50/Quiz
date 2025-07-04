import streamlit as st

if "score" not in st.session_state:
    st.session_state.score = 0

q1 = st.text_input("What is the largest planet in our solar system?")
btn1 = st.button("Submit answer 1")
if btn1:
    if q1 == "jupiter":
        st.success("Correct")
        st.session_state.score += 1
    else:
        st.error("Incorrect")

st.markdown("---")

q2 = st.number_input("How many days are there in a week?", min_value=1, max_value=10, step = 1)
btn2 = st.button("Submit answer 2")
if btn2:
    if q2 == 7:
        st.success("Correct")
        st.session_state.score += 1
    else:
        st.error("Incorrect")

st.markdown("---")

q3 = st.radio("What do we breathe in to stay alive?", ["Oxygen", "Carbon Dioxide", "Nitrogen"])
btn3 = st.button("Submit answer 3")
if btn3:
    if q3 == "Oxygen":
        st.success("Correct")
        st.session_state.score += 1
    else:
        st.error("Incorrect")

st.markdown("---")

q4 = st.slider("What is the result of 5 × 6?", 0, 50)
btn4 = st.button("Submit answer 4")
if btn4:
    if q4 == 30:
        st.success("Correct")
        st.session_state.score += 1
    else:
        st.error("Incorrect")

st.markdown("---")

q5 = st.selectbox("What is the official language of the United Kingdom?", ["Arabic", "English", "French"])
btn5 = st.button("Submit answer 5")
if btn5:
    if q5 == "English":
        st.success("Correct")
        st.session_state.score += 1
    else:
        st.error("Incorrect")

st.write("")

st.subheader("Your score = " + str(st.session_state.score))
if st.session_state.score == 5:
    st.balloons()