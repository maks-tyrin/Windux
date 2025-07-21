print('Идет загрузка Windux...')


from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog, scrolledtext
print("Loading Tkiner...")
from math import floor
print('loading math...')
from random import *
print('loading random...')
from PIL import Image, ImageDraw, ImageTk
print('loading Pillow...')
from googletrans import Translator
print('loading Googletran...')
import time
print('loading time... ')
import datetime
print('loading datetime...')
import psutil
print('loading psutil...')
import  subprocess
print('loading subprocess...')
import binascii
print('loading binascii...')
import os
print('loading os...')

import string
print('loading string...')
import keyboard
print("Loading keyboard...")
from threading import Thread





def generate_linux_filenames(count=150, min_length=10, max_length=25):

    filenames = []
    prefixes = ["etc", "var", "tmp", "usr", "dev", "proc", "boot", "lib", "bin", "sbin", "home", "media", "mnt", "sys",
                "run", "opt"]
    extensions = [".conf", ".sh", ".log", ".txt", ".ini", ".json", ".db", ".dat", ".c", ".cpp", ".py", ".h", "", ".o",
                  ".so", ".ko", ".xml", ".yaml"]

    def generate_random_name():
        prefix = choice(prefixes)
        name_length = randint(min_length, max_length)
        name_parts = []


        for _ in range(randint(2, 5)):
            part_length = randint(2, 8)
            name_parts.append("".join(choices(string.ascii_lowercase + string.digits, k=part_length)))


        if random() < 0.6:
            extension = choice(extensions)
            name_parts.append(extension)

        return f"{prefix}_{'_'.join(name_parts)}"

    for _ in range(count):
        filenames.append(generate_random_name())
    return filenames


file_list = generate_linux_filenames(count=150, min_length=15)



COLORS = {
    '1': '#251c91',
    '2': '#149129',
    '3': '#751919',
    '4': '#6a1a87',
    '5': '#d1b62c',
    '6': 'grey',
    '7': 'white'
}

COLORS2 = {
    '1': 'blue',
    '2': 'green', #
    '3': 'red',
    '4': 'purple',
    '5': 'yellow',
    '6': 'grey',
    '7': 'white'
}


root = Tk()
screen_width = root.winfo_screenwidth()


screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg = 'black')
root.overrideredirect(True)
if screen_width!=1920 and screen_height!=1080:
    screen_question = messagebox.askokcancel('warning','Ваше разрешение монитора не подходит, хотите ли вы продолжить не погрузившись полностью')
    if not screen_question:
        root.destroy()
root.wm_attributes("-toolwindow", True)
bg = PhotoImage(file ='bg_lin.png')
label_fon = Label(root, image = bg)
label_fon.image = bg
label_1 = Label(root, text = "OSUS ®",
                font= ('Arial Bold', 35),
                bg = 'black', fg = 'white')
label_1.place(x = 780, y = 100)



bg2 = PhotoImage(file='bg_lin_col (1).png')
is_driver_gpu = False
is_driver_cflc = False
is_driver_rand = False
is_driver_root = False
def Fatal_Error(ERROR):
    messagebox.showerror('ошибка', 'Критическая ошибка!')
    time.sleep(2)
    string = ERROR
    hex_error = binascii.hexlify(string.encode()).decode()
    root.config(cursor="none")
    for widget in root.winfo_children():
        widget.destroy()
    root.update()
    time.sleep(2)
    root.configure(bg = '#0c1a5e')
    #'#0c1a5e'

    label_win_error =  Label(root, text = 'WinDux',
                        bg = '#7f7878', fg = 'white',
                        font = ("Fixedsys", 30),
                        wraplength = 800)
    def center_label(root, label):
        label_win_error.place(y = 180,  x = 885)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        label_width = label_ERROR.winfo_reqwidth()
        label_height = label_ERROR.winfo_reqheight()

        x = (screen_width - label_width) // 2
        y = (screen_height - label_height) // 2

        label_ERROR.place(x=x, y=y)
    label_ERROR = Label(root, text = hex_error,
                        bg = '#0c1a5e', fg = 'white',
                        font = ("Fixedsys", 25),
                        wraplength = 800)
    center_label(root, label_ERROR)

    label_end = Label(root, text = 'Fatal Error. Press Alt+A to restart computer',
                        bg = '#0c1a5e', fg = 'white',
                        font = ("Fixedsys", 25))
    label_end.place(y = 250, x = 620)
    def restart(ERROR):
        if ERROR == "There was no need to download viruses":
            root['bg'] = 'black'
            for widget in root.winfo_children():
                widget.destroy()
            root.update()
            while True:
                for _ in range(35):
                    Label(root, text='your computer is destroyed, data deleted',
                              bg='black', fg='white',
                              font=("Fixedsys", 30)).place(x = 580, y = _*50)

                    root.update()
                    time.sleep(0.05)
                time.sleep(3)
                for widget in root.winfo_children():
                    widget.destroy()
                    root.update()
                    time.sleep(0.05)
        else:
            root.destroy()
    root.bind('<Alt-a>', lambda event: restart(ERROR))




oper = ''
num1 = 0

def show_tree(path, output, indent):

    try:
        entries = os.listdir(path)
        for i, entry in enumerate(entries):
            full_path = os.path.join(path, entry)
            is_last = i == len(entries) - 1
            connector = "└── " if is_last else "├── "
            output.insert(END, "│  " * indent + connector + entry)
            if os.path.isdir(full_path):
                output.insert(END, "\n")
                show_tree(full_path, output, indent + 1 if is_last else indent + 0)
            else:
                output.insert(END, "\n")
    except OSError as e:
        output.insert(END, f"Ошибка доступа: {e}\n")



def rm():
    time.sleep(5)
    for widget in root.winfo_children():
        widget.destroy()
        time.sleep(1)
        root.update()
    Fatal_Error(f"File '{file_list[randint(1, 39)]}' not found")


is_operation = False


