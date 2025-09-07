# Makefile for Qdrant setup and running services

.PHONY: qdrant-up qdrant-down run-ui run-api run-all

qdrant-up:
	docker run -d --name qdrant \
	  -p 6333:6333 \
	  -p 6334:6334 \
	  qdrant/qdrant

qdrant-down:
	docker stop qdrant && docker rm qdrant

run-ui:
	cd frontend && streamlit run src/app.py

run-api:
	cd backend && uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

run-all: qdrant-up
	make run-api &
	make run-ui
