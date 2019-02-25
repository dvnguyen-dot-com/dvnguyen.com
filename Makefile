build:
	pip install -e $(HOME)/code/src/github.com/nguyendv/gentor
	gentor build

serve:
	python -m http.server 8989 --directory public/
