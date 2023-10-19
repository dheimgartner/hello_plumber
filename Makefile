.PHONY: test, format, requirements, start_api, build, build_clean

test:
	@pytest

format:
	@black hello_plumber/

requirements:
	@pipreqs --force

start_api:
	@Rscript -e "library(rapi); rapi::run()"

build:
	@bash scripts/build.sh

build_clean:
	@rm -rf _build