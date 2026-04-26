import streamlit as st

st.set_page_config(page_title="MAT301 AI Tutor", layout="wide")

st.title("MAT301 AI Tutor — Demo Version")
st.write("This is a simple dummy version to prove the app runs before adding RAG.")

st.divider()

st.subheader("Ask a question")

question = st.text_input("Enter a MAT301 question:")

if question:
    st.subheader("Tutor Answer")

    st.write(
        """
        Great question. In the full version, I would search through the course notes
        and practice problems, then guide the student step by step.

        For now, this demo is working correctly if you can see this response.
        """
    )

    st.subheader("Example Teaching Style")

    st.write(
        """
        Instead of immediately giving the final answer, the tutor would:

        1. Identify the concept involved.
        2. Give the minimum background needed.
        3. Ask the student what they think the first step is.
        4. Give hints if they get stuck.
        5. Only reveal the full solution after the student has tried.
        """
    )

st.divider()

st.subheader("Example MAT301 Concepts")

st.write(
    """
    This app could eventually help students with:

    - Groups
    - Subgroups
    - Cyclic groups
    - Dihedral groups
    - Group actions
    - Orbits and stabilizers
    - Symmetry groups
    - Sylow theorems
    """
)