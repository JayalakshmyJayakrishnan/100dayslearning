from difflib import SequenceMatcher

with open("doc1.txt") as firstfile, open("doc2.txt") as secondfile:
    file1 = firstfile.read()
    file2 = secondfile.read()

    ab = SequenceMatcher(None, file1, file2).ratio()
    result = int(ab*100)
    print(f"PLAGIARISM DETECTED {result*100}%.") 
