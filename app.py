import streamlit as st
import random

NUM_ROUNDS = 5

# Initialize session state variables
if 'round' not in st.session_state:
    st.session_state.round = 1
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.your_num = random.randint(1, 100)
    st.session_state.computer_num = random.randint(1, 100)
    st.session_state.result = ""

st.title("🎮 High-Low Number Game")

if st.session_state.round <= NUM_ROUNDS and not st.session_state.game_over:
    st.subheader(f"Round {st.session_state.round} of {NUM_ROUNDS}")
    st.write(f"Your number is: **{st.session_state.your_num}**")

    st.write("Do you think your number is higher or lower than the computer's number?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔼 Higher"):
            if st.session_state.your_num > st.session_state.computer_num:
                st.session_state.score += 1
                st.session_state.result = f"✅ You were right! The computer's number was {st.session_state.computer_num}."
            else:
                st.session_state.result = f"❌ Aww, that's incorrect. The computer's number was {st.session_state.computer_num}."
            st.session_state.round += 1

    with col2:
        if st.button("🔽 Lower"):
            if st.session_state.your_num < st.session_state.computer_num:
                st.session_state.score += 1
                st.session_state.result = f"✅ You were right! The computer's number was {st.session_state.computer_num}."
            else:
                st.session_state.result = f"❌ Aww, that's incorrect. The computer's number was {st.session_state.computer_num}."
            st.session_state.round += 1

    if st.session_state.result:
        st.markdown(st.session_state.result)
        st.info(f"Your score is now **{st.session_state.score}**")

        # Prepare for next round
        if st.session_state.round <= NUM_ROUNDS:
            st.session_state.your_num = random.randint(1, 100)
            st.session_state.computer_num = random.randint(1, 100)
        else:
            st.session_state.game_over = True

elif st.session_state.game_over:
    st.success(f"🏁 Game over! Your final score is **{st.session_state.score}** out of {NUM_ROUNDS}.")
    if st.button("🔁 Play Again"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
