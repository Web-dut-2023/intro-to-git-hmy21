from openai import OpenAI

client = OpenAI(api_key="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")
import time
from pathlib import Path
import tkinter as tk




#设置窗口大小，位置
def window_set(root, width, height):
    screenwidth = root.winfo_screenwidth()  #获取显示器尺寸
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 5)
    root.geometry(size)
    root.update()

# 创建tkinter GUI应用程序
root = tk.Tk()
root.title("OpenAI Text-Davinci-003")
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
window_set(root,800,500)
# root.iconphoto(False, tkinter.PhotoImage(file='D:\yt_dlp_python_GUI\logo_icon\lucid.png'))  # logo
# root.iconbitmap(default=r'icon\r14.ico')   # 更改窗口图标
root.resizable(False, False) # 设置窗口大小不可变


# 创建输入框
input_field = tk.Text(root,font=("SimSun", 12),wrap='word',bg='#A1CBD1')
input_field.place(x=0, y=0,width=700,height=50)

# 创建文本框，用于显示机器人的回复文本
response_field = tk.Text(root,font=("SimSun", 12),bg='black',fg='orange',wrap='word')
response_field.place(x=0, y=50,width=800,height=450)


# 创建按钮，用于发送输入文本到OpenAI API
def send_input():
    # 获取输入文本
    input_text = input_field.get("1.0",'end')
    response_field.insert(tk.END, '\n\nYou:' + input_text)
    # 调用OpenAI API，获取回复文本
    response = client.completions.create(model='text-davinci-003',
    # 用户提供的输入文本，用于指导GPT输出
    prompt=input_text,
    # 控制输出的多样性，0-1，其中0表示最保守的输出，1表示最多样化的输出。
    temperature=0,
    # 输出的最大长度（输入+输出的token不能大于模型的最大token）,可以动态调整
    max_tokens=1500,
    # [控制字符的重复度] -2.0 ~ 2.0 之间的数字，正值会根据新 tokens 在文本中的现有频率对其进行惩罚，从而降低模型逐字重复同一行的可能性
    frequency_penalty=0.2,
    # [控制主题的重复度] -2.0 ~ 2.0 之间的数字，正值会根据到目前为止是否出现在文本中来惩罚新 tokens，从而增加模型谈论新主题的可能性
    presence_penalty=0.15)
    # 显示回复文本到GUI界面上的文本框中
    result = generated_text = response.choices[0].text.strip()

    response_field.insert(tk.END,'GPT-3:'+ result)


send_button = tk.Button(root, font=("SimSun", 12),text="发送", command=send_input,bg='#FCC09C')
send_button.place(x=700, y=0,width=100,height=50)

# 运行tkinter GUI应用程序
root.mainloop()

"""
class Chat_bot:
    def __init__(self, model):
        self.user = "\nYou: "
        self.bot = "GPT-3: "
        self.model = model
        self.question_list = []
        self.answer_list = []
        self.text = ''
        self.turns = []
        self.last_result = ''

    def dialogue_save(self):
        timestamp = time.strftime("%Y%m%d-%H%M-%S", time.localtime())
        file_name = 'output/Chat_' + timestamp + '.md'
        f = Path(file_name)
        f.parent.mkdir(parents=True, exist_ok=True)
        with open(file_name, "w", encoding="utf-8") as f:
            for q, a in zip(self.question_list, self.answer_list):
                f.write(f"You: {q}\nGPT-3: {a}\n\n")
        print("对话内容已保存到文件中: " + file_name)

    def Generate(self, user_input):
        question = user_input
        self.question_list.append(question)
        prompt = self.bot + self.text + self.user + question

        try:
            response = openai.Completion.create(
                model=self.model,
                prompt=prompt,
                temperature=0,
                max_tokens=1500,
                frequency_penalty=0.2,
                presence_penalty=0.15,
            )
            result = response["choices"][0]["text"].strip()
            self.answer_list.append(result)

            self.last_result = result
            self.turns += [question] + [result]
            if len(self.turns) <= 10:
                self.text = " ".join(self.turns)
            else:
                self.text = " ".join(self.turns[-10:])
            print(result)
        except Exception as exc:
            print(exc)

        self.dialogue_save()
        return result
"""