def pointr(event):
    global horizontalScale, pen_width, drawing, last_x, last_y, pen_color, canvas, image1, draw

    drawing = False
    last_x, last_y = None, None
    pen_color = "black"
    pen_width = 2

    paint = Toplevel()
    paint.title("PaintDux")
    paint.geometry('420x385')
    paint.transient(root)
    paint.grab_set()
    paint.resizable(width=False, height=False)
    list_names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    def save():
        global image1
        global name
        name = ''
        for _ in range(9):
            name += str(choice(list_names))
        filename = name + ".png"
        image1.save(filename)
        messagebox.showinfo('', f'Файл сохронен под именем {filename}')

    def line_hw(event=None):
        global pen_width
        pen_width = int(horizontalScale.get())

    def start_drawing(event):
        global drawing, last_x, last_y
        drawing = True
        last_x, last_y = event.x, event.y

    def stop_drawing(event):
        global drawing
        drawing = False

    def draw_both(event):
        global last_x, last_y, pen_color, pen_width, image1, draw
        if drawing:
            x1, y1 = last_x, last_y
            x2, y2 = event.x, event.y
            canvas.create_oval(x1 - pen_width, y1 - pen_width, x1 + pen_width, y1 + pen_width,
                               fill=pen_color, outline=pen_color)
            draw.ellipse((x1 - pen_width, y1 - pen_width, x1 + pen_width, y1 + pen_width), fill=pen_color,
                         outline=pen_color)
            last_x, last_y = event.x, event.y

    def change_color(new_color):
        global pen_color
        pen_color = new_color

    def open_image():
        global image1, draw, tk_image
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            try:
                image1 = Image.open(file_path)
                canvas_width = canvas.winfo_width()
                canvas_height = canvas.winfo_height()
                image1 = image1.resize((canvas_width, canvas_height), Image.LANCZOS)
                draw = ImageDraw.Draw(image1)
                tk_image = ImageTk.PhotoImage(image1)
                canvas.create_image(0, 0, image=tk_image, anchor="nw")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    canvas = Canvas(paint, width=400, height=300, bg="white", highlightthickness=1)
    canvas.pack()


    image1 = Image.new('RGB', (400, 300), 'white')
    draw = ImageDraw.Draw(image1)

    colors = ["red", "green", "blue", "black", "orange", "pink"]
    for color in colors:
        btn = Button(paint, text=color.capitalize(), bg=color, command=lambda c=color: change_color(c))
        btn.pack(side=LEFT)

    canvas.bind("<Button-1>", start_drawing)
    canvas.bind("<ButtonRelease-1>", stop_drawing)
    canvas.bind("<B1-Motion>", draw_both)

    horizontalScale = ttk.Scale(paint, length=200, from_=1, to=15, value=pen_width, command=line_hw)
    horizontalScale.pack()

    save_button = Button(paint, text="сохранить", command=save)
    save_button.pack()
    open_but = Button(paint, text='открыть', command=open_image)
    open_but.pack()
LIST_ERROR_VIR = [
    'directory C:/Windux/system69 not found',
    'file C:/Windux/System69/antivirus.dll is corrupted'
    'system is not responding',
    'unknown error'
]
index_error = 0

def errors(root):
    global index_error
    if index_error < len(LIST_ERROR_VIR):
        messagebox.showerror('Fatal Error!', LIST_ERROR_VIR[index_error])
        index_error += 1
        root.after(3000, lambda: errors(root))

def critical_virus():
    messagebox.showerror('Fatal Error', 'file C:/Windux/system69/assembly_02 not found')

    errors(root)
    for widget in root.winfo_children():
        widget.destroy()
        time.sleep(1)
        root.update()
    Fatal_Error("There was no need to download viruses")


