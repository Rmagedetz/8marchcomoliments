import streamlit as st
import random
import os
import shutil

messages_total = 4
messages_in_use_dir = "messages"
pictures_in_use_dir = "pictures"
no_use_msg_pics = "no_use"


def get_messages_count():
    messages = os.listdir(messages_in_use_dir)
    return messages_total - len(messages)


def get_text():
    messages = os.listdir(messages_in_use_dir)
    msg_file = random.choice(messages)

    old_file_path = os.path.join(messages_in_use_dir, msg_file)
    new_file_path = os.path.join(no_use_msg_pics, msg_file)

    shutil.move(old_file_path, new_file_path)

    with open(new_file_path, "r", encoding="utf-8") as file:
        msg_text = file.read().strip()

    return msg_text


def get_pic():
    pictures = os.listdir(pictures_in_use_dir)
    picture_file = random.choice(pictures)

    old_pic_path = os.path.join(pictures_in_use_dir, picture_file)
    new_pic_path = os.path.join(no_use_msg_pics, picture_file)

    shutil.move(old_pic_path, new_pic_path)

    return new_pic_path


def main():
    messages_sended = get_messages_count()
    if st.button("Получить послание", key="get_message"):
        if messages_sended != messages_total:
            message = get_text()
            picture = get_pic()
            col1, col2 = st.columns(2)
            with st.container(border=True):
                with col2:
                    message = message.replace("-", " --")
                    st.warning(message)
                with col1:
                    st.image(picture, use_container_width=True)
            st.write(f"Посланий получено {messages_sended + 1} из {messages_total}")
        else:
            with st.container(border=True):
                with open("final_message.txt", "r", encoding="utf-8") as file:
                    final_msg_text = file.read().strip()
                st.text(final_msg_text)
                st.audio("sm.mp3", format="audio/mpeg", loop=True)


if __name__ == "__main__":
    main()