
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

st.title("OpenAI GPT-3.5 Turbo Streamlitアプリ")

user_input = st.text_area("質問や指示を入力してください:", height=100)

if st.button("回答を生成"):
    if user_input:
        with st.spinner("回答を生成中..."):
            response = generate_response(user_input)
        st.write("回答:")
        st.write(response)
    else:
        st.warning("質問や指示を入力してください。")

# README.md
# OpenAI APIを使用したStreamlitアプリ
