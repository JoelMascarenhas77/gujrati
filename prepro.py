from inltk.inltk import tokenize
import re


stopwords_Gujrati = [
    "લેતા", "શા", "ઉભા", "હો", "હોઈ", "મા", "મૂકી", "નહી", "બધું", "હા", "મી", "એન", 
    "તું", "નો", "છો", "જી", "લેવા", "આર", "છીએ", "નં", "એવો", "હોવા", "તેથી", "નું", 
    "છ", "એવા", "એની", "થતાં", "જેવી", "બંને", "હશે", "માં", "ની", "હતાં", "તેવી", 
    "થયો", "એવી", "થી", "થયું", "ત્યાં", "બની", "ગયો", "છતાં", "આપી", "રહે", "તેઓ", 
    "પાસે", "તેમ", "ને", "તેને", "હું", "બાદ", "શકે", "જો", "અંગે", "રહી", "એમ", 
    "તેના", "કરે", "થઇ", "સુધી", "જાય", "રૂા", "કોઈ", "ના", "હવે", "તેની", "સામે", 
    "આવે", "બે", "થઈ", "ન", "જે", "આવી", "તા", "પર", "હોય", "હતું", "એ", "કરી", 
    "તે", "હતી", "માટે", "તો", "જ", "પણ", "કે", "આ", "અને", "છે"
]


def tokenize_and_filter(sentence):
    sentence = re.sub(r',.', '', sentence)
    
    tokens = tokenize(sentence, 'gu')  # Specify language as Gujarati
    filtered_tokens = []

    # First stage: Keep only tokens starting with "_"
    for token in tokens:
        if token.startswith("▁"):
            # Second stage: Strip the "_" and check for stop words
            cleaned_token = token.strip("▁")  # Clean token
            if cleaned_token not in stopwords_Gujrati:  # Filter out stop words
                filtered_tokens.append(cleaned_token)

    # Join the remaining tokens into a single string
    cleaned_string = " ".join(filtered_tokens)
    return cleaned_string