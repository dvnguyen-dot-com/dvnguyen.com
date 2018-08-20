build:
	pip install -e ../gentor
	gentor build

serve:
	python -m http.server 8989 --directory public/
