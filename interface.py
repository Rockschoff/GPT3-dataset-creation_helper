from tkinter import *
from tkinter import ttk
from scrapper import scrape
from request import ApiCall
import os

def open_prompt():
    prompt_file = open("prompt.txt" , "r")
    text = prompt_file.read()

    scrapped_box.insert(END , text)
    prompt_file.close()

def scrapeNow():
    print(link_box.get("1.0" , END))
    links = link_box.get("1.0" , END).splitlines()
    for link in links:
        print(link.strip(" "))
    print(links)
    scrape(links)
    open_prompt()

def call_api():
    print('calling the api now')
    input_file = open("input_prompt.txt" , "w")
    input_file.write(final_box.get(1.0 , END))
    input_file.close()
    ApiCall()
    os.system("start EXCEL.EXE Response.xlsx")





root =Tk()
root.title("Scrapper")
root.geometry("700x700")
main_frame = Frame(root)
main_frame.pack(fill=BOTH , expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT , fill=BOTH , expand=1)

scroll_bar=ttk.Scrollbar(main_frame , orient=VERTICAL , command=my_canvas.yview)
scroll_bar.pack(side=RIGHT , fill=Y)

my_canvas.configure(yscrollcommand=scroll_bar.set)
my_canvas.bind("<Configure>" , lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

frame=Frame(my_canvas)

my_canvas.create_window((0,0) , window=frame , anchor="nw")


link_label = Label(frame , text="Add the links here")
link_label.pack()
link_box = Text(frame , height=20 , width = 90 , font=("Helvetica" , 9))
link_box.pack(pady=20)

scrape_button = Button(frame , text="Scrape Now" , command=scrapeNow )
scrape_button.pack()

scrapped_box = Text(frame , height=20 , width=90 , font=("Helvetica" , 9))
scrapped_box.pack(pady=10)

final_label=Label(frame , text="Final File is as follows")
final_label.pack()

api_button = Button(frame , text="Call the API" , command=call_api)
api_button.pack(pady=10)

final_box= Text(frame , height=20 , width=90 , font=("Helvetica" , 9))
final_box.pack(pady=10)

time_pass = Text(frame , height=2 , width=2)
time_pass.pack()



# https://www.realization.com/why-it-works

root.mainloop()