docker-dev-start:
	docker compose -f docker-compose.dev.yml up --build -d
docker-dev-stop:
	docker compose -f docker-compose.dev.yml down
docker-prod-start:
	docker compose -f docker-compose.prod.yml up --build -d
docker-prod-stop:
	docker compose -f docker-compose.prod.yml down