#virus mainer
def windux():
    root['bg'] = 'black'
    but_windux2.destroy()
    label_fon.place(x=0, y=0)
    messagebox.showerror('', 'у вас не установлены драйвера на GPU')
    messagebox.showerror('', 'чтобы установить драйвера нажмите на кнопку в нижнем левом углу')


    paint_icon = PhotoImage(file='paint_icon.png')
    but_paint = Button(root, image=paint_icon)
    but_paint.image = paint_icon
    but_paint.place(x=345, y=25)
    but_paint.bind('<Double-Button-1>', pointr)
    def games(event):
        global knb
        win_games = Toplevel()
        win_games.geometry("350x500")
        win_games.title('игры')
        def knb():
            if is_driver_rand:
                win_knb = Toplevel()
                win_knb.geometry('800x600')
                label_ish = Label(win_knb,
                                  text='',
                                  font=('Coming Sans ms', 20))

                def click(user):
                    hot = ['камень', 'ножницы', 'бумага']
                    bot = choice(hot)

                    label_ish.place(x=250, y=150)

                    label.configure(text=f"компьютер выбрал {bot}")
                    if user == bot:
                        label_ish.configure(text='ничья')
                    elif user == 'камень':
                        if bot == 'ножницы':
                            label_ish.configure(text='ты выиграл')
                        else:
                            label_ish.configure(text='ты проиграл')
                    elif user == 'бумага':
                        if bot == 'камень':
                            label_ish.configure(text='ты выиграл')
                        else:
                            label_ish.configure(text='ты проиграл')
                    elif user == 'ножницы':
                        if bot == 'камень':
                            label_ish.configure(text='ты проиграл')
                        else:
                            label_ish.configure(text='ты выиграл')

                but1 = Button(win_knb,
                              text="камень",
                              font=('Coming Sans ms', 20),
                              command=lambda: click('камень'))
                but1.place(y=400, x=100)
                but2 = Button(win_knb,
                              text="ножницы",
                              font=('Coming Sans ms', 20),
                              command=lambda: click('ножницы'))
                but2.place(y=400, x=600)
                but3 = Button(win_knb,
                              text="бумага",
                              font=('Coming Sans ms', 20),
                              command=lambda: click('бумага'))
                but3.place(y=400, x=350)
                label = Label(win_knb, text='', font=('Comic Sans MS', 20))
                label.place(x=180, y=200)
                label1 = Label(win_knb, text='Это игра в камень-ножницы-бумага! ', font=('Comic Sans MS', 20))
                label1.place(x=165, y=0)

            else:
                messagebox.showwarning('', 'Драйвера на случайность не установлены')
        icon_knb = PhotoImage(file = 'unnamed (1).png')
        but_knb = Button(win_games, image= icon_knb,
                         font = ('Arial Bold', 16),
                         command= knb)
        but_knb.image = icon_knb
        but_knb.pack()

        def physic_game():
            messagebox.showinfo('information', 'Эта игра была вырезана')

        icon_physic = PhotoImage(file = 'Снимок экрана (1).png')
        but_physic = Button(win_games, image= icon_physic,
                            command = physic_game)
        but_physic.image = icon_physic
        but_physic.pack()

    icon_games = PhotoImage(file='game_icon.png')
    but_game = Button(root, image= icon_games)
    but_game.image = icon_games
    but_game.place(x = 100, y = 100)
    but_game.bind('<Double-Button-1>', games)
    def calc(event):
        if is_driver_cflc == True:
            messagebox.showwarning('Предупреждение', 'Внимание! Этот калькулятор 8-разрядный, превышение лимита приведет к ошибке ')
            global oper
            global num1
            global is_operation
            win_calc = Toplevel()
            win_calc.geometry("350x450")

            enter_num = Entry(win_calc, width=10,
                              font=('Consolas', 20),
                              justify='right')
            enter_num.place(x=20, y=30)


            def nabor(num):
                len_num = len(enter_num.get())
                if len_num > 8:
                    enter_num.configure(state='disabled')
                else:
                    enter_num.configure(state='normal')
                global oper
                global is_operation
                if is_operation:
                    oper = enter_num.get()
                    enter_num.delete(0, END)
                    is_operation = False

                enter_num.insert(END, str(num))

            def operation(op):
                enter_num.configure(state='normal')
                global num1
                global is_operation
                is_operation = True
                num1 = enter_num.get()
                enter_num.delete(0, END)
                enter_num.insert(END, op)

            def calc1():
                enter_num.configure(state='normal')
                num2 = enter_num.get()
                enter_num.delete(0, END)
                try:
                    if oper == '+':
                        rezultat = float(num1) + float(num2)
                        enter_num.delete(1, END)
                        enter_num.insert(END, rezultat)
                    elif oper == '-':
                        rezultat = float(num1) - float(num2)
                        enter_num.delete(1, END)
                        enter_num.insert(END, rezultat)
                    elif oper == '*':
                        rezultat = float(num1) * float(num2)
                        enter_num.delete(1, END)
                        enter_num.insert(END, rezultat)
                    elif oper == '/':
                        try:
                            rezultat = float(num1) / float(num2)
                            enter_num.delete(1, END)
                            enter_num.insert(END, rezultat)
                        except ZeroDivisionError:
                            enter_num.delete(0, END)
                            enter_num.insert(0, 'ERROR')
                    if len(str(rezultat)) > 8:
                        Fatal_Error('it was necessary to install a normal OS')
                except ValueError:
                    enter_num.delete(0, END)
                    enter_num.insert(0, 'ERROR')

            def clear():
                enter_num.delete(0, END)

            buttons_data = [
                ('1', 20, 100), ('2', 70, 100), ('3', 120, 100),
                ('4', 20, 150), ('5', 70, 150), ('6', 120, 150),
                ('7', 20, 200), ('8', 70, 200), ('9', 120, 200),
                ('0', 20, 250)
            ]

            for text1, x, y in buttons_data:
                button = Button(win_calc, text=text1, font=("Consolas", 17),
                                width=3, height=1,
                                command=lambda text=text1: nabor(text))
                button.place(x=x, y=y)

            but_point = Button(win_calc, text='.',
                               font=("Consolas", 17),
                               width=3, height=1,
                               command=lambda: nabor('.'))
            but_point.place(x=70, y=250)

            but_add = Button(win_calc,
                             text='+',
                             font=("Consolas", 17),
                             width=3, height=1,
                             command=lambda: operation('+'))
            but_add.place(x=170, y=100)
            but_sub = Button(win_calc,
                             text='-',
                             font=("Consolas", 17),
                             width=3, height=1,
                             command=lambda: operation('-'))
            but_sub.place(x=170, y=150)
            but_mult = Button(win_calc,
                              text='*',
                              font=("Consolas", 17),
                              width=3, height=1,
                              command=lambda: operation('*'))
            but_mult.place(x=170, y=200)
            but_div = Button(win_calc,
                             text='/',
                             font=("Consolas", 17),
                             width=3, height=1,
                             command=lambda: operation('/'))
            but_div.place(x=170, y=250)

            but_calc1 = Button(win_calc, text='=',
                               font=("Consolas", 17),
                               width=3, height=1,
                               command=calc1)
            but_calc1.place(x=220, y=100)

            but_clear = Button(win_calc, text='C',
                               font=("Consolas", 17),
                               width=3, height=1,
                               command=clear)
            but_clear.place(x=270, y=100)



        else:
            messagebox.showerror('Ошибка', 'Драйвера на мат. операции не установлены!')
    image_calc = PhotoImage(file ='Calc_icon.png')
    but_calc = Button(root, image = image_calc)
    but_calc.image = image_calc
    but_calc.place(x = 110, y = 25)
    but_calc.bind('<Double-Button-1>', calc)


    def translator(event):
        trans1 = Translator()

        win_trans = Toplevel()
        label23 = Label(win_trans, font='Arial 20 bold', text='выберете')
        label32 = Label(win_trans, font='Arial 20 bold', text='язык! ')

        def rus():
            label23.place_forget()
            label32.place_forget()
            global boti
            boti = 'ru'

        def eng():
            label23.place_forget()
            label32.place_forget()
            global boti
            boti = 'en'

        def trans():
            try:
                global boti
                text = enter1.get('1.0', END)
                a = trans1.translate(text, dest=boti)
                enter2.delete('1.0', END)
                enter2.insert('1.0', a.text)
            except NameError:
                label32.place(x=50, y=45)
                label23.place(x=50, y=10)

        enter1 = Text(win_trans, width=45, height=10,
                      wrap=WORD)
        enter1.place(x=240, y=35)

        enter2 = Text(win_trans, width=45, height=10)
        enter2.place(x=240, y=250)

        but0 = Button(win_trans, text='перевести',
                      command=trans,
                      font='Arial 14 bold')
        but0.place(x=355, y=205)

        label = Label(win_trans, text="введите текст на английском или на русском",
                      font='Arial 15 bold')
        label.place(x=205, y=5)

        but1 = Button(win_trans, text='переводить с английского на русский',
                      font='Arial 13 bold',
                      command=rus)
        but1.place(x=75, y=450)

        but2 = Button(win_trans, text='переводить с русского на английский',
                      font='Arial 13 bold',
                      command=eng)
        but2.place(y=450, x=430)
    icon_trans = PhotoImage(file = 'trans_icon.png')
    but_trans = Button(root, image =icon_trans )
    but_trans.image = icon_trans
    but_trans.place(y = 100, x = 25)
    but_trans.bind('<Double-Button-1>', translator)

    def compilator(event):
        win_compiler = Toplevel(root)
        win_compiler.title("Picharm")
        win_compiler['bg'] = 'black'
        win_compiler.geometry('900x800')
        win_compiler.transient(root)
        win_compiler.grab_set()


        code_editor = scrolledtext.ScrolledText(win_compiler, wrap=WORD, width=80,
                                                height=20,
                                                bg='black', fg='white',
                                                insertbackground='white')
        code_editor.pack(pady=10)
        code_editor.insert("1.0", "# Напишите свой Python код здесь\nprint('Привет, мир!')\n")


        output_window = scrolledtext.ScrolledText(win_compiler, wrap=WORD, width=80, height=10,
                                                  state="normal",
                                                  bg='black', fg='white',
                                                  insertbackground='white'
                                                  )
        output_window.pack(pady=10)


        def run_code():
            code_text = code_editor.get("1.0", "end-1c")

            try:

                with open("temp_code.py", "w", encoding="utf-8") as temp_file:
                    temp_file.write(code_text)


                result = subprocess.run(['python', 'temp_code.py'], capture_output=True, text=True, check=True)

                output_window.config(state='normal')
                output_window.delete("1.0", "end")
                output_window.insert("1.0", result.stdout)
            except subprocess.CalledProcessError as e:
                output_window.config(state='normal')
                output_window.delete("1.0", "end")
                output_window.insert("1.0", e.stderr)
            except Exception as e:
                messagebox.showerror("Error", f"Произошла ошибка: {e}")

            os.remove("temp_code.py")
            output_window.config(state="disabled")
        run_button = Button(win_compiler, text="Запустить", command=run_code,
                            bg='black', fg='white')
        run_button.pack(pady=5)

    icon_compiler = PhotoImage(file = 'python_icon.png')
    but_compiler = Button(root, image = icon_compiler,
                          command = compilator)
    but_compiler.image = icon_compiler
    but_compiler.place(x = 195, y = 25)



    def terminal(event):

        win_ter = Toplevel()
        win_ter.geometry('700x500')
        win_ter.transient(root)
        win_ter.grab_set()
        win_ter.configure(bg = 'grey')
        ter_input = Text(win_ter, width= 40, height= 25,
                   bg = 'black', fg = 'white',
                   font = ('Consolas', 12),
                   insertbackground='white',
                   selectbackground= 'white', selectforeground= 'black')
        ter_input.place(x = 0, y = 22)
        label_input = Label(win_ter,text = 'input',
                            fg = 'white', bg = 'grey')
        label_input.place(x = 100, y = 0)
        ter_output = Text(win_ter, width= 40, height= 25,
                   bg = '#1c1b1b', fg = 'white',
                   font = ('Consolas', 12),
                   insertbackground='white',
                   selectbackground= 'white', selectforeground= 'black')
        ter_output.place(y = 22, x = 360)
        label_output = Label(win_ter, text='output',
                            fg='white', bg='grey')
        label_output.place(x=450, y=0)
        #ter_input.insert('1.0', '>')
        list_command = [
            'exit',
            'clear',
            'calc', 'knb', 'note',
            'tree [folder]',
            'info [folder]',
            'echo [text]',
            'apt install [driver]',
            'text_color [color]',
            'bg_color [color]',
            'sudo [command]', '     rm -rf/'
        ]
        def com():
            global is_driver_gpu, is_driver_cflc, is_driver_rand, is_driver_root
            user_command = ter_input.get('1.0', END).strip()
            output = ''

            #ter_input.mark_set("insert", "end-1c")
            #ter_input.insert('0.0', '>')
            #в блокноте размер шрифта

            if user_command == 'help':
                for commands in list_command:
                    #for string in range(1, len(list_command) +1):
                    output += commands + '\n'
            elif user_command == 'cd C:/cat.exe':
                import time
                ter_output.delete(0.0, END)
                ter_output.insert(0.0, 'Format disk...\n')
                win_ter.update()
                time.sleep(5)
                ter_output.insert(END, 'Remove BIOS...\n')
                messagebox.showerror('Error', 'Fatal error!')
                win_ter.destroy()
                critical_virus()

            elif user_command.startswith('sudo '):
                if is_driver_root:
                    root_command = user_command[5:]
                    if root_command == 'rm -rf/':
                        import time
                        for x in range(0, 10):
                            for file in file_list:
                                ter_output.see(END)
                                time.sleep(0.005)
                                ter_output.insert(END,f'rm: {file}\n' )
                                win_ter.update()
                        else:
                            win_ter.destroy()
                            rm()

                    else:
                        output = 'root_command not found'
                else:
                    output = 'driver_root is not installed'
            elif user_command.startswith("apt install "):
                inst = user_command[12:].strip()
                import time
                for _ in range(5):
                    ter_input.mark_set("insert", 0.0)
                    ter_output.delete(0.0, END)
                    ter_output.insert(END, '\n')
                    ter_output.insert(END, 'Installing driver...|' )
                    win_ter.update()
                    time.sleep(0.5)
                    ter_output.delete(0.0, END)
                    ter_output.insert(END,'Installing driver.../' )
                    win_ter.update()
                    time.sleep(0.5)
                    ter_output.delete(0.0, END)
                    ter_output.insert(END,'Installing driver...―' )
                    win_ter.update()
                    time.sleep(0.5)
                    ter_output.delete(0.0, END)
                    ter_output.insert(END,'Installing driver...\ ' )
                    win_ter.update()
                    time.sleep(0.5)
                    ter_output.delete(0.0, END)
                    ter_input.mark_set("insert", 0.0)
                if inst == 'driver_GPU':
                    label_fon.configure(image=bg2)
                    is_driver_gpu = True
                    messagebox.showinfo('', 'Драйвера на GPU установлены!')
                elif inst == "driver_calc":
                    is_driver_cflc = True
                    messagebox.showinfo('', 'Драйвера на математические операции установлены!')
                elif inst == 'driver_rand':
                    is_driver_rand= True
                    messagebox.showinfo('', 'Драйвера на случайность установлены!')
                elif inst == 'driver_root':
                    is_driver_root = True
                    output = 'driver_root is installed'
                else:
                    output = ('not found this paket\n'
                              'driver_root\n, driver_calc\n, driver_rand\n, driver_gpu'
                              )

            elif user_command.startswith('text_color '):
                user_color = user_command.split(' ')[1]
                if user_color in COLORS:
                    if ter_output['bg'] != COLORS[user_color]:

                        ter_input.configure(fg = COLORS[user_color])
                        ter_output.configure(fg=COLORS[user_color])
                    else:
                        output = 'this operation is not possible'
                else:
                    output = 'this color not found\n'
                    for color in COLORS2:
                        output += f'{color}:{COLORS2[color]}' + '\n'

            elif user_command.startswith('bg_color '):
                user_color = user_command.split(' ')[1]

                if user_color in COLORS:
                    if ter_output['fg'] != COLORS[user_color]:
                        ter_input.configure(bg = COLORS[user_color])
                        ter_output.configure(bg=COLORS[user_color])

                        for color in COLORS2:
                            output += f'{color}:{COLORS2[color]}' + '\n'
                    else:
                        output = 'this operation is not possible'
                else:
                    output = 'this color not found\n'
            elif user_command == 'clear':
                ter_output.delete('1.0', END)
            elif user_command == 'exit':
                win_ter.destroy()
            elif user_command == 'calc':
                calc()
            elif user_command == 'knb':
                games()
                knb()
            elif user_command == 'note':
                note()
            elif user_command.startswith("tree "):
                path = user_command[5:].strip()
                if not os.path.exists(path):
                    ter_output.insert(END, f"Ошибка: Каталог '{path}' не существует.\n")
                    return
                ter_output.insert(END, f"Дерево каталогов для '{path}':\n")
                show_tree(path, ter_output, 0)
            elif user_command.startswith("info "):
                path = user_command[5:].strip()
                if not os.path.exists(path):
                    ter_output.insert(END, f"Ошибка: Каталог '{path}' не существует.\n")
                    return

                total_size = 0
                num_files = 0
                num_folders = 0

                for root, dirs, files in os.walk(path):
                    total_size += sum(os.path.getsize(os.path.join(root, name)) for name in files)
                    num_files += len(files)
                    num_folders += len(dirs)

                size_mb = total_size / (1024 * 1024)

                ter_output.insert(END, f"Информация о каталоге '{path}':\n")
                ter_output.insert(END, f"Общий размер: {size_mb:.2f} МB\n")
                ter_output.insert(END, f"Количество файлов: {num_files}\n")
                ter_output.insert(END, f"Количество папок: {num_folders}\n")


            elif user_command.startswith("echo"):
                output = user_command[5:].strip()

            else:
                output = 'command not found'
            try:
                ter_output.insert(END, f">{user_command}\n{output}\n")
                ter_input.delete('1.0', END)
                ter_output.see(END)
            except Exception:
                pass


        try:
            ter_input.bind("<Return>", lambda event : com())
        except Exception:
            pass
    image_cmd = PhotoImage(file ='command_icon.png')
    but_terminal = Button(root, image = image_cmd)
    but_terminal.image = image_cmd
    but_terminal.place(x = 25, y = 25)
    but_terminal.bind('<Double-Button-1>', terminal)
    def ttime():
        win_time = Toplevel()
        win_time.geometry('600x200')
        label_time = Label(win_time, text="0",
                           font=("Arial", 15),
                           bg='white', fg='blue')
        label_time.place(x=25, y=50)

        def secs():
            now = datetime.datetime.now()
            my_format = now.strftime("время: %H:%M:%S   *число: %Y %B %d %A   ")
            label_time.configure(text=f'{my_format}')

            win_time.update()
            win_time.after(1000, secs)

        secs()
    but_time = Button(root, text = datetime.datetime.now().strftime("%H:%M"),
                       bg = 'blue', font = ("Consolas", 15),
                      command = ttime)
    def time():
        try:
            but_time.configure(text = datetime.datetime.now().strftime("%H:%M"))
        except Exception:
            pass
        root.update()
        root.after(30000, time)
    time()


    but_time.place(x = 1850, y =1000 )


    def note(event):
        win_note = Toplevel()
        win_note.title('Блокнот')
        win_note.geometry("700x550")
        win_note.transient(root)
        win_note.grab_set()

        def tema(theme):
            text['bg'] = view_colors[theme]['text_bg']
            text['fg'] = view_colors[theme]['text_fg']
            text['insertbackground'] = view_colors[theme]['cursor']

        def fontss(fontis):
            text['font'] = fonts[fontis]['font']

        def close():
            ans = messagebox.askokcancel('выход', 'Вы действительно хотите выйти?')
            if ans:
                win_note.destroy()

        def open_file():
            file_path = filedialog.askopenfilename(title='Выбор файла',
                                                   filetypes=(('текстовые документы', "*.txt"), ('все файлы', '*.*')))
            if file_path:
                text.delete('1.0', END)
                try:
                    with open(file_path, encoding='utf-8') as f:
                        file_content = f.read()
                        text.delete('1.0', END)
                        text.insert(END, file_content)
                except FileNotFoundError:
                    messagebox.showerror("Ошибка", "Файл не найден.")
                    Fatal_Error('FileNotFoundError')
                except UnicodeDecodeError:
                    messagebox.showerror("Ошибка", "Ошибка декодирования файла. Возможно, неверная кодировка.")
                    Fatal_Error('UnicodeDecodeError')
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

        def save_file():
            file_path = filedialog.asksaveasfilename(title='Сохранить файл',
                                                     defaultextension=".txt",
                                                     filetypes=(('Текстовые документы', "*.txt"), ('Все файлы', "*.*")))
            if file_path:
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        text1 = text.get('1.0', END)
                        f.write(text1)
                    messagebox.showinfo("Успех", "Файл сохранен!")
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Ошибка при сохранении файла: {e}")

        menu = Menu(win_note)

        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label='Oткрыть', command=open_file)
        file_menu.add_command(label='Сохранить', command=save_file)
        file_menu.add_separator()
        file_menu.add_command(label='закрыть', command=close)
        win_note.config(menu=file_menu)

        view_menu = Menu(menu, tearoff=0)
        view_menu_sub = Menu(view_menu, tearoff=0)
        font_menu = Menu(view_menu, tearoff=0)

        view_menu.add_cascade(label='Тема', menu=view_menu_sub)
        view_menu_sub.add_command(label='Темная', command=lambda: tema('dark'))
        view_menu_sub.add_command(label='Светлая', command=lambda: tema('light'))

        view_menu.add_cascade(label='Шрифт', menu=font_menu)
        font_menu.add_command(label='Arial', command=lambda: fontss('Arial'))
        font_menu.add_command(label='Consolas', command=lambda: fontss('cons'))
        font_menu.add_command(label='Fixedsys', command=lambda: fontss('Fixed'))

        win_note.config(menu=view_menu)

        menu.add_cascade(label='File', menu=file_menu)
        menu.add_cascade(label='Вид', menu=view_menu)

        win_note.config(menu=menu)

        frame_text = Frame(win_note)
        frame_text.pack(fill=BOTH, expand=1)

        view_colors = {
            'dark': {
                "text_bg": 'black', 'text_fg': 'white', 'cursor': 'white'
            },

            'light': {
                'text_bg': 'white', 'text_fg': 'black', 'cursor': 'black'
            }
        }

        fonts = {
            'Arial': {
                'font': 'Arial 13 Bold'
            },
            'cons': {
                'font': ('Consolas', 13, 'bold')
            },
            'Fixed': {
                'font': ('Fixedsys', 13)
            }
        }

        text = Text(frame_text, bg='white', fg='black',
                    font=("Arial Bold", 13),
                    padx=10, pady=25,
                    wrap=WORD,
                    spacing3=10,
                    width=50)
        text.pack(expand=1, fill=BOTH, side=LEFT)

        scroll = Scrollbar(frame_text, command=text.yview)
        scroll.pack(side=LEFT, fill=Y)
        text.configure(yscrollcommand=scroll.set)


    icon_note = PhotoImage(file = 'note_icon (1).png')
    but_note = Button(root,image = icon_note)
    but_note.image = icon_note
    but_note.place(y = 25, x = 270)
    but_note.bind('<Double-Button-1>', note)

    def virus():
        label_vir = Label(root, image=icon_virus).pack()
        but_virus.destroy()
        root.update()
        import time
        time.sleep(4)


        class DummyEvent:
            def __init__(self):
                self.widget = None

        dummy_event = DummyEvent()
        terminal(dummy_event)
        messagebox.showwarning('', 'Напишите команду <<cd C:/cat.exe>> чтобы увидеть котиков ')

    icon_virus = PhotoImage(file='icon_vir.png')
    but_virus = Button(root, image=icon_virus,
                       command = virus)
    but_virus.image = icon_virus
    but_virus.place(y=400, x=75)

    def startp():
        start = Toplevel()
        start.geometry('400x600')
        def driver():
            global is_driver_gpu
            global is_driver_cflc
            global is_driver_rand
            win_driver = Toplevel()
            win_driver.geometry("300x500")
            def driver_gpu():
                global is_driver_gpu
                messagebox.showinfo('', 'Драйвера на GPU установлены!')
                label_fon.configure(image=bg2)
                is_driver_gpu = True
                but_driver_gpu.pack_forget()



            but_driver_gpu = Button(win_driver,
                                    text = 'установить драйвера на GPU',
                                    command = driver_gpu)
            if is_driver_gpu == False:
                but_driver_gpu.pack()
            def driver_calc():
                global is_driver_cflc
                is_driver_cflc = True
                messagebox.showinfo('', 'Драйвера на математические операции установлены!')

            but_driver_calc = Button(win_driver,
                                     text = 'установить драйвера на математические операции',
                                     command = driver_calc)
            if is_driver_cflc == False:
                but_driver_calc.pack()
            def driver_rand():

                global is_driver_rand
                is_driver_rand = True
                messagebox.showinfo('', 'Драйвера на случайность установлены!')

            but_driver_rand = Button(win_driver,
                                     text = 'установить драйвера на случайность',
                                     command = driver_rand)
            if is_driver_rand == False:
                but_driver_rand .pack()



        but_gpu = Button(start, text = 'Драйвера',
                         command = driver)
        but_gpu.pack()
        def exit_root():
            ans_exit = messagebox.askokcancel('Выход', 'вы действительно хотите выйти?')
            if ans_exit:
                messagebox.showinfo('завершение работы', 'завершение работы WinDux')
                if is_driver_gpu == True:
                    zav_driver = PhotoImage(file ='EndWorkColor.png')
                    label_zavdriver = Label(root, image = zav_driver)
                    label_zavdriver.place(x = 0, y = 0)
                    root.update()
                    import time
                    time.sleep(2)
                    root.update()
                    root.quit()
                else:
                    zav_driver = PhotoImage(file='EndWork.png')
                    label_zavdriver = Label(root, image=zav_driver)
                    label_zavdriver.place(x=0, y=0)
                    root.update()
                    import time
                    time.sleep(2)
                    root.update()
                    root.quit()
        but_exit_root = Button(start, text = 'выйти',
                               font = ("Consolas Bold", 14),
                               command = exit_root)
        but_exit_root.place(x = 320, y= 550)
        def dis():
            win_dis = Toplevel()
            win_dis.title("дисTпечер задач")
            win_dis.geometry("600x500")
            def cpu_dis():
                but_dis_cpu.place_forget()
                but_dis_ram.place_forget()
                frame_cpu = Frame(win_dis,
                                  width= 600, height= 500)
                frame_cpu.pack()
                label_cpu_dis = Label(frame_cpu, text = "процессор: не распознано]}",
                                      font = ('Arial Bold', 15))
                label_cpu_dis.place(x = 10, y = 10)

                label_cpu_ger_dis = Label(frame_cpu, text = f'текущая частота: {psutil.cpu_freq().current/ 1000} HZ',
                                          font = ('Arial Bold', 15))
                label_cpu_ger_dis.place(x = 10, y = 70)
                def ger():

                    label_cpu_ger_dis.configure(text = f'текущая частота: {psutil.cpu_freq().current/ 1000} HZ')
                    win_dis.update()
                    win_dis.after(1000, ger)
                label_cpu_zag_dis = Label(frame_cpu, text=f'загруженность: {psutil.cpu_percent()}',
                                          font = ('Arial Bold', 15))
                label_cpu_zag_dis.place(x=10, y=40)
                def zagr():
                    label_cpu_zag_dis.configure(text =f'загруженность: {psutil.cpu_percent()} %' )
                    win_dis.update()
                    win_dis.after(1000, zagr)
                zagr()
                ger()
                def exit_dis():
                    but_dis_cpu.place(x=20, y=5)
                    but_dis_ram.place(x=150, y=5)
                    frame_cpu.pack_forget()
                but_exit = Button(frame_cpu, text = 'выйти',
                                  font = ('Arial Bold', 15),
                                  command = exit_dis)
                but_exit.place(x = 20, y = 450)
            def dis_ram():
                but_dis_cpu.place_forget()
                but_dis_ram.place_forget()
                frame_ram = Frame(win_dis,
                                  width= 600, height= 500)
                frame_ram.pack()
                ram_info = psutil.virtual_memory()
                label_ram_dis = Label(frame_ram,
                                      text =f'объем ОЗУ: {ram_info.total / 1024 / 1024 / 1024:.2f} GB' ,
                                      font = ('Arial Bold', 15))
                label_ram_use = Label(frame_ram,
                                      text = f'используется: {ram_info.used / 1024 / 1024 / 1024:.2f} GB ({ram_info.percent}%)',
                                      font = ('Arial Bold', 15))
                def ram_use():
                    ram_info = psutil.virtual_memory()
                    label_ram_use.configure( text = f'используется: {ram_info.used / 1024 / 1024 / 1024:.2f} GB ({ram_info.percent}%)')
                    win_dis.update()
                    win_dis.after(1000, ram_use)
                ram_use()
                label_ram_dis.place(x = 20, y = 10)
                label_ram_use.place(x = 20, y = 40)
                def ram_exit():
                    but_dis_cpu.place(x=20, y=5)
                    but_dis_ram.place(x=150, y=5)
                    frame_ram.pack_forget()
                but_exit_ram = Button(frame_ram, text = 'выйти',
                                      font = ('Arial Bold', 15),
                                      command = ram_exit)
                but_exit_ram.place(x = 20, y = 450)
            but_dis_cpu = Button(win_dis, text = 'процессор',
                                 font = ('Arial Bold', 13),
                                 command = cpu_dis)
            but_dis_cpu.place(x = 20, y = 5)
            but_dis_ram = Button(win_dis, text = 'ОЗУ',
                                 font = ('Arial Bold', 13),
                                 command = dis_ram)
            but_dis_ram.place(x = 150, y = 5)
        but_dis = Button(start, text = 'диспетчер задач', command = dis)
        but_dis.pack()

        def info():
            window_info = Toplevel()

            window_info.geometry('600x250')

            label_main = Label(window_info, text='WinDux', font=('Consolas', 25))
            label_main.pack()

            label_version = Label(window_info, text='Версия: Windux UbuXep 1.0 Release')
            label_version.place(x=25, y=50)

            Label(window_info,
                  text='Это псевдо ОС Windux. Она написана на Python в шутку и собрала все самые известные ').place(
                x=25, y=50)
            Label(window_info, text='приколы из реальных ОС ').place(x=25, y=65)
            Label(window_info,
                  text='Внимание!!! Эта программа никак не влияет на компьютер, без ведома пользователя она ничего не сделает с компютером').place(
                x=25, y=90)
            Label(window_info, text='ничего не сделает с компютером').place(x=25, y=105)

            label_version = Label(window_info, text='Версия: Windux UbuXep 1.0 Release')
            label_version.place(x=25, y=130)

            Label(window_info, text='Сайт: http://winduxos.ulcraft.com').place(x=25, y=155)
            Label(window_info, text='Телеграм канал: @Windux_UbuXep').place(x=25, y=180)
            count = 0

            def click():
                nonlocal count
                count += 1
                if count == 3:
                    messagebox.showwarning('', 'Да хватит на меня тыкать!👾')

            Button(window_info, text='Помощь', command=click).place(x=25, y=220)

        but_information = Button(start, text='О программе', command=info)
        but_information.pack()
