REMOTE_USER = krs
REMOTE_HOST = 46.8.141.9
REMOTE_PATH_LFDD = /home/krs/VK2TG/LFDD
REMOTE_PATH_ATMOS = /home/krs/VK2TG/Atmosfera
LOCAL_PATH = dist

build:
	pyinstaller run.py
	cp settings.ini $(LOCAL_PATH)/

clean:
	rm -rf build/ $(LOCAL_PATH)/ __pycache__/ *.spec

clean-lfdd:
	@echo "Removing _internal and run from server..."
	ssh $(REMOTE_USER)@$(REMOTE_HOST) "rm -rf $(REMOTE_PATH_LFDD)/_internal $(REMOTE_PATH_LFDD)/run"
	@echo "✅ _internal and run removed from server"

clean-atmos:
	@echo "Removing _internal and run from server..."
	ssh $(REMOTE_USER)@$(REMOTE_HOST) "rm -rf $(REMOTE_PATH_ATMOS)/_internal $(REMOTE_PATH_ATMOS)/run"
	@echo "✅ _internal and run removed from server"

deploy-lfdd:
	cd $(LOCAL_PATH)/run/ && \
    	scp -r ./_internal $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_PATH_LFDD)/ && \
    	scp ./run $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_PATH_LFDD)/

deploy-atmos:
	cd $(LOCAL_PATH)/run/ && \
    	scp -r ./_internal $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_PATH_ATMOS)/ && \
    	scp ./run $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_PATH_ATMOS)/
