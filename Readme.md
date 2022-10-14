# Text to Image App

UI for creating images from text using these models.

* [Stable diffusion model](https://huggingface.co/CompVis/stable-diffusion-v1-4)
* [Waifu diffusion model](https://huggingface.co/hakurei/waifu-diffusion)
* [Wikiart model](https://huggingface.co/valhalla/sd-wikiart-v2)

## Usage

You will require user token from [huggingface.co](https://huggingface.co/settings/tokens) for Stable diffusion model

```
touch authtoken.py
```

Add  auth_token variable to `authtoken.py` and set it to your `huggingface` user token.

```
pip install -r requirements.txt 
python stable-diffusion.py 
```

You can also use other models 