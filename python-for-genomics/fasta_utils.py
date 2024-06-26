#!/usr/bin/python3

from collections import defaultdict

def read_fasta(file_path):
    sequences = {}
    try:
        with open(file_path, 'r') as file:
            identifier = None
            sequence = []
            for line in file:
                line = line.strip()
                if line.startswith('>'):
                    if identifier:
                        sequences[identifier] = ''.join(sequence)
                    identifier = line[1:].split()[0]
                    sequence = []
                else:
                    sequence.append(line)
            if identifier:
                sequences[identifier] = ''.join(sequence)
    except Exception as e:
        print(f"Error reading file: {e}")
    return sequences

def find_orfs(sequence, frame=1):
    start_codon = 'ATG'
    stop_codons = ['TAA', 'TAG', 'TGA']
    seq_len = len(sequence)
    orfs = []
    for i in range(frame - 1, seq_len, 3):
        codon = sequence[i:i+3]
        if codon == start_codon:
            for j in range(i+3, seq_len, 3):
                codon = sequence[j:j+3]
                if codon in stop_codons:
                    orfs.append((i+1, j+3, j+3 - i))
                    break
    return orfs

def find_longest_orf(sequence):
    longest_orf_length = 0
    longest_orf_start = None
    longest_orf_end = None
    
    for frame in range(1, 4):
        orfs = find_orfs(sequence, frame)
        for start, end, length in orfs:
            if length > longest_orf_length:
                longest_orf_length = length
                longest_orf_start = start
                longest_orf_end = end
    
    return longest_orf_length, longest_orf_start, longest_orf_end

def find_repeats(sequences, repeat_length):
    repeat_counts = defaultdict(int)
    
    for sequence in sequences.values():
        seq_len = len(sequence)
        for i in range(seq_len - repeat_length + 1):
            repeat = sequence[i:i + repeat_length]
            repeat_counts[repeat] += 1
    
    return repeat_counts

def find_max_repeats(repeat_counts):
    max_count = max(repeat_counts.values())
    max_repeats = [repeat for repeat, count in repeat_counts.items() if count == max_count]
    return max_count, max_repeats

def count_specific_repeats(sequences, repeat_length, repeats_to_check):
    repeat_counts = defaultdict(int)
    
    for sequence in sequences.values():
        seq_len = len(sequence)
        for i in range(seq_len - repeat_length + 1):
            repeat = sequence[i:i + repeat_length]
            if repeat in repeats_to_check:
                repeat_counts[repeat] += 1
    
    return repeat_counts