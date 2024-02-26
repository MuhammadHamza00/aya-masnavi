import streamlit as st
import cohere

# Initialize Cohere client
co = cohere.Client('esRNONdbHSZN1nh7yHSdkIEMRWclio9D9vzvL0jM') # Replace with your API key

def generate_summary(prompt):
    # Add the preamble before the user prompt
    full_prompt = (
        'Context: Behave like a Rumi\'s Masnavi teacher and only if given the phrase not in Masnavi then give the message "not a valid verse" and exit, Otherwise summarize the given verses in five or six lines:\n\n' + prompt + ""
    )
    response = co.generate(
        model='command',
        prompt=full_prompt,
        max_tokens=300,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE'
    )
    return response.generations[0].text

def main():
    # Add logo
    logo = 'pngwing.com.png'  # Change this to the path of your logo image
    st.image(logo, width=200)  # Adjust the width as needed
    st.title("Masnavi Summary Generator")


    # User input for phrase
    phrase = st.text_area("Enter the phrase from Masnavi:")

    if st.button("Generate Summary"):
        if phrase:
            summary = generate_summary(phrase)
            st.write("Summary:")
            st.write(summary)
        else:
            st.write("Please enter a phrase from Masnavi.")

if __name__ == "__main__":
    main()
