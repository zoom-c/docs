.docs-build-environment: Dockerfile
	docker build -t docs-build-environment .
	touch .docs-build-environment

shell: .docs-build-environment
	docker run -i -t -v $(PWD):/root -w /root docs-build-environment /bin/bash

html:
	./build.sh