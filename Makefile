install:	
	python -m pip install --upgrade pip && \
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203,W1202 *.py

format:
	black *.py
	black *.ipynb

check:
	#export FLASK_APP=app.py # i think i need to add this to the github actions runner to work as intended
	python -m pytest -vv --cov=src tests/*.py