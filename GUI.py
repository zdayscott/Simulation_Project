import tkinter as tk
from tkinter import ttk
import Backend


class GUI:

    def __init__(self, master):
        # fill in title, set default size to fulls screen
        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        master.state('zoomed')
        master.title("Tweet Simulator")
        master.configure(bg="#00008B")

        # create two frames(left/right) side of GUI
        self.inner_frame_width = (w/2) - (w/10)
        self.left_frame = tk.Frame(master, width= self.inner_frame_width, height=600, bg="#1E90FF", container=0)
        self.left_frame.configure(borderwidth=2, relief="ridge")
        self.left_frame.grid(row=0,column=0, padx=(w/20,0), sticky="wse", pady=(60,0))
        self.left_frame.grid_propagate(False)

        # right frame on page to contain output
        self.right_frame = tk.Frame(master, width= self.inner_frame_width, height=600, bg="#1E90FF")
        self.right_frame.configure(borderwidth=2, relief="ridge")
        self.right_frame.grid(row=0,column=1,sticky="wse", padx=(w/20,0), pady=(60,0))
        self.right_frame.grid_propagate(False)

        # small frame to hold user output
        output_width = 450
        self.output_frame = tk.Frame(self.right_frame, width = output_width, height = 300, bg="grey")
        self.pad_x = ((w/2) - (w/10)) - output_width
        self.output_frame.grid(row=0, column=0, padx = (self.pad_x / 2, self.pad_x / 2), pady = (30,0))
        self.output_frame.columnconfigure(0,weight=1)
        self.output_frame.grid_propagate(False)

        # label for output title inside output_frame
        self.tweet_title = tk.Label(self.output_frame, background="WHITE", text="Generated Tweet", anchor="center",relief="ridge")
        self.tweet_title.grid(row=0, column=0, sticky="nesw")

        # label for username
        self.user_name = tk.Label(self.output_frame, bg="white", text="User", anchor="w")
        self.user_name.grid(row=1, column=0, sticky="nesw")

        # string variable to hold tweet generated
        self.tweet_message = tk.StringVar()

        # label to display generated tweet inside output frame
        self.tweet_body = tk.Label(self.output_frame, bg="white", anchor="w", height=13, textvariable=self.tweet_message)
        self.tweet_body.grid(row=2,column=0, sticky="ew")

        # label to create border for output_form (to contain stars)
        self.tweet_border = tk.Label(self.output_frame, bg="white", anchor="w", height=7, relief="ridge")
        self.tweet_border.grid(row=3,column=0,sticky="ew")

        # create everything for the left frame

        # add entry area in left_frame
        pad_x = self.inner_frame_width
        self.entry = tk.Entry(self.left_frame, width=20)
        self.entry.grid(row=0, column=0, pady=(40, 0), padx=(0, pad_x / 2 + 70))

        # create scale for user
        self.opinion_scale = ttk.Scale(self.left_frame, length = 100, from_=1, to=5, orient="horizontal")
        self.opinion_scale.grid(row=1, column=0, pady=(5,0), padx=(pad_x/3,pad_x/3),sticky = "w")

        # small frame for checkboxes
        self.check_frame = tk.Frame(self.left_frame, width=200, height=300, bg="#1E90FF")
        self.check_frame.grid(row=2, column=0,pady=(30,0), padx=(pad_x/3,pad_x))

        # create modifier checkboxes
        self.var_1 = tk.StringVar()
        self.var_2 = tk.StringVar()
        self.var_3 = tk.StringVar()
        self.var_4 = tk.StringVar()

        # modifier 1
        self.mod_1 = tk.Checkbutton(self.check_frame, text="Person",variable = self.var_1, onvalue=("Person"), offvalue="")
        self.mod_1.grid(row=0, column=0, sticky="w")
        self.mod_1.configure(highlightthickness=0, bd=0, bg="#1E90FF")

        # modifier 2
        self.mod_2 = tk.Checkbutton(self.check_frame, text="Place",variable= self.var_2, onvalue="Word", offvalue="", bg="white")
        self.mod_2.configure(highlightthickness=0, bd=0, bg="#1E90FF")
        self.mod_2.grid(row=1, column=0, pady=(10,0), sticky="w")

        #modifier 3
        self.mod_3 = tk.Checkbutton(self.check_frame, text="Placeholder 3", variable= self.var_3, onvalue="Word3", offvalue="")
        self.mod_3.grid(row=2, column=0, pady=(10,0), sticky="w")
        self.mod_3.configure(highlightthickness=0, bd=0, bg="#1E90FF")

        # modifier 4
        self.mod_4 = tk.Checkbutton(self.check_frame, text="Placeholder 4", variable = self.var_4, onvalue="Word4", offvalue="")
        self.mod_4.grid(row=3,column=0, pady=(10,0), sticky="w")
        self.mod_4.configure(highlightthickness=0, bd=0, bg="#1E90FF")

        # submit button
        self.submit_button = ttk.Button(self.left_frame, text="Tweet", command=self.gen_tweet)
        self.submit_button.grid(row=4, column=0, padx=(0, pad_x / 2 + 50), pady=(10, 0))

        # init tweet contents
        self.tweet_content = "tweet"

    def get_user_data(self):
        print ("Entry: ", self.entry.get())
        print ("Hate bar: ", self.opinion_scale.get())
        print ("Modifier 1: ", self.var_1.get())
        print ("Mod 2: ", self.var_2.get())
        print ("Mod 3: ", self.var_3.get())
        print ("Mod 4: ", self.var_4.get())

    def gen_tweet(self):
        inp = [(self.entry.get(), self.opinion_scale.get(), self.var_1.get(), self.var_2.get())]
        self.tweet_content = Backend.TweetCreator(inp)
        self.display_tweet(self.tweet_content)

    # displays newly generated tweet in the tweet_body label
    def display_tweet(self, val):
        self.tweet_message.set(val)


if __name__ == '__main__':
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
