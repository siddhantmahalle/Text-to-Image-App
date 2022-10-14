import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk
from authtoken import auth_token

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline


class App(tk.Tk):
    def __init__(self, model_id: str, image_folder: str, auth_required: bool = False):
        super().__init__()
        self.guidance_scale_value = None
        self.geometry("532x730")
        self.title("Stable Bud")
        ctk.set_appearance_mode("dark")

        self.prompt = ctk.CTkEntry(self, height=40, width=512, text_font=("Arial", 20), text_color="black", fg_color="white")
        self.prompt.place(x=10, y=10)

        self.lmain = ctk.CTkLabel(self, height=512, width=512)
        self.lmain.place(x=10, y=210)

        self.model_id = model_id
        self.auth_required = auth_required

        self.trigger = ctk.CTkButton(self, height=40, width=120, text_font=("Arial", 20), text_color="white", fg_color="blue",
                                     command=self.generate)
        self.trigger.configure(text="Generate")
        self.trigger.place(x=206, y=150)

        self.slider_label = tk.Label(self, text="Guidance Value", font='Helvetica 14 bold')
        self.slider_label.place(x=10, y=80)

        self.current_value = tk.DoubleVar()

        self.slider = tk.Scale(self, from_=0.0, to=10.0, length=300, relief='solid', resolution=0.5, orient='horizontal',
                               command=self.set_guidance_value)
        self.slider.set(7.5)
        self.slider.place(x=360, y=90, anchor=tk.CENTER)

        self.device = "cuda"
        if self.auth_required:
            self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, revision="fp16", torch_dtype=torch.float16,
                                                                use_auth_token=auth_token)
            self.pipe.to(self.device)
        else:
            self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16)
            self.pipe.to(self.device)

        self.generated_image_loc = image_folder

    def generate(self):
        with autocast(self.device):
            prompt_entered = self.prompt.get()
            print(prompt_entered)
            print(f"Guidance Scale: {self.guidance_scale_value}")
            image = self.pipe(prompt_entered, guidance_scale=self.guidance_scale_value)["sample"][0]

        prompt_entered = prompt_entered.replace(",", "")
        prompt_entered = prompt_entered[:100]
        image.save(f'{self.generated_image_loc}/{prompt_entered}.png')
        img = ImageTk.PhotoImage(image)
        self.lmain.configure(image=img)

    def set_guidance_value(self, event):
        self.guidance_scale_value = self.slider.get()
        
