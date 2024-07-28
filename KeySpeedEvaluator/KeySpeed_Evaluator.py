from tkinter import *
import time
from PIL import Image, ImageTk
from tkinter import ttk
import random
import configparser
from datetime import datetime
import sqlite3
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import keyboard
import subprocess



# Create a configuration object
config = configparser.ConfigParser()
def define_all():
    global first_typed
    first_typed = False
    global st_time, timeremaining, difficulty, easy_sen, medium_sen, hard_sen,choised_para,typed_para, stored_name
    timeremaining = 15
    stored_name = ""
    difficulty = 'Easy'
    easy_sen = ["the sun is shining brightly in the sky","i love eating delicious chocolate ice cream","my cat enjoys chasing after laser pointers","birds sing sweetly in the morning","the quick brown fox jumps over the lazy dog","the red apple is on the table"]
    medium_sen = ["A mysterious old man lived at the end of the street.","The intricate pattern on the Persian rug fascinated me.","She played the piano with great skill and precision.","The scientific community debates the existence of parallel universes.","The ancient artifact was carefully preserved in a museum.","The detective followed the suspect through a labyrinth of narrow alleyways"]
    hard_sen = ["Quantum entanglement is a phenomenon that challenges classical physics.","The intricacies of neurobiology are still not fully understood.","The symphony orchestra's performance captivated the audience.","The mathematician devised a groundbreaking algorithm for encryption.","The esoteric principles of quantum field theory perplex many physicists.","In astrophysics, the concept of a black hole singularity remains enigmatic."]
    choised_para = " ".join(random.choice(easy_sen) for _ in range(15)) 
    typed_para = ""
root = Tk()
root.geometry("1850x570")
root.attributes('-alpha', 0.98)
root.state('zoomed')
easy_sen = ["the sun is shining brightly in the sky","i love eating delicious chocolate ice cream","my cat enjoys chasing after laser pointers","birds sing sweetly in the morning","the quick brown fox jumps over the lazy dog","the red apple is on the table"]
medium_sen = ["A mysterious old man lived at the end of the street.","The intricate pattern on the Persian rug fascinated me.","She played the piano with great skill and precision.","The scientific community debates the existence of parallel universes.","The ancient artifact was carefully preserved in a museum.","The detective followed the suspect through a labyrinth of narrow alleyways"]
hard_sen = ["Quantum entanglement is a phenomenon that challenges classical physics.","The intricacies of neurobiology are still not fully understood.","The symphony orchestra's performance captivated the audience.","The mathematician devised a groundbreaking algorithm for encryption.","The esoteric principles of quantum field theory perplex many physicists.","In astrophysics, the concept of a black hole singularity remains enigmatic."]

