import pickle
import streamlit as st
from win32com.client import Dispatch

def speak(text):
	speak=Dispatch(("SAPI.SpVoice"))
	speak.Speak(text)
model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))

def main():
	st.title("Email & SMS Spam Classification")
	st.subheader("Built with streamlit & python")
	msg=st.text_input("Enter a Text")
	if st.button("predict"):
		data=[msg]
		vect=cv.transform(data).toarray()
		prediction=model.predict(vect)
		result=prediction[0]
		if result==1:
			st.error("This is spam message")
			speak("this is spam message")
		else:
			st.success("This is ham message")
			speak("This is ham message")
main()