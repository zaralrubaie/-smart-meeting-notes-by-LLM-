import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load tokenizer and model ONCE at startup
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    # Convert input text to tokens
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )

    # Generate summary
    summary_ids = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=100,
        min_length=20,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True,
        no_repeat_ngram_size=3
    )

    # Decode tokens back to readable text
    summary = tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
    )

    return summary

# Create Gradio interface
iface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=5, label="Input Text"),
    outputs=gr.Textbox(label="Summary"),
    title="DistilBART Summarizer",
    description="Summarize any input text using a pretrained DistilBART model."
)

# Launch the app
iface.launch()
