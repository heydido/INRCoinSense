echo ["$(date)"]: "Start"

echo ["$(date)"]: "Creating Python Environment"
conda create -p ./venv python=3.10 -y

echo ["$(date)"]: "Starting the Python Environment"
source activate ./venv

echo ["$(date)"]: "Installing Python Packages"
pip install -r requirements.txt

echo ["$(date)"]: "End"