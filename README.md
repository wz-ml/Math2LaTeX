# Math2LaTeX
A open-source tool to convert Handwritten Math to LaTeX code!
## Samples

![image](https://github.com/leonlenk/LaTeX_OCR/assets/38673735/6a4c0574-aa68-4c68-a60c-d5ebe6ac46d1)

![image](https://github.com/leonlenk/LaTeX_OCR/assets/38673735/c439ed96-7bfa-4662-a3a2-52f54490464f)

_From top to bottom: Ground truth, predicted LaTeX._

On test samples from the CRHOME 2013 handwritten digit competition:

![image](https://github.com/leonlenk/LaTeX_OCR/assets/38673735/b212cbf4-162a-4e7d-96f8-3e2d90a3a70a)

![image](https://github.com/leonlenk/LaTeX_OCR/assets/38673735/55fa72d5-4937-4244-a193-74f7a5ae9c7e)

From a tablet handwritten validation image:

![image](https://github.com/leonlenk/LaTeX_OCR/assets/38673735/5e6d3823-643e-4fc4-afaf-b702b2bede7b)

![image](https://github.com/leonlenk/LaTeX_OCR/assets/38673735/df3bfb37-017f-4f6b-88f8-9b489819e99c)

## Features

- **Handwriting Recognition**: Uses a deep learning model trained on a large dataset of handwritten mathematical symbols and equations.
- **LaTeX Conversion**: Converts recognized handwriting into LaTeX code, ready to be used in your documents.
- **Open-Source**: All the details of our implementation can be found in this repository.

## Installation

To get started with Math2LaTeX, you'll need to have Python 3.6+ and PyTorch 1.0+ installed. To finetune your own model, follow the instructions below to set up the dataset.

2. Go to [Kaggle's Handwritten Mathematical Expressions](https://www.kaggle.com/datasets/rtatman/handwritten-mathematical-expressions) and download the dataset. Move `archive.zip` into the `Math2LaTeX` directory.
3. Run the following:
```python
conda create -n latexocr python==3.11
conda activate latexocr
pip install -r requirements.txt
bash ./setup.sh
```
You should see `all checks passed` after running `setup.sh`.
4. Images can be found in `img_data`, and image name / label pairs are in `img_data/labels.csv`.

## Todo:
- [x] BLIP baseline.
- [x] TrOCR experiments.
- [x] Handwritten text data for evaluation.
- [x] Pretrain on additional rendered latex data found at https://zenodo.org/api/records/56198/files-archive.

# Not yet implemented:
- [ ] RCNN + TrOCR segmentation-OCR pipeline.
- [ ] Model distillation and quantization.
- [ ] Rearrange code structure to a python package.

## Usage

To begin, run `train_TrOCR.ipynb` in `scripts`. Scroll down to the "Validation on REAL Handwritten Digits" header to run the model on your own validation images.

## Training the Model

Call `python scripts/train_TrOCR.py` with the `--gpu` flag to indicate which GPU to use. Default is 0.

## Contributing

Contributions to LaTeX-OCR are welcome! Whether it's bug reports, feature requests, or new code, we appreciate all help.
