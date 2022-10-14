from app_template import app

model_id = 'hakurei/waifu-diffusion'

if __name__ == "__main__":
    wikiart_app = app.App(model_id=model_id, image_folder='generated_images/waifu-diffusion', auth_required=False)
    wikiart_app.mainloop()
