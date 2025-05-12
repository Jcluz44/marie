import streamlit as st
import ffmpeg
import os
import tempfile

st.title("Convertisseur M4V → MP4")

uploaded_file = st.file_uploader("Téléverse un fichier M4V", type=["m4v"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".m4v") as temp_input:
        temp_input.write(uploaded_file.read())
        temp_input_path = temp_input.name

    temp_output_path = temp_input_path.replace(".m4v", ".mp4")

    with st.spinner("Conversion en cours..."):
        try:
            ffmpeg.input(temp_input_path).output(temp_output_path, codec='copy').run()
            st.success("Conversion terminée !")
            with open(temp_output_path, "rb") as f:
                st.download_button("Télécharger le MP4", f, file_name="video_convertie.mp4")
        except Exception as e:
            st.error(f"Erreur : {e}")
