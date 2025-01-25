# Summarize Media (WIP)

## What is this

Summarizes medias (like youtube videos etc), works for any audio

This repo contains the core logic of the application and a interactive demo at [main.ipynb](main.ipynb) (WIP)

## Installation

### Install ffmpeg (and add it to system PATH)

For linux (ubuntu):

```
sudo apt install ffmpeg
```

### Setup

First, create and activate new conda environment

```bash
conda create --name summarize-media python=3.12
conda activate summarize-media
```
V
Then, install the requirements

```bash
pip install -r requirements.txt
```

After that, clone the .env template and then fill in required API tokens

```bash
cp .env.example .env
nano .env
```

## Running the demo

Run all cells in [gradio_demo.ipynb](gradio_demo.ipynb), an interface (containing the demo) will pop up
