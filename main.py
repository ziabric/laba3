from llm_rs import AutoModel
import tkinter as tk


def generate_text():
    prompt = text_input.get("1.0", tk.END)
    text_output.configure(state='normal')
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", model.generate(prompt).text)
    text_output.configure(state='disabled')


model = AutoModel.from_pretrained("./ruGPT-3.5-13B-ggml", model_file="./ruGPT-3.5-13B-q4_0.bin")

root = tk.Tk()
root.title("ruGPT-3.5 13B")

text_input = tk.Text(root, width=80, height=8, font="Arial 18", padx=10, pady=10)
text_input.pack()

text_output = tk.Text(root, width=80, height=8, font="Arial 18", padx=10, pady=10, state="disabled")
text_output.pack()

generate_button = tk.Button(root, text="Generate", command=generate_text, font="Arial 18")
generate_button.pack()

root.mainloop()
