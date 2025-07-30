import streamlit as st
import os
from main import video_to_summary

def main():
    st.title("Video Summarizer AI")
    #File uploader widget
    uploaded_file=st.file_uploader("upload a video file", type=["mp4", "mov","avi","mkv"])

    if uploaded_file is not None:
        with open("uploaded_video.mp4","wb") as f:
            f.write(uploaded_file.read())

        st.write("Transcribing and sumarizing. This may take a few moments...")

        summary_result= video_to_summary(
            video_path="uploaded_video.mp4",
            model_size="base", #whisper model
            summarizer_model_name="facebook/bart-large-cnn",
            use_chunking= True

        ) 

        st.subheader("Summary")
        st.write(summary_result )

        if os.path.exists("uploaded_video.mp4"):
            os.remove("uploaded_video.mp4")

if __name__ =='__main__':
    main()            



