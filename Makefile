PROTO_PATH := ./proto
PROTO_FILES := $(wildcard $(PROTO_PATH)/*.proto)
OUTPUT := $(patsubst $(PROTO_PATH)/%.proto,%,$(PROTO_FILES))

default: $(OUTPUT)

% : $(PROTO_PATH)/%.proto
	mkdir -p $@
	python3 -m grpc_tools.protoc --proto_path=$(PROTO_PATH) $< --python_out=$@ --grpc_python_out=$@
	printf "import os\nimport sys\nsys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))" > $@/__init__.py

install:
	python3 -m pip install grpcio grpcio-tools

.PHONY: clean
clean:
	rm -rf $(OUTPUT)