#time

    icon_boom = PhotoImage(file='Boom_icon.png')
    but_start = Button(root, image=icon_boom, command= startp)
    but_start.image = icon_boom

    but_start.place(x = 10, y = 1020)

    def Casino(event):

        casino_window = Toplevel()
        casino_window.geometry("800x600")
        casino_window.configure(background='grey')
        casino_window.title("Casino")

        def start_():
            root.update()
            import time
            nonlocal casino_window
            casino_window.configure(bg='black')
            button_start.destroy()
            list_strings = ['...',
                            'launch CIH.exe',
                            'implementation in C:/WinDux/system69/kernel32.dll',
                            'procces kernel69 prervon',
                            'overwriting of BIOS',
                            'rm CIH.exe']
            time.sleep(2)
            for string in list_strings:
                Label(casino_window, text=string, fg='white', bg='black').pack(anchor='nw')
                root.update()
                time.sleep(0.5)

            for _ in range(25):
                Label(casino_window, text='/CIH', fg='white', bg='black').pack(anchor='nw')
                root.update()
                time.sleep(0.05)

            casino_window.destroy()
            Fatal_Error('UNEXPECTED_KERNEL_MODE_TRAP')

        button_start = Button(casino_window, text='Войти', bg='pink', fg='black', font=('Harlow Solid', 35, 'bold'),
                              command=start_)
        button_start.pack(expand=True)

    icon_casino = PhotoImage(file='Casino.png')
    but_casino = Button(root, image=icon_casino)
    but_casino.image = icon_casino
    but_casino.place(y=400, x=500)
    but_casino.bind('<Double-Button-1>', Casino)

    def on_button_press(event, button):
        button.start_x = event.x
        button.start_y = event.y

    def on_mouse_drag(event, button):
        x = button.winfo_x() - button.start_x + event.x
        y = button.winfo_y() - button.start_y + event.y
        button.place(x=x, y=y)

    but_calc.bind("<ButtonPress-1>", lambda event: on_button_press(event, but_calc))
    but_calc.bind("<B1-Motion>", lambda event: on_mouse_drag(event, but_calc))

    but_paint.bind("<ButtonPress-1>", lambda event: on_button_press(event, but_paint))
    but_paint.bind("<B1-Motion>", lambda event: on_mouse_drag(event, but_paint))

    but_note.bind("<ButtonPress-1>", lambda event: on_button_press(event, but_note))
    but_note.bind("<B1-Motion>", lambda event: on_mouse_drag(event, but_note))

    but_game.bind("<ButtonPress-1>", lambda event: on_button_press(event, but_game))
    but_game.bind("<B1-Motion>", lambda event: on_mouse_drag(event, but_game))

    but_terminal.bind("<ButtonPress-1>", lambda event: on_button_press(event, but_terminal))
    but_terminal.bind("<B1-Motion>", lambda event: on_mouse_drag(event, but_terminal))

    but_trans.bind("<ButtonPress-1>", lambda event: on_button_press(event, but_trans))
    but_trans.bind("<B1-Motion>", lambda event: on_mouse_drag(event, but_trans))

    but_compiler.bind("<ButtonPress-1>", lambda event: on_button_press(event, but_compiler))
    but_compiler.bind("<B1-Motion>", lambda event: on_mouse_drag(event, but_compiler))

    def Win():
        keyboard.add_hotkey('win', startp, suppress= True)
        keyboard.wait()
    thread_win = Thread(target=Win, daemon=True)
    thread_win.start()


    keyboard.block_key('win')

    root.bind("<Super_L>", startp())
    root.bind("<Super_R>", startp())



