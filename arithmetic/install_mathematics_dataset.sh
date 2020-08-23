git clone https://github.com/deepmind/mathematics_dataset
cd mathematics_dataset
virtualenv venv -p python3.7
source venv/bin/activate
python setup.py install
python ../generate_arithmetic_dataset.py
