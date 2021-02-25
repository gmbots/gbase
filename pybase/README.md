conda create -n myenv python=3.6
conda install numpy scipy pywin32 pillow opencv scikit-image
pyautogui python-mss pywinauto
conda config --add channels conda-forge
conda config --add channels anaconda
conda config --remove channels anaconda
conda env create -f environment.yml

conda config --show channels
conda env export > environment.yml
pip install msl-loadlib
conda remove --name myenv --all

pydirectinput
