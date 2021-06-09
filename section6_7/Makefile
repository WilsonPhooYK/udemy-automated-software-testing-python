PATH_TO_FILE := /data.db

run-tests:
ifeq ($(clear-db), true)
	echo "Deleting data.db..."
	(del /f data.db) || (echo "\nFile already deleted";)

endif
	echo "Running app..."
	CMD /C start CMD /K python app.py
	timeout 2
	echo "Running postman tests..."
	CMD /C start CMD /K newman run postman/tests.postman_collection.json -e postman/tests.postman_environment.json
	