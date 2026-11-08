# group-7-dv066g / Assignment 1

## 1. Project Overview
In this assignment, we used Ollama and Python to run two language models locally
and compare their responses to the same prompt. We also compared the local
models with a commercial model (GPT-4o) using the same prompt. The goal was to
understand how to interact with local language models, save their responses to
a CSV file, and compare both answer quality and inference speed.

## 2. Models Used
We tested these two models, and both models were downloaded and run locally
using Ollama:
- Llama 3.2 (3B) developed by Meta
- Gemma 3 (1B) developed by Google

We also compared the results with one commercial model:
- GPT-4o (commercial, run via the ChatGPT web interface)

## 3. How to Run the Program
First, install Ollama from https://ollama.com
Then download the models by running the following commands in the terminal:
- `ollama pull llama3.2`
- `ollama pull gemma3:1b`

Install the Ollama Python library:
- `python -m pip install ollama`

Finally, run the Python script:
- `python test_ollama.py`

The program sends the same prompt to both local models and saves their
responses in a file called `results.csv`. The GPT-4o answer was added manually
to the same file using the same prompt.

- `python benchmark_repeat.py`

This script performs one warm-up run followed by three measured runs for each
model. The results are saved in `benchmark_results.csv`.

## 4. Prompt Used
We used the following prompt for all models:
“What is machine learning?”

## 5. Results and Observations
Both local models provided detailed explanations of machine learning. Their
answers were generally correct, but they differed in structure and level of
detail.

Llama 3.2 gave a structured and technical explanation. It described machine
learning concepts, applications, and challenges such as bias and explainability.

Gemma 3 gave a more conversational explanation with practical examples. It also
explained techniques such as linear regression, decision trees, and neural
networks.

**Content Comparison:**

| Aspect | Llama 3.2 (3B) | Gemma 3:1b | GPT-4o (commercial) |
|--------|----------------|------------|---------------------|
| Length | Long | Medium | Long |
| Style | Technical, structured | Conversational ("let's break it down") | Clear, well-structured with headings |
| Types of ML | Supervised / unsupervised / reinforcement | Supervised / unsupervised / reinforcement | Supervised / unsupervised / reinforcement |
| Algorithms named | Linear regression, decision trees, random forests, neural networks | Linear regression, decision trees, neural networks | Mentions AI vs ML vs DL table |
| Extra content | Benefits and challenges (data quality, bias, explainability) | Learning resources + follow-up question | Step-by-step example, real-world applications, comparison table |
| Correct? | Yes | Yes | Yes |
| Most precise / detailed? | No | No | **Yes** |

The commercial model (GPT-4o) gave a longer, better structured and more precise
answer than the local models. It used clear headings, a step-by-step
explanation, a comparison table (AI vs ML vs DL), and concrete real-world
examples. Gemma 3:1b was the shortest and most conversational and sometimes
asked follow-up questions instead of answering directly, while Llama 3.2 was
more complete but still less organized and less concise than GPT-4o.

## 6. Performance Evaluation
We also compared the inference performance of Llama 3.2 (3B) and Gemma 3 (1B)
using Python and Ollama. Both models were tested using the same prompt. The
following settings were used to make the comparison more consistent:
- Temperature: 0
- Seed: 42
- Maximum output tokens: 150
- One warm-up run before measurement
- Three measured runs per model

### Performance Results

| Measurement | Llama 3.2 | Gemma 3 |
|-------------|-----------|---------|
| Run 1 (tokens/sec) | 8.36 | 17.67 |
| Run 2 (tokens/sec) | 8.80 | 19.61 |
| Run 3 (tokens/sec) | 9.31 | 17.86 |
| Average speed (tokens/sec) | 8.82 | 18.38 |
| Average generation time (seconds) | 17.03 | 8.18 |

### Observations
The results show in our test that Gemma 3 generated tokens approximately twice
as fast as Llama 3.2. Gemma 3 also had a shorter average generation time. Each
model was tested three times after a warm-up run, and the results cannot be
generalized to all tasks or hardware since we used only one prompt.

This may partly be related to its smaller model size, although hardware and
other factors can affect performance. The results suggest that Gemma 3 was
faster in the local experiment. However, this doesn't mean it is always faster
or more accurate.

We also tested different machines using the same prompt and settings.

| Measurement | Llama 3.2 | Gemma 3 |
|-------------|-----------|---------|
| Run 1 (tokens/sec) | 6.65 | 12.59 |
| Run 2 (tokens/sec) | 6.46 | 13.36 |
| Run 3 (tokens/sec) | 6.48 | 13.12 |
| Average speed (tokens/sec) | 6.53 | 13.02 |
| Average generation time (seconds) | 22.98 | 11.52 |

The results of the second test, conducted using a different computer, were
lower but displayed the same pattern. Gemma 3 was able to generate tokens two
times faster than Llama 3.2 (1.99 and 2.08 times faster respectively in the
second and first test). It indicates that the speed difference depends more on
the size of the model than on the computer itself.

### Performance Results – Third Computer

| Measurement | Llama 3.2 | Gemma 3 |
|-------------|-----------|---------|
| Run 1 (tokens/sec) | 15.42 | 30.47 |
| Run 2 (tokens/sec) | 14.80 | 31.74 |
| Run 3 (tokens/sec) | 13.87 | 29.82 |
| Average speed (tokens/sec) | 14.69 | 30.67 |

The same Python programs were also tested on a third computer using the same
models, prompt and settings. Both programs worked without errors.

Gemma 3 was faster in all three runs with an average speed of 30.67 tokens/sec
compared to 14.69 tokens/sec for Llama 3.2. The absolute results were different
from the other computers, but Gemma 3 was still approximately twice as fast.

We did not measure token throughput for GPT-4o, since it was run through its
web interface rather than locally via Ollama. The comparison with the commercial
model is therefore qualitative (answer quality, structure, and detail), not a
speed benchmark.

Based on the qualitative comparison, the local models gave correct answers but
were shorter and less detailed than the commercial model. Gemma 3 sometimes
asked additional questions instead of giving a direct explanation, while GPT-4o
provided a more precise and better organized answer. The main advantage of the
local models is that they run for free, offline, and without API keys or data
transfer.

## 7. Conclusion
This experiment helped us understand how to run language models locally using
Ollama and Python. We also learned how to collect responses from different
models and save them to a CSV file for comparison, how to measure inference
performance, and how to compare token generation speeds.

Overall, the experiment showed that different language models can produce
useful but different responses to the same prompt. The speed difference between
the local models was consistent across three different computers: Gemma 3 (1B)
was approximately twice as fast as Llama 3.2 (3B), suggesting that model size is
the main factor. The commercial model (GPT-4o) produced the most precise and
best-structured answer, while the local models offer the advantage of running
free and offline. Differences in performance may be influenced by model size,
hardware, and other factors.
