def only_duplicates(st):
    dupes_only = ""
    for char in st:
        if st.count(char) > 1:
            dupes_only += char
    return dupes_only
