from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton

import sys

import os
import openai

openai.api_key = "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"


def get_ai(input_str: str) -> str:
    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: {input_str}",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    result = response.to_dict()['choices'][0].to_dict()['text']
    # print(result)
    return result


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.input = QLineEdit()
        self.button = QPushButton("Submit")
        self.title = QLabel("Ask something:")
        self.label1 = QLabel()
        self.label2 = QLabel()

        self.input_str = ""
        self.input.textChanged.connect(self.add_string)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)
        self.container = QWidget()
        self.container.setLayout(self.layout)
        # Set the central widget of the Window.
        self.setCentralWidget(self.container)

    def add_string(self, a_string: str):
        return self.input_str + a_string

    def the_button_was_clicked(self):
        import time
        print("Clicked!")

        result = get_ai(self.input_str)
        time.sleep(2)

        self.label1.setText(result.replace("\n\n", ""))

        self.layout.addWidget(self.label1)
        self.container.setLayout(self.layout)
        # Set the central widget of the Window.
        self.setCentralWidget(self.container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
