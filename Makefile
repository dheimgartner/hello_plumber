.PHONY: install_r_package, uninstall_r_package, test, format, requirements, start_api

install_r_package:
	@install_rapi

uninstall_r_package:
	@uninstall_rapi

test:
	@pytest

format:
	@black hello_plumber/

requirements:
	@pipreqs --force

start_api:
	@Rscript -e "library(rapi); rapi::run()"