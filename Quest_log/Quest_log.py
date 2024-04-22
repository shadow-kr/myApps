import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Notebook, Style, Separator
import json

root = tk.Tk()
root.title("Quest log")
root.geometry("750x500")
file_for_task = "C:/Users/toshiba/Documents/my_Python_codes/Ressource/my_dictionary.json"

path_img = r"C:/Users/toshiba/Documents/my_Python_codes/Ressource/"


#---------------------------------------------------------->Variables
quest_dict = {}
print("---------->olddd : ",quest_dict)

new_key = "Empty"
new_value = "Empty"



#---------------------------------------------------------->frame
sidebar_frame = tk.Frame(root, bg="gray", width=200)
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)


listbox = tk.Listbox(sidebar_frame)

#---------------------------------------------------------->widgets
for dic_key in quest_dict.keys():
    listbox.insert(tk.END, dic_key)
listbox.pack(fill=tk.BOTH, expand=True)


label_content = tk.Label(root, text="", justify=tk.LEFT, font=("Arial", 20))
label_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


text_my_entry = tk.Entry(sidebar_frame, font=("Arial", 22), width=15, bg='#C5C6D0')

#---------------------------------------------------------->images

# label_icon    = tk.PhotoImage(file= path_img + "Settings - Option.png")

#---------------------------------------------------------->Functions

def show_variable_content():
    selected_index = listbox.curselection()

    if selected_index:
        index = int(selected_index[0])

        keys_list = list(quest_dict)   
        print("---------->keys_list : ", keys_list)
        try:
            print("---------->index : ",index)
            variable_name = keys_list[index]
            

            variable_content = quest_dict[variable_name]

            label_content.config(text=f"{variable_name} :\n\t {variable_content}")
        except Exception as error:
            print("Error : le dictionnaire est vide -->", error)



def add_quest():

    #--writing in text label
    listbox.insert(tk.END, text_my_entry.get())
    new_key = text_my_entry.get()

    #--add quest to dic
    quest_dict.update({new_key: new_value})

    #clean text label
    text_my_entry.delete(0, tk.END)

def add_quest_objectif():
    
    selected_index = listbox.curselection()

    if selected_index:
        new_dic_value = text_my_entry.get()

        dic_index = int(selected_index[0])
        keys_list = list(quest_dict)      

        key_id = keys_list[dic_index]
        quest_dict[key_id] = new_dic_value

        text_my_entry.delete(0, tk.END)

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)

        dic_index = int(selected_task_index)
        keys_list = list(quest_dict)      

        key_id = keys_list[dic_index]
        del quest_dict[key_id]

    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def write_file():
    
    file1 = open(file_for_task, "w")

    json.dump(quest_dict, file1)

    file1.close()
    print("Task saved to file")
    
def load_file():
    listbox.delete(0, tk.END)
    file1 = open(file_for_task, "r")
        
    loaded_dic = json.load(file1)
    quest_dict.update(loaded_dic)

    for value in quest_dict.keys() :

        listbox.insert(tk.END,value)

    file1.close()
    print("---------->newww : ",quest_dict)
    return   quest_dict

def cross_off_item():
    listbox.itemconfig(listbox.curselection(), bg="#3dad3f")
    listbox.selection_clear(0, tk.END)
    
#---------------------------------------------------------->Button




button_add_quest = tk.Button(sidebar_frame, text="add quest", command=add_quest, bg="#4CBB17", font=("arial", 10, "bold"))
button_add_quest_objectif = tk.Button(sidebar_frame, text="add quest objective", command=add_quest_objectif, bg="#4CBB17", font=("arial", 10, "bold"))

button_show = tk.Button(sidebar_frame, text="Show Content", command=show_variable_content, bg="#63C5DA", font=("arial", 10, "bold"))
cross_off_button = tk.Button(sidebar_frame, text="Cross Off Item", command=cross_off_item, bg="#7ADF20", font=("arial", 10, "bold"))




remove_button = tk.Button(sidebar_frame, text="Remove Task", command=remove_task, bg="#ED2939", font=("arial", 10, "bold"))

button_saving = tk.Button(sidebar_frame, text="save to file", command=write_file, bg="#FFB6C1", font=("arial", 10, "bold"))
button_load = tk.Button(sidebar_frame, text="load from file", command=load_file, bg="#FFB6C1", font=("arial", 10, "bold"))





# button_show.pack(anchor=tk.W, padx=15, pady=5, ipadx=40, fill='x')
button_show.pack( padx=15, pady=5, ipadx=10)
cross_off_button.pack(padx=15, ipadx=10)

text_my_entry.pack(pady=10)



button_add_quest.pack(anchor=tk.E, padx=10, pady=5, ipadx=40, fill='x')
button_add_quest_objectif.pack(anchor=tk.E, padx=10, pady=5, ipadx=40, fill='x')

remove_button.pack(anchor=tk.W, padx=10, pady=5, ipadx=40, fill='x')

button_saving.pack(anchor=tk.SE, padx=10, pady=5, ipadx=40, fill='x')
button_load.pack(anchor=tk.SE, padx=10, pady=5, ipadx=40, fill='x')





#---------------------------------------------------------->main
if __name__ == "__main__":
    root.mainloop()
