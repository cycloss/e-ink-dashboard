
.DEFAULT_GOAL := help
.PHONY: help playground

help: ## Show this help
# grep grabs target lines using a regex from the MAKEFILE_LIST which is the name of this file
# double dollar is required to escape a dollar sign (end of line in regex)
# FS is the field separator which is ':', 'anything', then '## '
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |\
	awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

hw-transfer-run: ## transfer and run the hello world test on the pi

hw-transfer: ## transfer the hello world test to the pi 

PROJECT_DIR = "~/dev/dashboard"

hw-run: ## run the hello world test on the pi
	ssh labrpi "python3 $(PROJECT_DIR)/hello-world.py"

demo: ## run the default demo on the pi
	ssh labrpi "python3 $(PROJECT_DIR)/ePaper/RaspberryPi_JetsonNano/python/examples/epd_3in7_test.py"	

playground: ## run playground
	python3 pg.py