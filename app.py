import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
#  Initialize tokenizer and model
# Tokenizer converts text into a numerical representation that the model can understand
model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
def summarize_text(text):
 # Tokenize input text
 tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

 inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
# Generate summary
 summary_ids = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=100,
        min_length=20,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True,
        no_repeat_ngram_size=3
    )
# decode will help to represent the ouptput as human understand language
 summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
 return summary
#  Launch Gradio Interface for Interactive Summarization
iface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=5, label="Input Text"),
    outputs=gr.Textbox(label="Summary"),
    title="DistilBART Summarizer",
    description="Summarize any input text using DistilBART fine-tuned model."
)
# Start the web interface

iface.launch()
