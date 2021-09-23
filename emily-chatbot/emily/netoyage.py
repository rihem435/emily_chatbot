import spacy
text = """La vie humaine est remplie de toutes sortes d'émotions.
Différentes personnes gèrent leurs émotions de différentes manières.
Exprimer sa tristesse est nécessaire, tout comme son bonheur. 
Mais si vous gardez votre tristesse en vous pendant longtemps,
il devient vraiment difficile de vous en débarrasser.
Si vous partagez vos émotions tristes avec vos proches,
cela vous aidera à vous sentir moins mal.
Si vous cachez vos émotions tristes
et que vous ne savez pas comment les exprimer à votre partenaire, 
ces messages tristes vous aideront à exprimer clairement vos émotions.
Cela leur fera comprendre ce à quoi vous avez affaire par vous-même."""
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
token_list = [token for token in doc]
#print(token_list)

filtered_tokens = [token for token in doc if not token.is_stop]
#print(filtered_tokens)

lemmas = [
     f"Token: {token}, lemma: {token.lemma_}"
     for token in filtered_tokens
 ]

f=filtered_tokens[1].vector
print(f)