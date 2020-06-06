import tkinter as tk
from tkinter import ttk
import tkfontchooser as tkf
import pymongo
import ssl
import dns

cluster = pymongo.MongoClient('mongodb+srv://user:user@cluster0-kiqxz.gcp.mongodb.net/test', 27017)
db = cluster['theguardian']
collection = db['articles']
collection.create_index([('author', 'text'), ('title', 'text')])

m = tk.Tk()
m.wm_title("The Guardian")
m.iconbitmap("icon.ico")
text = tk.StringVar()
name = tk.Label(m, text="Search")
label = tk.Label(m, text="Articles", font=("Arial", 30))
cols=("Author", "Title", "Link", "")
listBox = ttk.Treeview(m, selectmode='browse', columns=cols, show='headings')



def OnDoubleClick(item):
    a = tk.Toplevel(m)
    T = tk.Text(a)
    T.configure(font=tkf.Font(family="Helvetica", size=12))
    T.pack(expand=True, fill=tk.BOTH)
    c=str("Author : "+listBox.item(listBox.selection())['values'][0]
          +"\n\n Title : "+listBox.item(listBox.selection())['values'][1]
          +"\n\n Link : "+listBox.item(listBox.selection())['values'][2]
          +"\n\n Article : "+listBox.item(listBox.selection())['values'][3])
    T.insert(tk.END,c)
    tk.mainloop()

    print(listBox.item(listBox.selection())['values'])

def show():
    d=0
    keyword=text.get()
    results= collection.find({"$text": {"$search": keyword}})
    listBox.delete(*listBox.get_children())

    for i in results:
        d+=1
        if d<200:
            listBox.insert("", "end", values=(i['author'], i['title'], i['link'], i['article']))


listBox.heading("Author", text="Author")
listBox.column("Author", stretch=False, anchor=tk.W, width=150)

listBox.heading("Title", text="Title")
listBox.column("Title", stretch=True, anchor=tk.W)

listBox.heading("Link", text="Link")
listBox.column("Link", stretch=True, anchor=tk.W)

listBox.heading("", text="")
listBox.column("", width=0, stretch=False)

listBox.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
e1 = tk.Entry(m, textvariable=text, width=30).pack(side=tk.LEFT,expand=True,fill=tk.X)
m.grid_columnconfigure(0, weight=1)
showArticles = tk.Button(m, text="Show articles", width=15, command=show).pack(side=tk.LEFT)
listBox.bind("<Double-1>", OnDoubleClick)

m.mainloop()