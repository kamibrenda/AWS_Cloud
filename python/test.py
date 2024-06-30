preproinsulin_seq = """
ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
"""

# Remove unwanted characters
clean_seq = preproinsulin_seq.replace("ORIGIN", "").replace("//", "")
clean_seq = "".join(clean_seq.split()).lower()  # Remove spaces and newlines, convert to lowercase

# Write the cleaned sequence to a file
with open("preproinsulin-seq-clean.txt", "w") as file:
    file.write(clean_seq)

# Verify the file length
print(f"Length of preproinsulin-seq-clean.txt: {len(clean_seq)}")  # Should be 110
