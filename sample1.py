import os
import langextract as lx

# visualize file
visualize_file = "sample1.jsonl"
html_file = visualize_file.replace(".jsonl", ".html")

# Simple prompt
prompt = "Extract the city and country from the text."

# A few shot. Correct style examples
examples = [
    lx.data.ExampleData(
        text="Paris is the capital of France.",
        extractions=[
            lx.data.Extraction(
                extraction_class="location",
                extraction_text="Paris",
                attributes={"city": "Paris", "country": "France"}
            )
        ]
    ),
    lx.data.ExampleData(
        text="Berlin is the capital of Germany.",
        extractions=[
            lx.data.Extraction(
                extraction_class="location",
                extraction_text="Berlin",
                attributes={"city": "Berlin", "country": "Germany"}
            )
        ]
    )
]

# Input
input_text = "Rome is the capital city of Italy."

# Run extraction
result = lx.extract(
    text_or_documents=input_text,
    prompt_description=prompt,
    examples=examples,
    model_id="gpt-4o",  # auto-selects OpenAI GPT-4o
    api_key=os.environ.get("OPENAI_API_KEY"),
    fence_output=True,
    use_schema_constraints=False,
)

print(result)

# Save and visualize the results
lx.io.save_annotated_documents([result], output_name=visualize_file, output_dir=".")

# Generate the interactive visualization
html_content = lx.visualize(visualize_file)
with open(html_file, "w") as f:
    if hasattr(html_content, 'data'):
        f.write(html_content.data)  # For Jupyter/Colab
    else:
        f.write(html_content)
