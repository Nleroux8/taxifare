run_api:
	@uv run uvicorn api.fast:app

auth_docker:
	gcloud auth configure-docker ${GCP_REGION}-docker.pkg.dev

create_docker_repo:
	gcloud artifacts repositories create ${DOCKER_REPO_NAME} \
		--repository-format=docker \
		--location=${GCP_REGION} \
		--description="Repository for storing Docker images"

docker_build_local:
	@docker build -t ${DOCKER_IMAGE_NAME}:dev .

docker_run:
	@docker run -p 8001:8080 ${DOCKER_IMAGE_NAME}:dev
