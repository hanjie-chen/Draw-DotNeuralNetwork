# Makefile for neural network graph generation
# This Makefile is designed to work on both Unix-like systems and Windows

# Determine the operating system
ifeq ($(OS),Windows_NT)
    # Windows-specific settings
    PYTHON = python
    RM = del /Q
    CHECK_AND_RM = if exist $(1) del /Q $(1)
else
    # Unix-like system settings
    PYTHON = python3
    RM = rm -f
    CHECK_AND_RM = test -f $(1) && $(RM) $(1)
endif

# Script name
SCRIPT = dot_neuralnetwork_graph.py

# Default layers
layers ?= [3, 5, 4, 2]

# Phony targets
.PHONY: all clean help network.png

# Default target
all: network.png

# Generate the network graph
network.png: $(SCRIPT)
	$(PYTHON) $(SCRIPT) $(layers)

# Clean up generated files
clean:
	$(call CHECK_AND_RM,network.png)
	$(call CHECK_AND_RM,network.dot)

# Help target
help:
	@echo "Available targets:"
	@echo "  all                : Generate the neural network graph (default)"
	@echo "  clean              : Remove generated files"
	@echo "  help               : Show this help message"
	@echo ""
	@echo "Usage:"
	@echo "  make               : Use default layers [3, 5, 4, 2]"
	@echo "  make layers=[5,3,2,1] : Specify custom layers"
