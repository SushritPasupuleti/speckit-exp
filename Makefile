# Makefile for Qdrant setup

.PHONY: qdrant-up qdrant-down

qdrant-up:
	docker run -d --name qdrant \
	  -p 6333:6333 \
	  -p 6334:6334 \
	  qdrant/qdrant

qdrant-down:
	docker stop qdrant && docker rm qdrant
