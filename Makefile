venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

init:
	. venv/bin/activate; \
	FLASK_APP="src.application.app" \
	FLASK_DEBUG=True \
	flask init-db;

test:
	. venv/bin/activate; \
	pytest tests;

start:
	. venv/bin/activate; \
	FLASK_APP="src.application.app" \
	FLASK_DEBUG=True \
	flask run;