def zag():
    but_windux2.pack_forget()
    root['bg'] = 'white'

    zags = PhotoImage(file='logo_windux.png')
    helloing = PhotoImage(file='helloing (1).png')
    label_zag = Label(root, image = zags)

    label_zag.place(x = 300, y = 0)
    root.update()


    time.sleep(2)
    label_zag2 = Label(root, image= helloing)
    label_zag2.place(x = 0, y = 0)
    root.update()
    time.sleep(3)
    label_zag2.place_forget()
    label_zag.place_forget()
    but_windux.place_forget()
    but_bios.place_forget()
    label_1.place_forget()
    windux()



but_windux = Button(root, text = 'Windux UbuXep',
                    font=('Arial Bold', 16),
                    bg='black', fg='white',
                    command=zag)


but_windux.place(x = 900, y = 450)








def bios():
    but_windux2.destroy()

    but_windux.place_forget()
    label_1.place_forget()
    but_bios.place_forget()
    root.configure(bg = 'white')
    label_time = Label(root, text="0",
                       font=("Arial", 15),
                       bg='white', fg='blue')
    label_time.place(x=25, y=50)
    def secs():
        sec = time.time()
        tyme = time.ctime(sec)
        label_time.configure(text= f'Time: {tyme}')

        root.update()
        root.after(1000, secs)
    secs()


    label_bios = Label(root, text = 'version BIOS: 1.00',
                       font = ("Arial", 15),
                       bg = 'white', fg = 'blue')
    label_bios.place(x = 25, y = 100)
    label_cpu = Label(root, text = 'не распознано',
                      font=("Arial", 15),
                      bg='white', fg='blue')
    label_cpu.place(x = 25, y = 150)

    label_cpu_temp = Label(root, text='Temperature of CPU: (137°C/ 303°F)',
                      font=("Arial", 15),
                      bg='white', fg='blue')
    label_cpu_temp.place(x = 25, y = 250)
    hdd = psutil.disk_usage('/')
    label_hdd = Label(root, text=f'HDD: {floor(hdd.total /(2**30))} GB',
                      font=("Arial", 15),
                      bg='white', fg='blue')
    label_hdd.place(x = 25, y = 300)
    ram_info = psutil.virtual_memory()
    label_ram = Label(root, text=f'RAM: {ram_info.total / 1024 / 1024 / 1024:.2f} GB',
                      font=("Arial", 15),
                      bg='white', fg='blue')
    label_ram.place(x = 25, y = 350)

    def re_bios():
        labels_bios = [label_cpu, label_cpu_temp,
                       label_ram, label_hdd, label_time, label_bios]
        for label in labels_bios:
            label.destroy()
        but_per.place_forget()
        label_flash = Label(root, text='have you inserted a USB flash drive?',
                            font=("Arial", 15),
                            bg='white', fg='blue')
        label_flash.pack()


        def per_bios():
            ttk.Progressbar(orient="horizontal", length=150, value=20).pack(pady=5)
            but_yes.place_forget()
            but_no.place_forget()
            label_flash.place_forget()
            blue_screen = PhotoImage(file='bluescreen(22).png')
            label_blue_screen = Label(root, image=blue_screen)
            label_blue_screen.image = blue_screen
            label_blue_screen.place(x=0, y=0)

        but_yes = Button(root, text = "yes",
                         font=("Arial", 15),
                         bg='white', fg='blue',
                         command = per_bios)
        def no_per_bios():

            label_no_bios = Label(root, text = 'тогда тебе тут нечего делать',
                                  font=("Arial", 15),
                                  bg='white', fg='blue')
            label_no_bios.pack()
            root.update()
            time.sleep(2)
            label_no_bios.pack_forget()

            blue_screen = PhotoImage(file='bluescreen(22).png')
            label_blue_screen = Label(root, image=blue_screen)
            label_blue_screen.image = blue_screen
            label_blue_screen.place(x=0, y=0)

            but_yes.place_forget()
            but_no.place_forget()
            label_flash.place_forget()

        but_no = Button(root, text = "no",
                         font=("Arial", 15),
                         bg='white', fg='blue',
                         command = no_per_bios)
        but_no.place(x = 450, y = 300)
        but_yes.place(x = 500, y = 300)
    but_per = Button(root, text='re-flash BIOS',
                      font=("Arial", 15),
                      bg='white', fg='blue',
                      command = re_bios)
    but_per.place(x=25, y=400)





