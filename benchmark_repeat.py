import csv
from statistics import mean
from ollama import chat

models = ["llama3.2", "gemma3:1b"]
prompt = "What is machine learning?"
results = []

options = {
    "temperature": 0,
    "num_predict": 150,
    "seed": 42
}

for model in models:
    print(f"\nWarming up {model}...")

    chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        options=options,
        keep_alive="10m"
    )

    speeds = []

    for run in range(1, 4):
        response = chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            options=options,
            keep_alive="10m"
        )

        seconds = response.eval_duration / 1_000_000_000
        tokens = response.eval_count
        speed = tokens / seconds if seconds > 0 else 0

        speeds.append(speed)
        results.append([
            model, run, round(seconds, 2),
            tokens, round(speed, 2)
        ])

        print(f"Run {run}: {speed:.2f} tokens/sec")

    print(f"Average: {mean(speeds):.2f} tokens/sec")

with open("benchmark_results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Model", "Run", "Inference Time (s)",
        "Output Tokens", "Tokens per Second"
    ])
    writer.writerows(results)

print("\nResults saved to benchmark_results.csv")
