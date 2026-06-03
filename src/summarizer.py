from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from src.prompts import MAP_PROMPT, REDUCE_PROMPT


llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

parser = StrOutputParser()


def generate_summary(transcript: str) -> str:

    document = Document(
        page_content=transcript,
        metadata={
            "source": "youtube"
        }
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )

    docs = splitter.split_documents([document])

    map_chain = (
        MAP_PROMPT
        | llm
        | parser
    )

    chunk_summaries = []

    for doc in docs:

        summary = map_chain.invoke(
            {
                "text": doc.page_content
            }
        )

        chunk_summaries.append(summary)

    combined_summary = "\n".join(
        chunk_summaries
    )

    reduce_chain = (
        REDUCE_PROMPT
        | llm
        | parser
    )

    final_summary = reduce_chain.invoke(
        {
            "notes": combined_summary
        }
    )

    return final_summary