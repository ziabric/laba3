from llm_rs import AutoModel
import tkinter as tk

def send_text():
    text_to_copy = entry1.get("1.0", tk.END)
    entry2.delete("1.0", tk.END)
    entry2.insert("1.0", model.generate(text_to_copy).text)


model = AutoModel.from_pretrained("./ruGPT-3.5-13B-ggml", model_file="./ruGPT-3.5-13B-q4_0.bin")

root = tk.Tk()
root.title("Chat")

entry1 = tk.Text(root, width=50, height=8)
entry1.pack()

entry2 = tk.Text(root, width=50, height=8)
entry2.pack()

copy_button = tk.Button(root, text="Send", command=send_text)
copy_button.pack()

root.mainloop()
