Bully_README
The bully checker evaluates if the comments are abusive or not.
Toxicities include: toxic, severe_toxic, obscene, threat, insult, identity_hate

Initially the text is preprocessed using “get_samples”,”get_stopwords”, “get_words_and_tags”, “get_data_profile”, “shorten_text”, “cleaning_text”, “text_preprocessor” functions.
We then used a predefined python detoxify function to detect the toxic behavior.

References:
https://www.kaggle.com/code/renokan/toxic-comments-get-predicts-by-detoxify-model/notebook
https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/data
