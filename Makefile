SERVICE_NAME = SWProTelegramTopicsManager

.PHONY: start stop restart status enable disable logs

start:
	sudo systemctl start $(SERVICE_NAME)

stop:
	sudo systemctl stop $(SERVICE_NAME)

restart:
	sudo systemctl restart $(SERVICE_NAME)

status:
	sudo systemctl status $(SERVICE_NAME)

enable:
	sudo systemctl enable $(SERVICE_NAME)

disable:
	sudo systemctl disable $(SERVICE_NAME)

logs:
	journalctl -u $(SERVICE_NAME) -f

reload: 
	sudo systemctl daemon-reload

reforce: reload restart