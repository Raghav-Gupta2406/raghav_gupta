# Raghav-Gupta-Langsmith-496
## Langsmith Course Assignment - MAT496

This repository documents my progress through Modules 1 and 2 of the Langsmith course, fulfilling the requirements for video-by-video commits, learning summaries, and unique code examples.


 ## MODULE 1

 ### LESSON 1: Tracing Basics with @traceable
 - **Learned:** Learned how to manually instrument Python functions using the @traceable decorator to create a nested run tree. This process is essential for logging custom code components and ensuring full observability of a Groq-based RAG pipeline within Langsmith.
 - **Tweak:** Added custom name and descriptive metadata arguments (e.g., vectordb_type: FAISS, model_name: llama-3.3-70b-versatile) on the @traceable decorators for the core RAG functions to enrich the trace data with specific context.
 - **Source File:** [lesson1_tracing_basics.ipynb](lesson1_tracing_basics.ipynb) 

 ### LESSON 2: Types Of Runs
 - **Learned:** Learned to correctly classify traces using the run_type parameter (llm, retriever) which enables special rendering in Langsmith. Also learned how to implement the reduce_fn for streaming outputs.
 - **Tweak:** Implemented all missing run_type and reduce_fn arguments, modified the LLM input to a coffee order, and customized the Retriever document content/metadata to create a unique example.
 - **Source File:** [lesson2_TypesOfRuns.ipynb](lesson2_TypesOfRuns.ipynb) 

 ### LESSON 3: Alternative Ways To Trace
 - **Learned:** Learned to use the with trace() context manager for explicit control over trace inputs/outputs and learned that for LangChain-compatible providers, setting environment variables enables automatic tracing across all LLM calls.
 - **Tweak:** Removed the decorator from generate_response and implemented a custom with trace() block, adding the unique tag manual-context-manager to the trace, demonstrating precise manual control.
 - **Source File:** [lesson3_AlterWaysToTrace.ipynb](lesson3_AlterWaysToTrace.ipynb) 

 ### LESSON 4: Conversational Threads
 - **Learned:** Learned that conversational threads are tracked by passing a consistent, unique identifier (session_id, thread_id, or conversation_id) within the langsmith_extra metadata of sequential runs.
 - **Tweak:** Implemented conversation tracking by generating a Python uuid.uuid4() and passing this value as the conversation_id in the langsmith_extra parameter for both turns of the chat.
 - **Source File:** [lesson4_conversational_threads.ipynb](lesson4_conversational_threads.ipynb)


 ## MODULE 2

 ### LESSON 1: Datasets
 - **Learned:** Learned how to programmatically manage Langsmith Datasets using the langsmith.Client to perform a test-driven workflow. Specifically, utilized the client.create_dataset() method to initialize a new dataset and client.create_examples() for bulk uploading input/reference output pairs.
 - **Tweak:** The core tweak was to abandon the pre-existing dataset ID and use the SDK's client.create_dataset() method to programmatically create a new dataset with a unique name using uuid.uuid4(). This ensured the entire dataset creation and example upload process could be run end-to-end within the notebook.
 - **Source File:** [M2L1_Datasets.ipynb](M2L1_Datasets.ipynb)

 ### LESSON 2: Evaluators
 - **Learned:** Learned that LangSmith evaluators are functions that take a Run and an Example and return a Feedback object. We implemented LLM as Judge evaluation by defining criteria in a prompt and using a Pydantic schema for mandatory structured output.
 - **Tweak:** Replaced the proprietary OpenAI structured output method (client.beta.chat.completions.parse) with a Groq-compatible structured output chain using ChatGroq.with_structured_output. This allows us to maintain the LLM-as-Judge evaluation logic with structured data while adhering to the Groq LLM requirement.
 - **Source File:** [M2L2_Evaluators.ipynb](M2L2_Evaluators.ipynb)

 ### LESSON 3: Experiments
 - **Learned:** Learned to use langsmith.evaluate to systematically compare different versions of an application against a dataset. We ran experiments to compare two Groq models (Llama vs Mixtral) and confirmed how parameters like experiment_prefix, metadata, num_repetitions, and max_concurrency control the evaluation process.
 - **Tweak:** 1. Robust Dataset Fetching: Implemented logic to dynamically retrieve the name of the most recently created dataset using client.list_datasets() for stability. 2. Custom Constraint Evaluator: Created a new evaluator, is_three_sentences, to enforce the RAG system prompt's "three sentences maximum" rule, adding a layer of quality assurance to the experiment.
 - **Source File:** [M2L3_experiments.ipynb](M2L3_experiments.ipynb)

