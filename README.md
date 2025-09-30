# Langsmith-496
## Langsmith Course Assignment - MAT496

This repository documents my progress through Modules 1 and 2 of the Langsmith course, fulfilling the requirements for video-by-video commits, learning summaries, and unique code examples.


## Module 1

### Lesson 1: Tracing Basics with @traceable
- **Learned:** How to utilize the `@traceable` decorator to easily trace standard Python functions, automatically creating a nested run structure visible in the Langsmith UI. This enables easy debugging and observability of custom components outside of standard LangChain Expression Language (LCEL).
- **Tweak:** Added **custom `name` and `metadata`** arguments to the `@traceable` decorators for the `retrieve_documents` and `generate_response` functions to enrich the trace data with context (e.g., retriever type and model name).
- **Source File:** [lesson1_tracing.ipynb](lesson1_tracing.ipynb) 
