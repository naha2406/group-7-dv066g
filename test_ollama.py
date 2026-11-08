
import csv
from ollama import chat

models = ["llama3.2", "gemma3:1b"]
prompt = "What is machine learning?"

with open("results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Model", "Prompt", "Response"])

    for model in models:
        print(f"Running {model}...")

        response = chat(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.message.content
        writer.writerow([model, prompt, answer])
        print(f"Finished {model}")

print("Results saved to results.csv")
