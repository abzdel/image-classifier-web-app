install:	
	python -m pip install --upgrade pip && \
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203,W1202 *.py

format:
	black *.py
	black *.ipynb

check:
	pytest test_app.py