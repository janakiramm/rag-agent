
# RAG-Agent

RAG-Agent is a framework for implementing Retrieval Augmented Generation (RAG) along with function calling to enhance response quality of LLMs.

## Overview

This repository contains code and examples for setting up and running RAG models. It includes:

- **API**: Tools and API interface for interacting with the structured data stored in MySQL.
- **Data**: Sample PDF representing unstructured data.
- **Notebooks**: Jupyter Notebooks demonstrating the implementation and use cases of RAG Agent.

## Getting Started

1. **Clone the repository**:
   ```
   git clone https://github.com/janakiramm/rag-agent.git
   ```
2. **Launch API Server**:
   ```
   bash start_api_server.sh
   ```
3. **Index the PDF**:
   Follow the instructions in `Index-Datasheet.ipynb`.

4. **Run the Agent**:
   Follow the instructions in `RAG-Agent.ipynb`.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
