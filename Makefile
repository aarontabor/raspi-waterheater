install:
	sudo pip install -r .requirements.txt
	sudo cp .S99.waterheater /etc/rc3.d/S99.waterheater
	sudo chmod +x /etc/rc3.d/S99.waterheater
