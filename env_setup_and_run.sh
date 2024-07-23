#!/bin/bash

# Update pip and install virtualenv if not already installed
echo "Updating pip and installing virtualenv..."
pip install --upgrade pip setuptools
#pip install virtualenv

# Navigate to your desired directory
#cd path_to_your_directory

# Create a new virtual environment
#echo "Creating virtual environment..."
#virtualenv myenv

# Activate the virtual environment
#echo "Activating virtual environment..."
#source myenv/Scripts/activate
#export PATH=$PATH:./ffmpeg/bin
pip install --upgrade pip setuptools


# Clone the NeMo repository
echo "Cloning NeMo repository..."
git clone https://github.com/NVIDIA/NeMo.git


# Create output directory and copy necessary files
echo "Setting up directory and copying files..."
mkdir -p outdir
cp utils.py data_setup.py cluster_diarizer.py ./NeMo
pip install -r requirements.txt

# Navigate into the NeMo directory
cd NeMo

# Modify exp_manager.py for compatibility
#echo "Modifying exp_manager.py for Windows..."
#sed -i 's/signal.SIGKILL/signal.SIGTERM/g' nemo/utils/exp_manager.py

# Install additional Python dependencies if needed
echo "Installing additional Python dependencies..."

# Install dependencies from requirements files
echo "Installing dependencies from requirements files..."
#pip install -r requirements/requirements_asr.txt
#pip install -r requirements/requirements.txt
pip install -r ../requirements.txt
#pip install torchvision
#pip install torchaudio
#pip install nemo_toolkit[asr]
#pip install omegaconf
#pip install hydra-core
#pip install pytorch-lightning
#pip install transformers
#pip install webdataset
#pip install sentencepiece datasets
#pip install IPython




# Run the data_setup.py script
#echo "Running data_setup.py..."
#python data_setup.py

# Run the cluster_diarizer.py script
#echo "Running cluster_diarizer.py..."
#python cluster_diarizer.py

echo "Setup and execution complete!"
