import streamlit as st
from transformers import pipeline

def main():
    """
    Launches a Streamlit application for text generation using the GPT-2 model.

    This application allows users to input a text prompt, which is then processed
    by the text generation model. The generated text is displayed to the user.

    Functions:
        - Load the GPT-2 model for text generation.
        - Provide a user interface for input and output.
    """
    text_generator = pipeline("text-generation", model="gpt2")

    st.title("Text Generation Bot")
    st.subheader("Generate text based on your input!")

    user_input = st.text_area("Input your text prompt here:", height=120)

    if st.button("Generate Text"):
        if user_input:
            """
            Generates text based on the user input.

            This function calls the text generation model with the user's prompt
            and displays the generated output.
            """
            generated_texts = text_generator(user_input, max_length=200)

            st.subheader("Generated Text:")
            for i, text in enumerate(generated_texts):
                st.write(f"**Generated Text {i + 1}:**")
                st.write(text['generated_text'])
        else:
            st.warning("Please enter a text prompt.")

if __name__ == "__main__":
    main()
