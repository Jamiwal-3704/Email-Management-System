from transformers import pipeline

def generate_response(email_content):
    # Using BART for text generation
    nlp_model = pipeline('text2text-generation', model='facebook/bart-large-cnn')
    response = nlp_model(email_content, max_length=50, truncation=True)
    return response[0]['generated_text']
