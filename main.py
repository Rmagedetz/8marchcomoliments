import streamlit as st
import random
import os

TOTAL_COMPLIMENTS = 16


def read_compliments():
    try:
        with open("compliments.txt", "r", encoding="utf-8") as file:
            compliments = file.readlines()
        return [c.strip() for c in compliments]
    except Exception as e:
        st.error(f"Ошибка при чтении файла: {e}")
        return []


def write_compliments(compliments):
    try:
        with open("compliments.txt", "w", encoding="utf-8") as file:
            for compliment in compliments:
                file.write(compliment + "\n")
    except Exception as e:
        st.error(f"Ошибка при записи в файл: {e}")


def remove_compliment(compliment):
    compliments = read_compliments()
    compliment = compliment.strip()
    if compliment in compliments:
        compliments.remove(compliment)
        write_compliments(compliments)


def get_random_compliment_and_picture():
    compliments = read_compliments()
    if compliments:
        compliment = random.choice(compliments)
        remove_compliment(compliment)
    else:
        compliment = "Сегодня все комплименты использованы!"

    picture = random.choice(os.listdir("pictures"))
    return compliment, picture, len(compliments)


def main():
    compliments = read_compliments()
    if st.button("Получить послание"):
        compliment, picture, remaining_count = get_random_compliment_and_picture()

        if remaining_count > 0:
            col1, col2 = st.columns(2)
            with st.container(border=True):
                with col2:
                    compliment = compliment.replace("-", " --")
                    st.warning(compliment)
                with col1:
                    st.image(f"pictures/{picture}", use_container_width=True)
        else:
            with st.container(border=True):
                compliment = ("Милые наши дамы!! От всей мужской части компании поздравляем вас с этим прекрасным "
                              "днём, а также с завтрашним, послезавтрашним и"
                              "всеми последующими, потому что каждый день - ваш день! Пусть окружающая реальность "
                              "разговаривает с вами на вашем языке! Пусть любовь, внимание, комфорт и забота "
                              "будут обличены именно в ту форму, которая нужна именно вам! Благополучия и "
                              "процветания! Всего всего самого-самого!!")
                st.header(compliment)
                st.audio("sm.mp3", format="audio/mpeg", loop=True)
                # st.image("sunrise.jpg", caption="Sunrise by the mountains")

        sent_count = TOTAL_COMPLIMENTS - len(compliments)
        st.write(f"Посланий получено {sent_count} из {TOTAL_COMPLIMENTS}")


if __name__ == "__main__":
    main()