def on_canvas_scroll(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")


# Create a Canvas widget
canvas = Canvas(root, borderwidth=0, background="white")

# Create a Vertical Scrollbar
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Bind the mouse wheel to the canvas for scrolling
canvas.bind_all("<MouseWheel>", on_canvas_scroll)
root_frame = Frame(root)
f1 = Frame(root_frame)
f1.pack(fill=X)
label = Label(f1, text="KeySpeed Evaluator",bg="orange",font="Sans 35 bold",fg="black").pack(fill=X)
root_frame.pack(fill=X)

f2 = Frame(root_frame)
type_photo = ImageTk.PhotoImage(Image.open("Images\\logo_img.jpg").resize((500, 300)))
Label(f2, image= type_photo).pack(side="left",pady=40,padx=20)
txt = """
Double your typing speed. Learn keyboarding in the fun way. 
Test your wpm speed and accuracy. Play top-notch typing games.
Find it all from KeySpeed Evaluator! KeySpeed Evaluator for Windows is a 
complete touch typing tutor application with a real-time analysis widget."""
f3 = Frame(f2)
text_label = Label(f3,text=txt,font="Sans 15 bold")
text_label.pack(side="top",pady=60)


# start_buttn1 = ImageTk.PhotoImage(Image.open("Images\\car2.png").resize((160, 160)))
# start_buttn = Button(f3, image=start_buttn1,border=0).pack(side="bottom")
f2.pack()
f3.pack()

begin_image = ImageTk.PhotoImage(Image.open("Images\\learn_photo.png").resize((400,550)))
game_image = ImageTk.PhotoImage(Image.open("Images\\game_photo.png").resize((400,550)))
tree1_img = ImageTk.PhotoImage(Image.open("Images\\tree1.png").resize((400,550)))
tree2_img = ImageTk.PhotoImage(Image.open("Images\\tree2.png").resize((400,550)))
tree3_img = ImageTk.PhotoImage(Image.open("Images\\tree3.png").resize((400,550)))
f4 = Frame(root_frame)



def name_entry_page():
    global win_name_entry, stored_name
    # Retrieve the stored username
    try:
        win_name_entry = "null"
        config.read('config.ini')
        stored_name = config['User']['username']
        main_page()
    except:
        win_name_entry = Toplevel(root)
        win_name_entry.geometry("1850x570")
        win_name_entry.attributes('-alpha', 0.98)
        win_name_entry.state('zoomed')
        label = Label(win_name_entry, text="Enter Your name:",font="Sans 22")
        label.place(x=515,y=150)

        entry = Entry(win_name_entry,font="Sans 22")
        entry.place(x=480,y=210)
        
        def btn_start():
            global stored_name
                    # Store a username
            username = str(entry.get())
            config['User'] = {'username': username}
            # Save the username to a configuration file
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            stored_name = username
            main_page()
            
        
        btn_img = PhotoImage(file="C:\\Users\\hp\\Downloads\\btn_start.png")
        go_btn = Button(win_name_entry,image=btn_img,border=0,command=btn_start)
        go_btn.place(x=615,y=270)
        
        win_name_entry.mainloop()

define_all()
def typing_page():
    global win_name_entry
    try:
        if(win_name_entry != "null"):
            win_name_entry.destroy()
    except:
        pass
    global type_win
    type_win = Toplevel(root)
    type_win.geometry("1850x570")
    type_win.attributes('-alpha', 0.98)
    type_win.state('zoomed')
    
    def define_all():
        global first_typed
        first_typed = False
        global st_time, timeremaining, difficulty, easy_sen, medium_sen, hard_sen,choised_para,typed_para
        timeremaining = 15
        difficulty = 'Easy'
        easy_sen = ["the sun is shining brightly in the sky","i love eating delicious chocolate ice cream","my cat enjoys chasing after laser pointers","birds sing sweetly in the morning","the quick brown fox jumps over the lazy dog","the red apple is on the table"]
        medium_sen = ["A mysterious old man lived at the end of the street.","The intricate pattern on the Persian rug fascinated me.","She played the piano with great skill and precision.","The scientific community debates the existence of parallel universes.","The ancient artifact was carefully preserved in a museum.","The detective followed the suspect through a labyrinth of narrow alleyways"]
        hard_sen = ["Quantum entanglement is a phenomenon that challenges classical physics.","The intricacies of neurobiology are still not fully understood.","The symphony orchestra's performance captivated the audience.","The mathematician devised a groundbreaking algorithm for encryption.","The esoteric principles of quantum field theory perplex many physicists.","In astrophysics, the concept of a black hole singularity remains enigmatic."]
        choised_para = " ".join(random.choice(easy_sen) for _ in range(15)) 
        typed_para = ""
    define_all()
    type_win.config(bg="#d9d9d9")
    style=Frame(type_win,highlightthickness=10,bg="yellow",padx=250,pady=5,borderwidth=5,relief=SUNKEN)
    style.pack(fill="y")
    timer_label = Label(type_win, text="Timer: 15 sec", font=("Arial", 16),bg="#ffffff")

    def start_timer(time_r):
        global timer_id, remaining_time
        remaining_time = time_r
        update_timer_display()
        timer()

    def update_timer_display():
        timer_label.config(text=f"Timer: {remaining_time} sec")

    def change_time():
        global timeremaining
        if(timeremaining == 15 or timeremaining == 30 or timeremaining == 45):
            timeremaining += 15
        elif(timeremaining == 60):
            timeremaining = 120
        else:
            timeremaining = 15
        timer_label.config(text=f"Timer: {timeremaining} sec")


    def timer():
        global timer_id, remaining_time,timeremaining,difficulty,choised_para, typed_para
        if remaining_time > 0:
            remaining_time -= 1
            update_timer_display()
            timer_id = type_win.after(1000, timer)
        else:
            timer_label.config(text="Timer finished!")
            text_type.config(state="disabled")
            # checker(len(text_type.get('1.0',END)),text_type.get('1.0',END))
            sqliteConnection = sqlite3.connect('Database\\keySpeed.db')
            cursor = sqliteConnection.cursor()

            sqlite_insert_query = """INSERT INTO clientName
                                    (Score,Time,Difficulty) 
                                    VALUES 
                                    (?,?,?)"""
                                    

            sqliteConnection = sqlite3.connect('Database\\keySpeed.db')
            cursor = sqliteConnection.cursor()
            typed_paraa = text_type.get('1.0',END)
            typed_para = typed_paraa
            ch = choised_para
            length = len(typed_para.split())-1
            res = 0 
            correct = 0
            while (res<len(typed_paraa.split())-1):
                if(typed_paraa.split()[res]==ch.split()[res]):
                    correct+=1
                res+=1
            wpm = round((correct*(60/timeremaining)),2)
            data_tuple2 = (str(wpm),str(timeremaining),str(difficulty))
            cursor.execute(sqlite_insert_query,data_tuple2)
            sqliteConnection.commit()
            time.sleep(2)
            typing_result_page()

    def choose_diff(event):
        global difficulty, easy_sen, medium_sen , hard_sen, choised_para
        difficulty = diff_Combo.get()
        if(difficulty ==  "Medium"):
            choised_para = " ".join(random.choice(medium_sen) for _ in range(15)) 
        elif(difficulty == "Hard"):
            choised_para = " ".join(random.choice(hard_sen) for _ in range(15)) 
        else:
            choised_para = " ".join(random.choice(easy_sen) for _ in range(15)) 
        text_para.config(state=NORMAL)
        text_para.delete("1.0", END)
        text_para.insert("1.0", choised_para)
        text_para.config(state=DISABLED)
        
    def restart_type():
        type_win.destroy()
        typing_page()

    def on_key(event):
        global first_typed,timeremaining
        try:
            textt = text_type.get("1.0", END)
            if not textt.strip():
                return
            textt=textt.strip()
            
            if(text_type.get("1.0", END)[-2] == ' '):
                textt += " "
                if(textt != text_type.get("1.0", END)):
                    text_type.delete('1.0',END)
                    text_type.insert('1.0',textt)
                    
            reference_words = text_para.get("1.0", END).split()
            entered_words = textt.split()
            text_para.tag_remove("correct", "1.0", "end")
            text_para.tag_remove("incorrect", "1.0", "end")   
            if(not first_typed):
                start_timer(timeremaining)
                first_typed = True
                 
            
            for i in range(len(reference_words)):
                reference_word = reference_words[i]
                entered_word = entered_words[i]
                if(i == len(entered_words)-1):
                    if reference_word == entered_word:
                        text_para.tag_add("correct", f"1.{len(' '.join(reference_words[:i]))}", f"1.{(len(' '.join(reference_words[:i])) + len(reference_word)+1)}")
                        text_para.tag_config("correct", foreground="black")
                        
                if i >= (len(entered_words)-1):
                    break
                if reference_word == entered_word:
                    text_para.tag_add("correct", f"1.{len(' '.join(reference_words[:i]))}", f"1.{(len(' '.join(reference_words[:i])) + len(reference_word)+1)}")
                    text_para.tag_config("correct", foreground="black")
                else:
                    text_para.tag_add("incorrect", f"1.{len(' '.join(reference_words[:i]))}", f"1.{(len(' '.join(reference_words[:i])) + len(reference_word)+1)}")
                    text_para.tag_config("incorrect", foreground="red")
                        
        except Exception as e:
            pass


    diff_Combo = ttk.Combobox(type_win,value = ['Easy','Medium','Hard'],state="readonly",font=('Times',16))
    diff_Combo.current(0)

    diff_Combo.bind("<<ComboboxSelected>>",choose_diff)

    back_img = PhotoImage(file="C:\\Users\\hp\\Downloads\\Back_btn.png")
    timer_img = PhotoImage(file="C:\\Users\\hp\\Downloads\\icon_timer.png")
    rest_img = PhotoImage(file=r"C:\Users\hp\Downloads\restart_btn1.png")
    Button_back = Button(type_win,image=back_img,bg="#d9d9d9",relief="flat",command=type_win.destroy)
    Button_timer = Button(type_win,image=timer_img,relief="flat",bg="#ffffff",command=change_time)
    Button_restart = Button(type_win,image=rest_img,relief="flat",border=0,command=restart_type)

    text_para = Text(type_win, height=7, width=85,wrap=WORD, font=("Times", 20))
    text_para.insert("1.0", choised_para)
    text_para.config(foreground="#787878", background="#ffffff")
    text_para.config(state=DISABLED)
    
    

    text_type = Text(type_win, height=8, width=85, font=("Courier", 18))
    text_type.insert("1.0", "")
    text_type.tag_add("light", "1.0", "end")
    text_type.tag_configure("light", foreground="lightgreen")
    
    def disable_paste(event):
        # Do nothing when paste (Ctrl+V or Command+V) is pressed
        return "break"
    text_type.bind("<Control-v>", disable_paste)
    text_type.bind("<Key>", on_key)
    
    
    style.place(x=25, y=80)
    text_para.place(x=25, y=80)
    Button_restart.place(x=1150, y=370)
    text_type.place(x=25, y=400)
    Button_back.place(x=14,y=10)
    Button_timer.place(x=850,y=12)
    timer_label.place(x=700,y=12)
    diff_Combo.place(x=920,y=14)

    type_win.mainloop()

def typing_result_page():
    global type_win, fig,difficulty
    try:
        type_win.destroy()
    except:
        pass
    global choised_para, timeremaining, typed_para
    win_typing_result = Toplevel(root)
    win_typing_result.geometry("1850x570")
    win_typing_result.attributes('-alpha', 0.98)
    win_typing_result.state('zoomed')
    win_typing_result.config(bg="#d9d9d9")
    
    def load_data():
        global canvas_widget, fig, score_now
        sqliteConnection = sqlite3.connect('Database\\keySpeed.db')
        cursor = sqliteConnection.cursor()
        r_set=cursor.execute('''SELECT * from clientName''')
        # Create a Matplotlib figure and axis
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        l_y = []
        i = 0
        tot = 0
        highest_score = 0
        for data in r_set:
            if(difficulty == data[3]):
                tot += 1
                if(int(float(data[1]))>highest_score):
                    highest_score = int(float(data[1]))
                l_y.append(int(float(data[1])))
            

        l_y = l_y[tot-8:]
        l_y.insert(0,highest_score)
        
        
        l2 = []
        h = 1
        for j in l_y:
            l2.append(h)
            h+=1

        # Data for the bar graph
        categories = l2
        values = l_y

        # Create the bar graph
        bars = ax.bar(categories, values)
        scores = l_y
        # Add scores as text labels on top of the bars
        for bar, score in zip(bars, scores):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(score),
                    ha='center', va='bottom')

        # Create a Tkinter canvas to display the Matplotlib figure
        
        
    
    def restart_btn():
        win_typing_result.destroy()
        typing_page()
    
    def checker():
        global score_now
        length = len(typed_para.split())-1
        res = 0 
        correct = 0
        while (res<len(typed_para.split())-1):
            if(typed_para.split()[res]==choised_para.split()[res]):
                correct+=1
            res+=1
        score_now = round((correct*(60/timeremaining)),2)
        accuracy_label.config(text=f"Accuracy : {round(((correct/length)*100),2)}%")
        wpm_label.config(text=f" {round((correct*(60/timeremaining)),2)} ")
        
        
    global stored_name
    
    frame1 = Frame(win_typing_result,height=650,width=1000,bg="#F6F7FE",border=2)
    config.read('config.ini')
    stored_name = config['User']['username']
    head_label = Label(frame1, text=stored_name,font="Courier 20 bold",bg="#ffffff")
    frame2 = Frame(frame1,height=200,width=950,bg="#F6F7FE")
    frame2_f1 = Frame(frame2,height=200,width=200,bg="#FCEFB4",padx=15)
    frame2_f2 = Frame(frame2,height=200,width=150,bg="#B5FEA3",padx=15)
    frame_showcase = Frame(frame2_f1,height=200,width=200,bg="#ffff0f",padx=15)
    wpm_label_text = Label(frame_showcase, text="WPM",font=("Sans",18),bg="#ffff0f")
    wpm_label = Label(frame_showcase, text="20",font=("Sans",25),bg="#ffff0f")
    diff_label = Label(frame2_f2, text=f"Mode: {difficulty}",font=("Sans",20),bg="#B5FEA3")
    time_label = Label(frame2_f2, text=f"Time: {timeremaining}s",font=("Sans",16),bg="#B5FEA3",pady=15)
    accuracy_label = Label(frame2_f1, text="Accuracy : ",font=("Sans",17),bg="#ffffff",pady=15)
    frame3 = Frame(frame1,height=200,width=950,bg="#F6F7FE",padx=15)
    checker()
    load_data()
    canvas = FigureCanvasTkAgg(fig, master=frame3)
    btn_restart = Button(frame3, text="Restart",bg="#ffffff",relief="flat",command=restart_btn)
    canvas_widget = canvas.get_tk_widget()
    
    
    frame1.pack()
    head_label.pack()
    frame2.pack()
    frame_showcase.pack()
    frame2_f1.pack(side='left')
    wpm_label.pack()
    wpm_label_text.pack()
    accuracy_label.pack()
    frame2_f2.pack(side='right')
    diff_label.pack()
    time_label.pack()
    frame3.pack()
    canvas_widget.pack()
    btn_restart.pack()
    
    win_typing_result.mainloop()
    

