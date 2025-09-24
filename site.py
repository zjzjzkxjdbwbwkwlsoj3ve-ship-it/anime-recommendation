import streamlit as st
import pickle
import pandas as pd
import requests
import random
import time


def recommend(animer):

    matches = anime[anime['Title_English'] == animer]
    if matches.empty:
        return []

    animeindex = matches.index[0]

    distances = similarity[animeindex]
    animelist = sorted(list(enumerate(similarity[animeindex])), reverse=True, key=lambda x: x[1])[1:21]

    recommendedanime = []
    for i in animelist:
        title = anime.iloc[i[0]]['Title_English']
        if pd.notna(title) and title != animer:
            recommendedanime.append(title)

    return recommendedanime


animelist = pickle.load(open('anime.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
anime = pd.DataFrame(animelist)




st.title('anime recommendation system')


selected = st.selectbox(
    "what is your favourite anime",
    anime['Title_English'].values,
)

images = [
    "a1.jpg",
    "a2.jpg",
    "a3.jpg",
    "a4.jpg"
]


if st.button("recommend anime"):
    recommendations = recommend(selected)
    st.snow()
    st.image(images[0], caption="anime is art")
    st.title("your recommendations are")

    for i in recommendations:
        st.write(i)


    st.image(images[1], caption="fixating")
    st.image(images[2], caption="less than 3d more than 2d")
    st.image(images[3], caption="see more like no tomorrow")