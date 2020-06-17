if [[ ! -d /home/user/venv/ ]];
then
	virtualenv /home/user/venv -p python3
	source /home/user/venv/bin/activate
fi
pip install -r requirements.txt
echo source /home/user/venv/bin/activate >> ~/.bashrc
