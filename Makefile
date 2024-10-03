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

# Phony targets
.PHONY: all clean help

# Default target
all: network.png

# Generate the network graph
network.png: $(SCRIPT)
	$(PYTHON) $(SCRIPT)

# Clean up generated files
clean:
	$(call CHECK_AND_RM,network.png)
	$(call CHECK_AND_RM,network.dot)

# Help target
help:
	@echo "Available targets:"
	@echo "  all    : Generate the neural network graph (default)"
	@echo "  clean  : Remove generated files"
	@echo "  help   : Show this help message"
