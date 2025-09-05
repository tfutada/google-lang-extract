import langextract as lx

# Define prompt and schema guidance
prompt = """
Extract medications with their dosage, route, and frequency. Use exact text, no paraphrasing.
Link each medication to its attributes clearly.
"""

examples = [
    lx.data.ExampleData(
        text="Administer 5 mg of lorazepam orally every 6 hours as needed.",
        extractions=[
            lx.data.Extraction(
                extraction_class="medication",
                extraction_text="lorazepam",
                attributes={
                    "dosage": "5 mg",
                    "route": "orally",
                    "frequency": "every 6 hours"
                }
            )
        ]
    )
]

# Input text to process
clinical_text = "Patient receives aspirin 100 mg by mouth daily."

# Run the extraction
result = lx.extract(
    text_or_documents=clinical_text,
    prompt_description=prompt,
    examples=examples,
    # model_id="gemini-2.5-pro",  # or another suitable model
    model_id="gemma2:2b",  # Automatically selects Ollama provider
    model_url="http://localhost:11434",
    fence_output=False,
    use_schema_constraints=False
)

# Save and visualize
lx.io.save_annotated_documents([result], output_name="med_extractions.jsonl", output_dir=".")
html = lx.visualize("med_extractions.jsonl")
with open("med_extractions.html", "w") as f:
    f.write(html.data if hasattr(html, "data") else html)
