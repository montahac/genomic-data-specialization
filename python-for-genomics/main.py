#!/usr/bin/python3

from fasta_utils import read_fasta, find_longest_orf, find_repeats, find_max_repeats, count_specific_repeats

def main():
    # Example usage for finding the longest ORF
    file_path = "dna2.fasta"  # Replace with the actual file path for the exam
    sequences = read_fasta(file_path)
    identifier = 'gi|142022655|gb|EQ086233.1|16'
    sequence = sequences.get(identifier)

    if sequence:
        longest_orf_length, longest_orf_start, longest_orf_end = find_longest_orf(sequence)
        print(f"Longest ORF length in sequence {identifier}: {longest_orf_length}")
        print(f"Starting position of longest ORF in sequence {identifier}: {longest_orf_start}")
        print(f"Ending position of longest ORF in sequence {identifier}: {longest_orf_end}")
    else:
        print(f"Sequence with identifier {identifier} not found.")

    # Example usage for finding the most frequent repeat of length 12
    repeat_length = 12
    repeat_counts = find_repeats(sequences, repeat_length)
    max_count, max_repeats = find_max_repeats(repeat_counts)

    print(f"Maximum number of copies of the most frequent repeat of length {repeat_length}: {max_count}")
    print(f"Number of different 12-base sequences that occur {max_count} times: {len(max_repeats)}")

    # Example usage for finding the most frequent repeat of length 7 from a specific list
    repeat_length = 7
    repeats_to_check = ["TGCGCGC", "CATCGCC", "CGCGCCG", "GCGCGCA"]
    repeat_counts = count_specific_repeats(sequences, repeat_length, repeats_to_check)

    # Find the repeat with the maximum number of occurrences
    max_repeat = max(repeat_counts, key=repeat_counts.get)
    max_count = repeat_counts[max_repeat]

    print(f"Repeat of length {repeat_length} with the maximum number of occurrences: {max_repeat}")
    print(f"Number of occurrences: {max_count}")

if __name__ == "__main__":
    main()