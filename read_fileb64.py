import sys
from converter_base64 import base64_tohex
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLabel

def show_result_in_window(result_hex):
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Result in Hexadecimal")

    layout = QVBoxLayout()

    label = QLabel("Converted Result:")
    text_area = QTextEdit()
    text_area.setReadOnly(True)
    text_area.setText(result_hex)

    layout.addWidget(label)
    layout.addWidget(text_area)

    window.setLayout(layout)
    window.resize(600, 400)
    window.show()

    sys.exit(app.exec_())

def main():
    if len(sys.argv) != 2:
        print("Use: python read_fileb64.py <path_file>")
        sys.exit(1)

    path_file = sys.argv[1]

    try:
        with open(path_file, 'r') as file:
            content_base64 = file.read().strip()
    except FileNotFoundError:
        print(f"File not found: {path_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading the file {e}")
        sys.exit(1)

    result_hex = base64_tohex(content_base64)
    show_result_in_window(result_hex)

if __name__ == "__main__":
    main()
