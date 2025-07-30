def chunk_text(text: str, chunk_size: int = 2000, overlap: int = 200) -> list:
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
        if start < 0:
            start = 0

    return chunks  # 🟢 this must be outside the loop


def chunked_summarize(text: str, summarize_func, max_chunk_size: int = 2000) -> str:
    text_chunks = chunk_text(text, chunk_size=max_chunk_size, overlap=200)

    partial_summaries = []
    for chunk in text_chunks:
        result = summarize_func(chunk)

        # Check the result type
        if isinstance(result, list) and isinstance(result[0], dict):
            summary = result[0]['summary_text']
        else:
            summary = result  # fallback if it's already a string

        partial_summaries.append(summary)

    combined_summary_input = " ".join(partial_summaries)
    final_result = summarize_func(combined_summary_input)

    if isinstance(final_result, list) and isinstance(final_result[0], dict):
        return final_result[0]['summary_text']
    else:
        return final_result
