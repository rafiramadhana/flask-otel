server: 
	python app.py

infra:
	docker compose up

stress:
	hey -n 20 -c 20 -m POST http://localhost:8080/books/purchase