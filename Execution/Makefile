# Python version

PYTHON = python3

# Store functions

.PHONY = commands setup test run clean

FILES = input output

# Execute commands

.DEFAULT_GOAL = commands

commands:

	@echo "TYPE make setup TO SETUP THE PROJECT"
	@echo "TYPE make test TO TEST THE PROJECT"
	@echo "TYPE make run TO RUN PROJECT"

setup:
	
	@echo "-----Generating files-----"

	[ -d project_files.project ] || (echo "No directory found, please wait..." && mkdir project_files.project)
	for FILE in ${FILES}; do \
		touch "project_files.project/$${FILE}.txt"; \
	done
	
run:

	@${PYTHON} LowLatency_predict.py

# .project extension

clean:

	@rm -r *.project