but_bios = Button(root, text = 'BIOS',
                  font =('Fixedsys', 16),
                  bg = 'black', fg = 'white',
                  command= bios)
but_bios.place(x = 900, y = 350)

value = 0
state = 1


def welcome(name):
    global  is_driver_gpu
    messagebox.showwarning('Error', 'Несоответствие клавиатуры')
    messagebox.showinfo('', f'привет {name[:: -1]}')
    is_driver_gpu = True
    bg_new = PhotoImage(file = 'bg3.png')
    label_fon.configure(image= bg_new)
    label_fon.image = bg_new
    root['bg'] = 'green'
    root.after(2000, windux)
def inst_win2():
    label_1.destroy()
    but_bios.destroy()
    but_windux.destroy()
    but_windux2.destroy()
    zast_image = PhotoImage(file='zast.png')
    label_inst2 = Label(root, image= zast_image)
    label_inst2.image = zast_image
    label_inst2.place(x = 0, y = 0)
    root.update()
    time.sleep(3)
    root.update()
    label_inst2.destroy()
    root['bg'] = '#0c1a5e'

    def install_win2():

        def registracia():
            progress_bar.destroy()
            label_proces.destroy()
            label_info = Label(root, text = 'Name: ',
                               bg='#0c1a5e', fg='white',
                               font=('Consolas Bold', 15))
            label_info.place(x = 250, y = 220)
            user_info = Text(root, width= 10, height= 1,
                             font=('Consolas Bold', 15))
            user_info.place(x = 330, y = 220)

            but_name = Button(root, text = 'OK',
                              command = lambda: (welcome(user_info.get('1.0', END)),
                                                 label_info.destroy(),
                                                 but_name.destroy(),
                                                 user_info.destroy()) ,
                              bg='#0c1a5e', fg='white',
                               font=('Consolas Bold', 15))
            but_name.place(x = 350, y = 250)



        def start_inst():
            global value, state
            progress_bar['value'] += randint(1, 3)

            if state == 1 and progress_bar['value'] >= 20:
                state = 2
            elif state == 2 and progress_bar['value'] >= 40:
                state = 3
            elif state == 3 and progress_bar['value'] >= 90:
                state = 4

            if state == 1:
                text = f'Checking disk... {progress_bar["value"]}%'
            elif state == 2:
                text = f'Format disk... {progress_bar["value"]}%'
            elif state == 3:
                text = f'Copying files... {progress_bar["value"]}%'
            elif state == 4:
                text = f'Finishing installing... {progress_bar["value"]}%'
            else:
                text = "Installation complete!"

            label_proces.config(text=text)

            if progress_bar['value'] < 100:
                root.after(randint(400, 900), start_inst)
            else:

                registracia()

        label_hellloing.destroy()
        but_start_inst.destroy()

        s = ttk.Style()
        s.theme_use('clam')
        s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
        progress_bar = ttk.Progressbar(root, orient="horizontal", length=300,
                                       #mode="determinate",
                                       variable = value, maximum=100,
                                       style = 'yellow.Horizontal.TProgressbar')
        progress_bar.place(x = 820, y = 380)

        label_proces = Label(root,
                             text=f'checking disk... {progress_bar['value']} %',
                             bg='#0c1a5e', fg='white',
                             font=('Consolas Bold', 15))
        label_proces.place(x=860, y=350)
        start_inst()
    label_hellloing = Label(root, text = 'Welcome to installer of WinDux UbuXep2.0',
                            bg = '#0c1a5e', fg = 'white',
                            font = ('Consolas Bold', 20))
    label_hellloing.place(x = 720, y = 100)
    but_start_inst = Button(root, text = 'Install Windux UbuXep 2.0',
                            bg='#0c1a5e', fg='white',
                            font = ('Consolas Bold', 18),
                            command= install_win2)
    but_start_inst.place(x = 790, y = 280)



image_inst2 = PhotoImage(file= 'inst2.0.png')
but_windux2 = Button(root, image= image_inst2,
                     command= inst_win2)
but_windux2.image = image_inst2
but_windux2.place(x = 20, y = 900)



root.mainloop()

