import tkinter as tk
from threading import Thread
from tkinter import scrolledtext
from crawler import fetch_news,BbcSportsSpider,SkySportsSpider
from twisted.internet import reactor
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


def fetch_sky_sports_news():
    news_list = []
    thread = Thread(target=fetch_news, args=(SkySportsSpider, news_list))
    thread.start()
    thread.join()
    print(news_list)
    news_text_sky.delete(1.0, tk.END)
    for news in news_list:
        news_text_sky.insert(tk.END, f"Title: {news['title']}\nLink: {news['link']}\n\n")

def fetch_bbc_sports_news():
    news_list = []
    thread = Thread(target=fetch_news, args=(BbcSportsSpider, news_list))
    thread.start()
    thread.join()
    print(news_list)
    news_text_bbc.delete(1.0, tk.END)
    for news in news_list:
        news_text_bbc.insert(tk.END, f"Title: {news['title']}\nLink: {news['link']}\n\n")

# Create the main window
root = tk.Tk()
root.title("Sports News Crawler")

# Create the notebook (tab container)
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill='both')

# Sky Sports tab
sky_frame = ttk.Frame(notebook)
notebook.add(sky_frame, text="Sky Sports")

tk.Label(sky_frame, text="Sky Sports News").pack(padx=10, pady=10)
news_text_sky = scrolledtext.ScrolledText(sky_frame, height=20, width=80)
news_text_sky.pack(padx=10, pady=10)
fetch_sky_button = tk.Button(sky_frame, text="Fetch Sky Sports News", command=fetch_sky_sports_news)
fetch_sky_button.pack(pady=10)

# BBC Sports tab
bbc_frame = ttk.Frame(notebook)
notebook.add(bbc_frame, text="BBC Sports")

tk.Label(bbc_frame, text="BBC Sports News").pack(padx=10, pady=10)
news_text_bbc = scrolledtext.ScrolledText(bbc_frame, height=20, width=80)
news_text_bbc.pack(padx=10, pady=10)
fetch_bbc_button = tk.Button(bbc_frame, text="Fetch BBC Sports News", command=fetch_bbc_sports_news)
fetch_bbc_button.pack(pady=10)

# Run the main loop
root.mainloop()