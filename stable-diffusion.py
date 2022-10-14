from app_template import app

model_id = 'CompVis/stable-diffusion-v1-4'

if __name__ == "__main__":
    wikiart_app = app.App(model_id=model_id, image_folder='generated_images/stable-diffusion', auth_required=True)
    wikiart_app.mainloop()
