import streamlit as st
import wikipedia


def load_wiki_summary(query: str) -> str:
    results = wikipedia.search(query)
    wikipedia.set_lang('ru')
    summary = wikipedia.summary(results[0], sentences=3)
    return summary


# Main app engine
if __name__ == "__main__":
    st.title("хелло ворлд")
    st.write("я сделала это (украла код) за 10 минут")
    st.write("")

    # display topic input slot
    topic = st.text_input("ВВЕДИТЕ ТИКЕР", "")

    # display article paragraph
    article_paragraph = st.empty()

    if topic:
        # load wikipedia summary of topic
        summary = load_wiki_summary(topic)

        # display article summary in paragraph
        article_paragraph.markdown(summary)


