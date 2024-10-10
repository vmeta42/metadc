# Copyright 2022-2023 The VNET Project Authors. All Rights Reserved.

# SPDX-License-Identifier: MIT

pull:
	docker pull meta42/metatoc-violas-config-generator
	docker compose -f compose/docker-compose.yaml pull
run:
	cd violas; make gen;
	docker compose -f compose/docker-compose.yaml up -d
stop:
	docker compose -f compose/docker-compose.yaml down
	rm -rf violas/etc
