import re
import math
from collections import Counter


# Step 1. Helper functions



def clean_text(text):
    # remove URLs
    text = re.sub(r"http[s]?://\S+", "", text)
    # remove non-word characters
    text = re.sub(r"[^\w\s]", "", text)
    # normalize spaces
    text = re.sub(r"\s+", " ", text).strip()
    # lowercase
    return text.lower()

# iterate through the stopwords, and account for them
def remove_stopwords(words, stopwords):
    return [w for w in words if w not in stopwords]

# check the ending of the words for stemming & lemmatization
def stem_word(word):
    if word.endswith("ing") and len(word) > 4:
        return word[:-3]
    elif word.endswith("ly") and len(word) > 3:
        return word[:-2]
    elif word.endswith("ment") and len(word) > 5:
        return word[:-4]
    else:
        return word

# main function to call all helpers abover
def preprocess_document(docname, stopwords):
    with open(docname, "r") as f:
        text = f.read()

    # clean
    text = clean_text(text)

    # tokenize
    words = text.split()

    # remove stopwords
    words = remove_stopwords(words, stopwords)

    # apply stemming
    words = [stem_word(w) for w in words]

    # save to preproc_ file
    preproc_name = f"preproc_{docname}"
    with open(preproc_name, "w") as f:
        f.write(" ".join(words))

    return words


# # Step 2. TF-IDF computation

def compute_tf(words):
    counts = Counter(words)
    total = len(words)
    return {w: counts[w] / total for w in counts}

def compute_idf(all_docs):
    all_words = set().union(*all_docs)
    num_docs = len(all_docs)
    idf = {}
    for w in all_words:
        doc_count = sum(1 for d in all_docs if w in d)
        idf[w] = math.log(num_docs / doc_count) + 1
    return idf


# ---------------------------
# Step 3. Main script
# ---------------------------

def main():
    # Read file list
    with open("tfidf_docs.txt", "r") as f:
        docnames = [line.strip() for line in f if line.strip()]

    # Load stopwords
    with open("stopwords.txt", "r") as f:
        stopwords = set(line.strip() for line in f if line.strip())

    # Preprocess each document
    preprocessed_docs = []
    for doc in docnames:
        words = preprocess_document(doc, stopwords)
        preprocessed_docs.append(words)

    # Compute TF for each doc
    tf_list = [compute_tf(words) for words in preprocessed_docs]

    # # Compute IDF
    idf = compute_idf(preprocessed_docs)

    # Compute TF-IDF per doc and write top 5
    for i, doc in enumerate(docnames):
        tfidf_scores = {w: round(tf_list[i][w] * idf[w], 2) for w in tf_list[i]}
        sorted_scores = sorted(tfidf_scores.items(), key=lambda x: (-x[1], x[0]))
        top5 = sorted_scores[:5]

        out_name = f"tfidf_{doc}"
        with open(out_name, "w") as f:
            f.write(str(top5))


if __name__ == "__main__":
    main()
