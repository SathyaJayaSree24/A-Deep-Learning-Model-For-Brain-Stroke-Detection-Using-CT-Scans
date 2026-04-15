"""Streamlit app module"""

import streamlit as st
import predict
from PIL import Image
import numpy as np

TITLE = "Brain Stroke Detector"

STROKE_STYLE = "padding: 20px; background-color: #f44336; color: white; text-align: center; font-size: 24px;"
HEALTHY_STYLE = "padding: 20px; background-color: #4cbb17; color: white; text-align: center; font-size: 24px;"
ERROR_STYLE = "padding: 20px; background-color: #ffc300; color: black; text-align: center; font-size: 20px;"


def print_outcome(outcome):
    if outcome:
        st.markdown(f'<div style="{STROKE_STYLE}">⚠️ Stroke Detected</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="{HEALTHY_STYLE}">✅ Healthy</div>', unsafe_allow_html=True)


def print_error(msg):
    st.markdown(f'<div style="{ERROR_STYLE}">{msg}</div>', unsafe_allow_html=True)


# ✅ SMART CHECK: is image grayscale-like?
def is_ct_like(image):
    img = Image.open(image).convert("RGB")
    img = img.resize((100, 100))  # smaller for speed

    arr = np.array(img)

    # difference between R, G, B channels
    diff_rg = np.abs(arr[:, :, 0] - arr[:, :, 1]).mean()
    diff_rb = np.abs(arr[:, :, 0] - arr[:, :, 2]).mean()
    diff_gb = np.abs(arr[:, :, 1] - arr[:, :, 2]).mean()

    # if differences are small → grayscale
    avg_diff = (diff_rg + diff_rb + diff_gb) / 3

    return avg_diff < 10   # threshold


def main():
    st.set_page_config(page_title=TITLE)
    st.title(TITLE)

    st.write("Upload a **Brain CT scan image**")

    uploaded_img = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_img is not None:
        try:
            # ❌ Reject non-CT-like images
            if not is_ct_like(uploaded_img):
                print_error("❌ Wrong image uploaded. Please upload a Brain CT scan.")
                return

            # ✅ Show image
            st.image(uploaded_img, caption='Uploaded Image', use_column_width=True)

            with st.spinner("Analyzing..."):
                stroke = predict.predict(uploaded_img)

            print_outcome(stroke)

        except Exception as e:
            print_error(f"Error: {e}")


if __name__ == '__main__':
    main()