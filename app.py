import streamlit as st
import os
import subprocess
from main import video_to_summary

def main():
    st.title("🎬 Video Summarizer AI")

    # ✅ Optional: Check if ffmpeg is available
    try:
        result = subprocess.run(["ffmpeg", "-version"], check=True, capture_output=True, text=True)
        st.success("✅ ffmpeg is installed and ready")
        st.text(result.stdout.splitlines()[0])
    except FileNotFoundError:
        st.error("❌ ffmpeg is not installed or not found in path.")
        return

    # 📁 File uploader
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])

    if uploaded_file is not None:
        # Save the uploaded file locally
        with open("uploaded_video.mp4", "wb") as f:
            f.write(uploaded_file.read())

        st.info("⏳ Transcribing and summarizing... Please wait. This might take a few minutes.")

        # Generate summary
        try:
            summary_result = video_to_summary(
                video_path="uploaded_video.mp4",
                model_size="base",  # Whisper model size
                summarizer_model_name="facebook/bart-large-cnn",
                use_chunking=True
            )

            st.subheader("📄 Final Summary")
            st.write(summary_result)

        except Exception as e:
            st.error(f"⚠️ Error during processing: {str(e)}")

        finally:
            # Cleanup
            if os.path.exists("uploaded_video.mp4"):
                os.remove("uploaded_video.mp4")

if __name__ == "__main__":
    main()
