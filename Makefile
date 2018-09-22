# Clean build files
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	pip install -r requirements.txt