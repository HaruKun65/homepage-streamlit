import streamlit as st

#program

import cv2
from glob import glob


def display():
    st.title('フォルダの動画時間の合計app')
    with st.form(key='dir_form'):
        st.subheader('読み込むフォルダのディレクトリを教えてください。')
        dir_name = st.text_input('最後に/を忘れずに')

        form_select = ['.MOV', '.mov', '.mp4']
        form_name = st.radio('ファイル形式を選択してください。', form_select)

        time_select = ['h', 'min', 's']
        time_name = st.radio('時間の単位設定', time_select)

        count_button = st.form_submit_button('計算開始')
        if count_button:
            videos_path = glob(f'{dir_name}*{form_name}')

            total_time = 0
            number_file = 0
            for videos_path in videos_path:
                cap = cv2.VideoCapture(videos_path)
                video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                video_fps = cap.get(cv2.CAP_PROP_FPS)
                time = video_frame_count / video_fps
                total_time += time
                number_file += 1
            
            #時間の単位を設定
            if time_name=='h':
                times_figure = 3600
            elif time_name=='min':
                times_figure = 60
            else:
                times_figure = 1
            
            total_time = round(total_time/times_figure, 2)

            st.title(f'{total_time}{time_name}')
            st.subheader(f'該当ファイルは{number_file}個でした。')


#homepage

from PIL import Image

def intro():

    st.title("Avixy's Homepage")
    st.caption('Welocome!!')

    img = Image.open('./data/Avixy.png')
    st.image(img, width=300)

    st.subheader('自己紹介')
    'スクラッチで主に活動している高身長の高校生です！'
    '趣味はパソコン、映画鑑賞、読書、文房具集めです。'
    '調布のコーダ道場に顔出してるので一緒にお話ししましょう！！'
    'ちなみにこのサイトはPythonとStreamlitを用いて作成しました。'
    '（もしよろしければ、下にある自分の作品をご覧ください）'


if __name__=="__main__":
    intro()
    display()
    