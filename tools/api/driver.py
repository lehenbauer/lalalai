

import tkinter as tk
from tkinter import filedialog

import tkinter as tk

class MyGUI:
    def __init__(self, root):
        self.root = root
        self.stem_vars = {}
        self.backing_track_vars = {}
        self.elements = ['vocals', 'drum', 'bass', 'piano', 'electric_guitar', 'acoustic_guitar', 'synthesizer', 'voice', 'strings', 'wind']
        self.setup_gui()


    def setup_gui(self):
        self.root.title("Stem and Backing Track Extractor")

        tk.Label(self.root, text="Stems", font=("Helvetica", 14, "bold")).grid(row=0, column=0, sticky='w')
        tk.Label(self.root, text="Backing Tracks", font=("Helvetica", 14, "bold")).grid(row=0, column=1, sticky='w')

        for i, element in enumerate(self.elements):
            self.stem_vars[element] = tk.BooleanVar()
            tk.Checkbutton(self.root, text=element, variable=self.stem_vars[element]).grid(row=i+1, column=0, sticky='w')

        for i, element in enumerate(self.elements):
            self.backing_track_vars[element] = tk.BooleanVar()
            tk.Checkbutton(self.root, text=element, variable=self.backing_track_vars[element]).grid(row=i+1, column=1, sticky='w')

        self.filter = tk.IntVar()  # Initialize filter variable
        self.splitter = tk.StringVar()  # Initialize splitter variable

        # Filter options
        tk.Label(self.root, text="Filter", font=("Helvetica", 14, "bold")).grid(row=len(self.elements)+2, column=0, sticky='w')
        tk.Radiobutton(self.root, text="Mild", variable=self.filter, value=0).grid(row=len(self.elements)+3, column=0, sticky='w')
        tk.Radiobutton(self.root, text="Normal", variable=self.filter, value=1).grid(row=len(self.elements)+4, column=0, sticky='w')
        tk.Radiobutton(self.root, text="Aggressive", variable=self.filter, value=2).grid(row=len(self.elements)+5, column=0, sticky='w')

        # Splitter options
        tk.Label(self.root, text="Splitter", font=("Helvetica", 14, "bold")).grid(row=len(self.elements)+2, column=1, sticky='w')
        tk.Radiobutton(self.root, text="Phoenix", variable=self.splitter, value="phoenix").grid(row=len(self.elements)+3, column=1, sticky='w')
        tk.Radiobutton(self.root, text="Cassiopeia", variable=self.splitter, value="cassiopeia").grid(row=len(self.elements)+4, column=1, sticky='w')

        tk.Button(self.root, text='Run', command=self.run_program).grid(row=len(self.elements)+6, column=0, columnspan=2)

        self.filter.set(1)
        self.splitter.set("phoenix")

    def run_program(self):
        stems = [stem for stem, var in self.stem_vars.items() if var.get()]
        backing_tracks = [track for track, var in self.backing_track_vars.items() if var.get()]
        filter = self.filter.get()
        splitter = self.splitter.get()
        file_path = filedialog.askopenfilename()
        print(f'"{file_path}"')
        print("Stems: ", stems)
        print("Backing Tracks: ", backing_tracks)
        print("Filter: ", filter)
        print("Splitter: ", splitter)
        self.root.quit()

root = tk.Tk()
root.my_gui = MyGUI(root)
root.mainloop()

