clean:
	rm -rf extractedLetters
	rm model.hdf5
	rm labels.dat
download:
	python parser.py
extract-data:
	python Helpers/lettersExtractor.py
train-model:
	python TrainerModel.py
captcha-test:
	python main.py
server:
	gunicorn --bind 0.0.0.0:5000 webserver:main
