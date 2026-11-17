
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Management", page_icon="🎓")

st.title("🎓 Student Management System")
st.write("Manage student records using CRUD operations")

if "students" not in st.session_state:
    st.session_state.students = pd.DataFrame(
        columns=["ID", "Name", "Age", "Course", "Email"]
    )

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Add Student", "View Students", "Update Student", "Delete Student"]
)

if menu == "Add Student":
    st.subheader("Add New Student")

    id = st.number_input("Student ID", min_value=1, step=1)
    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    course = st.text_input("Course")
    email = st.text_input("Email")

    if st.button("Add Student"):
        if name and course and email:
            if id not in st.session_state.students["ID"].values:
                new_student = pd.DataFrame([{
                    "ID": id,
                    "Name": name,
                    "Age": age,
                    "Course": course,
                    "Email": email
                }])

                st.session_state.students = pd.concat(
                    [st.session_state.students, new_student],
                    ignore_index=True
                )

                st.success("Student added successfully!")
            else:
                st.error("Student ID already exists.")
        else:
            st.warning("Please fill all fields.")

elif menu == "View Students":
    st.subheader("All Students")

    st.dataframe(st.session_state.students, use_container_width=True)

    st.write("Total Students:", len(st.session_state.students))

elif menu == "Update Student":
    st.subheader("Update Student Details")

    if not st.session_state.students.empty:
        id = st.selectbox(
            "Select Student ID",
            st.session_state.students["ID"].tolist()
        )

        student = st.session_state.students[
            st.session_state.students["ID"] == id
        ].iloc[0]

        name = st.text_input("Name", student["Name"])
        age = st.number_input("Age", min_value=1, value=int(student["Age"]))
        course = st.text_input("Course", student["Course"])
        email = st.text_input("Email", student["Email"])

        if st.button("Update Student"):
            i = st.session_state.students[
                st.session_state.students["ID"] == id
            ].index[0]

            st.session_state.students.loc[i, ["Name", "Age", "Course", "Email"]] = [
                name, age, course, email
            ]

            st.success("Student updated successfully!")
    else:
        st.info("No students available.")

elif menu == "Delete Student":
    st.subheader("Delete Student")

    if not st.session_state.students.empty:
        id = st.selectbox(
            "Select Student ID",
            st.session_state.students["ID"].tolist()
        )

        if st.button("Delete Student"):
            st.session_state.students = st.session_state.students[
                st.session_state.students["ID"] != id
            ].reset_index(drop=True)

            st.success("Student deleted successfully!")
    else:
        st.info("No students available.")
