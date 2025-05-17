# Academic Research Finder CLI

A command-line tool that uses Perplexity's Sonar API to find and summarize academic literature (research papers, articles, etc.) related to a given question or topic.

## Features

- Takes a natural language question or topic as input, ideally suited for academic inquiry.
- Leverages Perplexity Sonar API, guided by a specialized prompt to prioritize scholarly sources (e.g., journals, conference proceedings, academic databases).
- Outputs a concise summary based on the findings from academic literature.
- Lists the primary academic sources used, aiming to include details like authors, year, title, publication, and DOI/link when possible.
- Supports different Perplexity models (defaults to `sonar-pro`).
- Allows results to be output in JSON format.

## Installation

### 1. Install required dependencies

Ensure you are using the Python environment you intend to run the script with (e.g., `python3.10` if that's your target).

```bash
pip install requests
```
*(Note: `requests` is the primary dependency. Ensure your Python environment can execute it.)*

### 2. Make the script executable (Optional)

```bash
chmod +x research_finder.py
```
Alternatively, you can run the script using `python3 research_finder.py ...`.

## API Key Setup

The tool requires a Perplexity API key (`PPLX_API_KEY`) to function. You can provide it in one of these ways (checked in this order):

1.  **As a command-line argument:**
    ```bash
    python3 research_finder.py "Your query" --api-key YOUR_API_KEY
    ```
2.  **As an environment variable:**
    ```bash
    export PPLX_API_KEY=YOUR_API_KEY
    python3 research_finder.py "Your query"
    ```
3.  **In a file:** Create a file named `pplx_api_key`, `.pplx_api_key`, `PPLX_API_KEY`, or `.PPLX_API_KEY` in the *same directory as the script* or in the *current working directory* containing just your API key.
    ```bash
    echo "YOUR_API_KEY" > .pplx_api_key
    chmod 600 .pplx_api_key # Optional: restrict permissions
    python3 research_finder.py "Your query"
    ```

## Usage

Run the script from the `sonar-use-cases/research_finder` directory or provide the full path.

```bash
# Basic usage
python3 research_finder.py "What are the latest advancements in quantum computing?"

# Using a specific model
python3 research_finder.py "Explain the concept of Large Language Models" --model sonar-small-online

# Getting output as JSON
python3 research_finder.py "Summarize the plot of Dune Part Two" --json

# Using a custom system prompt file
python3 research_finder.py "Benefits of renewable energy" --prompt-file /path/to/your/custom_prompt.md

# Using an API key via argument
python3 research_finder.py "Who won the last FIFA World Cup?" --api-key sk-...

# Using the executable (if chmod +x was used)
./research_finder.py "Latest news about Mars exploration"
```

### Arguments

-   `query`: (Required) The research question or topic (enclose in quotes if it contains spaces).
-   `-m`, `--model`: Specify the Perplexity model (default: `sonar-pro`).
-   `-k`, `--api-key`: Provide the API key directly.
-   `-p`, `--prompt-file`: Path to a custom system prompt file.
-   `-j`, `--json`: Output the results in JSON format.

## Example Output (Human-Readable - *Note: Actual output depends heavily on the query and API results*)

```
Initializing research assistant for query: "Recent studies on transformer models in NLP"...
Researching in progress...

✅ Research Complete!

📝 SUMMARY:
Recent studies on transformer models in Natural Language Processing (NLP) continue to explore architectural improvements, efficiency optimizations, and new applications. Key areas include modifications to the attention mechanism (e.g., sparse attention, linear attention) to handle longer sequences more efficiently, techniques for model compression and knowledge distillation, and applications beyond text, such as in computer vision and multimodal tasks. Research also focuses on understanding the internal workings and limitations of large transformer models.

🔗 SOURCES:
  1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. Advances in neural information processing systems, 30. (arXiv:1706.03762)
  2. Tay, Y., Dehghani, M., Bahri, D., & Metzler, D. (2020). Efficient transformers: A survey. arXiv preprint arXiv:2009.06732.
  3. Beltagy, I., Peters, M. E., & Cohan, A. (2020). Longformer: The long-document transformer. arXiv preprint arXiv:2004.05150.
  4. Rogers, A., Kovaleva, O., & Rumshisky, A. (2020). A primer in bertology: What we know about how bert works. Transactions of the Association for Computational Linguistics, 8, 842-866. (arXiv:2002.12327)
```

## Limitations

-   The ability of the Sonar API to consistently prioritize and access specific academic databases or extract detailed citation information (like DOIs) may vary. The quality depends on the API's search capabilities and the structure of the source websites.
-   The script performs basic parsing to separate summary and sources; complex or unusual API responses might not be parsed perfectly. Check the raw response in case of issues.
-   Queries that are too broad or not well-suited for academic search might yield less relevant results.
-   Error handling for API rate limits or specific API errors could be more granular.
