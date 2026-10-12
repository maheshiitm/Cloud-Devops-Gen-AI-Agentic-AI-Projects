# Airbnb AI Trip Concierge 

This project is an Agentic AI architecture designed for the PM/TPM Module 2 assignment. It features a Supervisor Agent that orchestrates custom tools to handle traveler discovery, reservation modifications, and host communications.

## Architecture Highlights
* **Supervisor Router:** Analyzes user intent and routes to the appropriate deterministic or generative tool.
* **Policy RAG Tool:** A custom Langflow component that searches authoritative Airbnb cancellation policies and house rules.
* **Travel API Tool:** A mock deterministic API integration to calculate date shift pricing and check active reservation inventory.
* **Tech Stack:** Langflow, OpenAI (gpt-4o-mini), Python.

## Usage
Import `airbnb_concierge_flow.json` directly into a local Langflow instance to view the node architecture and test the compound queries in the Playground.
