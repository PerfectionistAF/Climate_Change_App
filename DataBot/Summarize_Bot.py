import os
import pandas as pd
from groq import Groq
import time

# Initialize Groq client with API key
client = Groq(api_key="")

def preprocess_input_data(data):
    """
    This function can preprocess the input data for LLM interpretation.
    """
    return data.lower().strip()

def generate_story_from_data(data):
    """
    This function generates a story-based summary from LLM.
    """
    preprocessed_data = preprocess_input_data(data)
    
    try:
        # Generate the summary
        chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": """You are a professional Data Analyst. Your responses should be data-driven, precise, and professional. Always ensure your analysis is clear, concise, and well-structured. Be objective, follow data analytics principles, and provide insights based on the given data.""",
        },
        {
            "role": "user",
            "content": f"""Summarize the data provided and present it in a narrative format: {preprocessed_data}
                            Focus on key metrics such as "Value_co2_emissions (metric tons per capita)" which indicates the carbon dioxide emissions per person in metric tons.
                            Highlight how high this value is compared to global standards, particularly noting that it exceeds the recommended amount set by the United Nations.
                            Provide your analysis in a professional, objective tone, and be clear in your data-driven conclusions.
                        """,
        }
    ],
    model="llama3-8b-8192",
)
        
        # Extracting the response correctly
        story_summary = chat_completion.choices[0].message.content
        return story_summary
    
    except Exception as e:
        print(f"Error generating story: {str(e)}")
        return None

def process_csv_data(file_path, row_limit=None, char_limit=None):
    """
    Reads and limits CSV data based on row or character limit.
    """
    df = pd.read_csv(file_path)
    
    if row_limit:
        df = df.head(row_limit)
    
    combined_data = ' '.join(df.astype(str).values.flatten())
    
    if char_limit and len(combined_data) > char_limit:
        combined_data = combined_data[:char_limit]
    
    return combined_data

def chunk_data(data, chunk_size=5000):
    """
    Splits data into smaller chunks based on the specified chunk size (characters).
    """
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def generate_story_from_csv(file_path, row_limit=None, char_limit=None, chunk_size=5000):
    """
    Processes CSV data, splits it into chunks, and generates a story for each chunk.
    """
    raw_data = process_csv_data(file_path, row_limit=row_limit, char_limit=char_limit)
    data_chunks = chunk_data(raw_data, chunk_size=chunk_size)

    all_stories = []
    
    for i, chunk in enumerate(data_chunks):
        print(f"Processing chunk {i+1}/{len(data_chunks)}...")
        story = generate_story_from_data(chunk)
        if story:
            all_stories.append(story)
        else:
            print(f"Error generating story for chunk {i+1}")
        
        # To avoid rate limit errors, wait for a short period between requests
        time.sleep(30)
    
    # Combine all chunked stories
    final_story = "\n\n".join(all_stories)
    return final_story


if __name__ == "__main__":
    csv_file_path = "./test-data.csv"
    row_limit = 100
    char_limit = 20000
    chunk_size = 5000
    
    # Generate the story from the CSV data
    story = generate_story_from_csv(csv_file_path, row_limit=row_limit, char_limit=char_limit, chunk_size=chunk_size)
    
    print(story)