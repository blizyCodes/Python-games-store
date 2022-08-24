from tkinter import *
import backend


def get_selected_game(event):
    try:
        global selected
        index = list1.curselection()[0]
        selected = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected[1])
        e2.delete(0, END)
        e2.insert(END, selected[2])
        e3.delete(0, END)
        e3.insert(END, selected[3])
        e4.delete(0, END)
        e4.insert(END, selected[4])
    except IndexError:
        pass


def handle_view():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def handle_search():
    list1.delete(0, END)
    for row in backend.search(
        title_text.get(), developer_text.get(), year_text.get(), genre_text.get()
    ):
        list1.insert(END, row)


def handle_insert():
    backend.insert(
        title_text.get(), developer_text.get(), year_text.get(), genre_text.get()
    )
    list1.delete(0, END)
    list1.insert(
        END, (title_text.get(), developer_text.get(), year_text.get(), genre_text.get())
    )


def handle_delete():
    backend.delete(selected[0])


def handle_update():
    backend.update(
        selected[0],
        title_text.get(),
        developer_text.get(),
        year_text.get(),
        genre_text.get(),
    )


window = Tk()
window.wm_title("My Games DB by DonBlizy")

backend.play()
l1 = Label(window, text="Title:")
l1.grid(row=0, column=0)

l2 = Label(window, text="Developer:")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year:")
l3.grid(row=1, column=0)

l4 = Label(window, text="Genre:")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

developer_text = StringVar()
e2 = Entry(window, textvariable=developer_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

genre_text = StringVar()
e4 = Entry(window, textvariable=genre_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2, sticky=(N, W, E, S))

sb1 = Scrollbar(window, orient=VERTICAL)
sb1.grid(
    row=2,
    column=2,
    rowspan=6,
)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_game)
b1 = Button(window, text="View All", width=14, command=handle_view)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Game", width=14, command=handle_search)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Game", width=14, command=handle_insert)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected Game", width=14, command=handle_update)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=14, command=handle_delete)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close App", width=14, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()