def main_page():
    win_main_page = Toplevel(root)
    win_main_page.geometry('1100x700')
    win_main_page.minsize(800,600)
    win_main_page.state("zoomed")
    root_frame = Frame(win_main_page)
    f1 = Frame(root_frame)

    img_load1 =  ImageTk.PhotoImage(Image.open("Images\\typing_practice.png").resize((340,240)))
    img_load2 = ImageTk.PhotoImage(Image.open("Images\\learn_typing.png").resize((435,285)))
    img_load3 = ImageTk.PhotoImage(Image.open("Images\\typing_game.png").resize((410,235)))
    img_load4 = ImageTk.PhotoImage(Image.open("Images\\performanceimg.png").resize((390,280)))

    f2 = Frame(f1)
    image1 = Label(f2, image=img_load1,cursor="hand2")
    image1.pack()
    text1 = Label(f2, text='Start Typing',font="Helvetica 14 bold").pack()
    f2.pack(side='left', pady=10)

    f3 = Frame(f1)
    image2 = Label(f3, image=img_load2,cursor="hand2")
    image2.pack()
    text1 = Label(f3, text='Learn To Type',font="Helvetica 14 bold").pack()
    f3.pack(side='left')

    f1.pack()

    ff1 = Frame(root_frame)
    f4 = Frame(ff1)
    image3 = Label(f4, image=img_load3,cursor="hand2")
    image3.pack()
    text1 = Label(f4, text='play Games',font="Helvetica 14 bold").pack()
    f4.pack(side='left')

    f5 = Frame(ff1)
    image4 = Label(f5, image=img_load4,cursor="hand2")
    image4.pack()
    text1 = Label(f5, text='Performance',font="Helvetica 14 bold").pack()
    f5.pack(side='left')
    ff1.pack()

    def image_typing_practice(event):
        typing_page()

    def image_learn_typing(event):
        win_learn_typing = Toplevel(root)
        win_learn_typing.state("zoomed")
        win_learn_typing.title("KeySpeed Evaluator")
        win_learn_typing.config(bg="#ffffff")

        label_heading = Label(win_learn_typing, text="Keys - Remember Point",background="green",fg="#ffffff",font="Sans 18 bold").pack(fill=X)


        f1_learn = Frame(win_learn_typing)
        keyboard_keys_img = ImageTk.PhotoImage(Image.open("Images\\keyboard_typing_learn.png").resize((350,220)))
        keyboard_placement_img = ImageTk.PhotoImage(Image.open("Images\\learn_typing_keyboard.png").resize((350,220)))
        next_btn_img = ImageTk.PhotoImage(Image.open("Images\\next_btn.png").resize((150,115)))
        

        txt = """Explore the world of touch typing through this engaging image. 
        The keyboard is a canvas of colors, with each key uniquely shaded to guide your fingers. 
        Watch as skilled fingers gracefully hover over the keyboard, ready to press the right keys. 
        It's like a visual roadmap for learning touch typing - where the colors help you know which key to press. 
        Teaching touch typing isn't just about the keys; 
        it's about creating a smooth and colorful journey for your fingers on the keyboard.
        Get ready for a fun and educational experience!"""

        label_txt = Label(f1_learn,text=txt,font="Times 15")

        label_keyboard = Label(f1_learn,image=keyboard_keys_img)
        label_keyboard2 = Label(f1_learn,image=keyboard_placement_img)

        label_keyboard.pack(side='left',pady=20,padx=10)
        label_txt.pack(padx=20,pady=50)
        f1_learn.pack(fill=X)
        label_heading = Label(win_learn_typing, text="Finger Placement",background="green",fg="#ffffff",font="Sans 18 bold").pack(fill=X)

        
        def move_type():
            win_learn_write = Toplevel(win_learn_typing)
            win_learn_write.state("zoomed")
            win_learn_write.config(bg="#ffffff")
            
            text_widget = Text(win_learn_write,wrap=NONE,height=2,font=("Sans 24 bold"))
            answer = "asdf jkl; asdf aassddffjjkkll;; asdf jkl; rteu iop nmvcxz rewq rraakk uuooxz zzxxccvvz nnmmuuii aqz swx dec frv tgb yhn ujm ik, ol. p;/ bbvncx the sun rises over a quiet town fields of green stretch far and wide a gentle breeze rustles the leaves of tall trees a river flows calmly through the landscape birds chirp in harmony as they welcome the new day children laugh and play in the open fields flowers bloom in a riot of colors under the warm sunlight a cat lounges lazily on a porch steps a dog runs freely, chasing its tail with joy friends gather in a park, sharing stories and laughter a simple life, filled with moments of happiness and tranquility take a deep breath, feel the rhythm of the simple, beautiful world around you and type away with ease and confidence as you embrace the flow of words on your keyboard"
            text_widget.insert("1.0",answer)
            text_widget.pack(side='top',fill=X,padx=10,pady=5)
            text_widget.config(fg='#b0b0b0')
            text_widget.config(state='disabled')
            global k, sp_scroll
            k = 0
            sp_scroll = 10
            def key_event(e):
                global k, label_hand,hand_display_img,sp_scroll
                list = [[1,2,3,4,5,6,7,8,9,10],["aqz","swx","dec","frvtgb"," ","","jumyhn","ik,","ol.","p;/"]]
                lst_hands = ["Images\\finger1.png","Images\\finger2.png","Images\\finger3.png","Images\\finger4.png","Images\\finger5.png","Images\\finger6.png","Images\\finger7.png","Images\\finger8.png","Images\\finger9.png","Images\\finger10.png"]
                text_type = text_widget.get("1.0",END)
                ch = "no"
                if(k<len(text_type)):
                    ch = text_type[k+1]
                text_type = text_type[:k]
                if e.event_type == keyboard.KEY_DOWN:
                    if e.name == 'backspace':
                        if(k> 0):
                            k-=1
                        text_type = text_type[:len(text_type)-1]
                        text_widget.tag_remove("correct", "1.0", "end")
                        text_widget.tag_add("correct", f"1.0", f"1.{len(text_type)}")
                        text_widget.tag_config("correct", foreground="black")
                    
                    if(k < len(answer) or len(text_type) < len(answer)):
                        if(answer[k] == e.name or (e.name == 'space' and answer[k] == ' ')):
                            if(len(text_type.strip()) >= 11):
                                text_widget.xview_scroll(sp_scroll,'pixels')
                            k += 1
                            text_type += answer[k-1]
                            text_widget.tag_add("correct", f"1.0", f"1.{len(text_type)}")
                            text_widget.tag_config("correct", foreground="black")
                            if(ch != "no"):
                                j = 0
                                for i in list[1]:
                                    j+=1
                                    if(ch in i):
                                        break
                                hand_display_img = ImageTk.PhotoImage(Image.open(lst_hands[list[0][j-1]-1]).resize((380,220)))
                                label_hand.config(image=hand_display_img)
            keyboard.hook(key_event)
            global label_hand,hand_display_img
            hand_display_img = ImageTk.PhotoImage(Image.open("Images\\hands.png").resize((380,220)))
            label_hand = Label(win_learn_write, image=hand_display_img)
            label_hand.pack(side="bottom",pady=20)
            keyboard_display_img = ImageTk.PhotoImage(Image.open("Images\\keyboard_display.png").resize((650,180)))
            label = Label(win_learn_write, image=keyboard_display_img)
            label.pack(anchor="center",pady=20)
            
            win_learn_write.mainloop()

        f2_learn = Frame(win_learn_typing)

        txt = """Get ready to start touch typing like a pro! 
        In this image, your left-hand fingers find their place on A, S, D, and F, while your right-hand fingers 
        rest on J, K, L, and semicolon (;). This is your home row, the foundation of efficient typing. 
        Let muscle memory take over as you position your fingers strategically for a smooth and accurate typing 
        experience. Mastering the home row is the key to building speed and precision. 
        Let's start typing with confidence!"""

        label_txt = Label(f2_learn,text=txt,font="Times 15")

        label_keyboard2 = Label(f2_learn,image=keyboard_placement_img)

        label_keyboard2.pack(side='left',pady=20,padx=10)
        label_txt.pack(padx=20,pady=50)
        btn_cont = Button(win_learn_typing,image=next_btn_img,border=0,cursor="hand2",command=move_type)
        f2_learn.pack(fill=X)
        btn_cont.pack(padx=5,fill=X)
        win_learn_typing.mainloop()



    def image_typing_game(event):
        win_game_mainpage = Toplevel(root)
        win_game_mainpage.state('zoomed')
        f1 = Frame(win_game_mainpage)

        img_load1  = ImageTk.PhotoImage(Image.open("Images\\car_race.png").resize((420,250)))
        img_load2 = ImageTk.PhotoImage(Image.open("Images\\bird_game.png").resize((400,260)))
        
        def car_race_game(event):
            def choose_car():
                pass
            
            def start_game():
                pass
            
            def main_game():
                win_car_game = Toplevel(root)
                win_car_game.state('zoomed')
                global isworking, ismiddleroad,isfinishroad
                isworking = True
                ismiddleroad = False
                isfinishroad = False
                global k, text_type, speed_curr,speed_prev, time_start, time_end,road_startx,road_finishx,road_stripx,road_stripx2,road_middlex
                global carx, car2x
                carx = 125
                car2x = 125
                road_startx = -20
                road_finishx = 0
                road_stripx = 0
                road_stripx2 = 1630
                road_middlex = -20
                time_start = 0
                time_end = 0
                img_load1 = ImageTk.PhotoImage(Image.open("Images\\sky_bg.png").resize((1300,1200)))
                img_load2 = ImageTk.PhotoImage(Image.open("Images\\full_roadwithouBg.png").resize((1600,250)))
                img_load3 = ImageTk.PhotoImage(Image.open("Images\\land_img.png").resize((1300,800)))
                img_loadcar = ImageTk.PhotoImage(Image.open("Images\\car2.png"))
                img_loadcar2 = ImageTk.PhotoImage(Image.open("Images\\car1.png"))
                img_road_start = ImageTk.PhotoImage(Image.open("Images\\road_start.png").resize((2000,250)))
                img_road_finish = ImageTk.PhotoImage(Image.open("Images\\road_finish.png").resize((2000,250)))
                img_roadstrip = ImageTk.PhotoImage(Image.open("Images\\road_strip.png").resize((1600,10)))
                img_road_middle = ImageTk.PhotoImage(Image.open("Images\\road_middle.png").resize((2000,250)))

                image1 = Label(win_car_game, image=img_load1).place(x=0,y=0)
                image1 = Label(win_car_game, image=img_load3).place(x=0,y=350)
                btn_road = Button(win_car_game, image=img_road_start,highlightthickness=0,border=0)
                btn_road.place(x=road_startx,y=250)
                btn_roadstrip = Button(win_car_game, image=img_roadstrip,highlightthickness=0,border=0)
                # btn_roadstrip.place(x=road_stripx,y=370)
                btn_roadstrip2 = Button(win_car_game, image=img_roadstrip,highlightthickness=0,border=0)
                # btn_roadstrip2.place(x=road_stripx2,y=370)
                image_car = Button(win_car_game, image=img_loadcar,background="#222222",border=0)
                image_car.place(x=carx,y=300)
                image_car2 = Button(win_car_game, image=img_loadcar2,background="#222222",border=0)
                image_car2.place(x=car2x,y=420)
                
                text_widget = Text(win_car_game,wrap=NONE,height=2,font=("Sans 18 bold"))
                
                
                answer = "This is the text for typing I am increasing the text now you can see it through testing all the things are not working accordingly This is for typing and checking for the correct speed"
                text_widget.insert("1.0",answer)
                text_widget.pack(side='bottom')
                text_widget.config(fg='#b0b0b0')
                text_widget.config(state='disabled')
                text_type = ""
                speed_curr = 1
                speed_prev = 1
                k = 0
                label_timer = Label(win_car_game, text="00",font="Sans 18 bold")
                label_timer.pack(side='bottom')
                
                sqliteConnection = sqlite3.connect('Database\\keySpeed.db')
                cursor = sqliteConnection.cursor()
                r_set=cursor.execute('''SELECT * from clientName''')
                
                global isCrossed
                isCrossed = False
                
                highest_score = 0
                for data in r_set:
                    if(int(float(data[1]))>highest_score):
                        highest_score = int(float(data[1]))
                global time_s
                time_s = 1
                
                def update_timer():
                    global time_s
                    time_s += 1
                    label_timer.config(text=f"{time_s}")
                    win_car_game.after(1000,update_timer)
                
                def key_event(e):
                    global k, text_type, speed_curr, time_start, time_end, speed_prev, isworking
                    if e.event_type == keyboard.KEY_DOWN:
                        if(time_start == 0):
                            now = datetime.now()
                            now = now.strftime("%H:%M:%S")
                            time_start = datetime.strptime(str(now),"%H:%M:%S")
                            update_timer()
                        if e.name == 'backspace':
                            k-=1
                            text_type = text_type[:len(text_type)-1]
                            text_widget.tag_remove("correct", "1.0", "end")
                            text_widget.tag_add("correct", f"1.0", f"1.{len(text_type)}")
                            text_widget.tag_config("correct", foreground="black")
                        
                        if(k < len(answer) or len(text_type) < len(answer)):
                            if(answer[k] == e.name or (e.name == 'space' and answer[k] == ' ')):
                                now = datetime.now()
                                now = now.strftime("%H:%M:%S")
                                time_now = datetime.strptime(str(now),"%H:%M:%S")
                                diff = time_now - time_start
                                time_now = diff.total_seconds()
                                try:
                                    sp = round((int(len(text_type)/4)*(60/time_now)),2)
                                    speed_curr = round(sp/10, 1)
                                except:
                                    speed_curr = 1
                                    
                                speed_prev = round(highest_score/10, 1)
                                
                                if(len(text_type.strip()) >= 8):
                                    text_widget.xview_scroll(8,'pixels')
                                k += 1
                                text_type += answer[k-1]
                                text_widget.tag_add("correct", f"1.0", f"1.{len(text_type)}")
                                text_widget.tag_config("correct", foreground="black")
                        else:
                            global choised_para, typed_para, timeremaining, difficulty
                            now = datetime.now()
                            now = now.strftime("%H:%M:%S")
                            time_end = datetime.strptime(str(now),"%H:%M:%S")
                            difference = time_end - time_start
                            timeremaining = difference.total_seconds() 
                            choised_para = answer
                            typed_para = answer
                            difficulty = "Easy"
                            win_car_game.destroy()
                            keyboard.unhook_all()
                            isworking = False
                            typing_result_page()
                            


                    # Register the key event listener
                try:
                    if(isworking):
                        keyboard.hook(key_event)
                        def update_car_position():
                            global carx,speed_curr, car2x, speed_prev, isCrossed, ismiddleroad, isfinishroad,road_startx,road_stripx,road_stripx2
                            
                            carx += speed_curr
                            car2x += speed_prev
                            
                            if carx > 1200:
                                carx = 80
                            if car2x > 1200:
                                car2x = 80

                            image_car.place(x=carx, y=300)
                            image_car2.place(x=car2x,y=420)
                            if(speed_curr>1):
                                speed_curr -=1
                        
                            if((carx >= 240 or isCrossed) or (isCrossed)):
                                if(not isCrossed):
                                    isCrossed = True
                                if(not ismiddleroad):
                                    btn_road.place(x=road_startx,y=250)
                                    road_startx -= speed_curr
                                if(road_startx <= -200 and not ismiddleroad):
                                    btn_road.config(image=img_road_middle)
                                    ismiddleroad = True
                                    btn_road.place(x=-20,y=250)
                                
                                if(ismiddleroad):
                                    btn_roadstrip.place(x=road_stripx,y=370)
                                    road_stripx -= speed_curr
                                    if(road_stripx == -500):
                                        road_stripx = 1700
                                    btn_roadstrip2.place(x=road_stripx2,y=370)
                                    road_stripx2 -= speed_curr
                                    if(road_stripx2 == -500):
                                        road_stripx2 = 1630
                                        
                                    
                                
                            win_car_game.after(100, update_car_position)

                        update_car_position()
                        win_car_game.mainloop()
                except:
                    pass
                
                
            main_game()

        def flappy_game(event):
            print("Flappy Bird run")
            try:
                command = ["python", r"C:\Users\hp\Desktop\Coding World\projects\flappy_bird.py"]
                subprocess.run(command, capture_output=True, text=True)
                # os.startfile(r"C:\Users\hp\Desktop\Coding World\projects\flappy_bird.py")
            except Exception as e:
                print(e)
        f2 = Frame(f1)
        image1_cargame = Label(f2, image=img_load1,cursor="hand2")
        image1_cargame.bind("<Button-1>", car_race_game)
        image1_cargame.pack()
        text1 = Label(f2, text='Type Racer',font="Helvetica 14 bold").pack()
        f2.pack(side='left', pady=10)

        f3 = Frame(f1)
        image1 = Label(f3, image=img_load2)
        image1.pack()
        image1.bind("<Button-1>", flappy_game)
        image1.pack()
        text1 = Label(f3, text='Catch The  Bird',font="Helvetica 14 bold").pack()
        f3.pack(side='left')

        f1.pack()
        win_game_mainpage.mainloop()

    def image_typing_performance(event):
        global stored_name,per_time,per_diff, canvas_widget, canvas
        per_time = 15
        per_diff = 'Easy'
        win_performance = Toplevel(root)
        win_performance.geometry("1850x570")
        win_performance.attributes('-alpha', 0.98)
        win_performance.state('zoomed')
        win_performance.config(bg="#d9d9d9")
        
        def load_data(ch = 0):
            global canvas_widget, fig, highest_score,per_time, per_diff, canvas
            sqliteConnection = sqlite3.connect('Database\\keySpeed.db')
            cursor = sqliteConnection.cursor()
            r_set=cursor.execute('''SELECT * from clientName''')
            # Create a Matplotlib figure and axis
            fig = Figure(figsize=(8, 6), dpi=100)
            ax = fig.add_subplot(111)
            
            l_y = []
            i = 0
            tot = 0
            highest_score = 0
            for data in r_set:
                if(per_diff == data[3] and per_time == int(data[2])):
                    tot += 1
                    if(int(float(data[1]))>highest_score):
                        highest_score = int(float(data[1]))
                    l_y.append(int(float(data[1])))
                
            if(tot>20):
                l_y = l_y[tot-14:]
            
            l2 = []
            h = 1
            for j in l_y:
                l2.append(h)
                h+=1

            # Data for the bar graph
            categories = l2
            values = l_y

            # Create the bar graph
            bars = ax.bar(categories, values)
            scores = l_y
            # Add scores as text labels on top of the bars
            for bar, score in zip(bars, scores):
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(score),
                        ha='center', va='bottom')
            if(ch == 1):
                canvas = FigureCanvasTkAgg(fig, master=frame3)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack()
        load_data()
        
        def combo_diff(event):
            global per_diff, canvas_widget
            per_diff = str(diff_Combo.get())
            canvas_widget.destroy()
            load_data(ch = 1)
        
        def combo_time(event):
            global per_time, canvas_widget
            per_time = int(str(time_Combo.get()))
            canvas_widget.destroy()
            load_data(ch = 1)
            
        global highest_score
        frame1 = Frame(win_performance,height=650,width=1000,bg="#F6F7FE",border=2)
        config.read('config.ini')
        stored_name = config['User']['username']
        head_label = Label(frame1, text=f"{stored_name}'s Performance",font="Courier 20 bold",bg="#ffffff")
        frame2 = Frame(frame1,height=200,width=950,bg="#F6F7FE")
        frame2_f1 = Frame(frame2,height=200,width=200,bg="#FCEFB4",padx=15)
        frame2_f2 = Frame(frame2,height=200,width=150,bg="#B5FEA3",padx=15)
        frame_showcase = Frame(frame2_f2,height=200,width=200,bg="#ffff0f",padx=15)
        diff_Combo = ttk.Combobox(frame_showcase,value = ['Easy','Medium','Hard'],state="readonly",font=('Times',16))
        diff_Combo.current(0)

        diff_Combo.bind("<<ComboboxSelected>>",combo_diff)
        
        time_Combo = ttk.Combobox(frame_showcase,value = ['15','30','45','60','120'],state="readonly",font=('Times',16))
        time_Combo.current(0)

        time_Combo.bind("<<ComboboxSelected>>",combo_time)
        highscore_label = Label(frame2_f1, text=f"Highest Score: {highest_score}",font=("Sans",20),bg="#B5FEA3")

        frame3 = Frame(frame1,height=200,width=950,bg="#F6F7FE",padx=15)
        load_data()
        canvas = FigureCanvasTkAgg(fig, master=frame3)
        canvas_widget = canvas.get_tk_widget()
        
        frame1.pack()
        head_label.pack()
        frame2.pack()
        frame2_f1.pack(side='left')
        highscore_label.pack()
        frame2_f2.pack(side='right')
        frame_showcase.pack()
        time_Combo.pack()
        diff_Combo.pack()
        frame3.pack()
        canvas_widget.pack()
        
    # Bind the click event to the label
    image1.bind("<Button-1>", image_typing_practice)
    image2.bind("<Button-1>", image_learn_typing)
    image3.bind("<Button-1>", image_typing_game)
    image4.bind("<Button-1>", image_typing_performance)
    root_frame.place(anchor='center', relx=0.5, rely=.5)

    win_main_page.mainloop()


open_img = ImageTk.PhotoImage(Image.open("Images\\open_buttn.png").resize((150,75)))
opn_btn = Button(f3,image=open_img,border=0,cursor="hand2",command=main_page)
opn_btn.pack(pady=10)

imagee1 = Label(f4, image=begin_image)
# imagee1.bind("<Button-1>", main_page)
imagee1.pack(side="left",padx=60,pady=20)

imagee2 = Label(f4, image=game_image)
# imagee2.bind("<Button-1>", main_page)
imagee2.pack(pady=20)

f4.pack()

# Use a window item to contain the frame
canvas.create_window((0, 0), window=root_frame, anchor="nw")

# Pack the Canvas and Scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Configure the Canvas to resize with the window
root.update()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()