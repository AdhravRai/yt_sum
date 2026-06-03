from langchain_core.prompts import ChatPromptTemplate


MAP_PROMPT = ChatPromptTemplate.from_template(
    """
    You are an expert note maker for students.

    Summarize the following transcript chunk.

    Transcript:
    {text}
    """
)


REDUCE_PROMPT = ChatPromptTemplate.from_template(
    """
    Create a coherent final summary from the following notes.

    Notes:
    {notes}
    """
)