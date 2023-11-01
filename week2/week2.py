#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Programming Lab II exercise 2"""

# A dictionary of genetic code to amino acid
standard_genetic_code: dict[str, str] = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S',
    'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y', 'GGG': 'G', 'GGA': 'G',
    'UGU': 'C', 'UGC': 'C', 'GGC': 'G', 'UGG': 'W', 'CUU': 'L', 'CUA': 'L', 
    'CUC': 'L', 'CUG': 'L', 'CCU': 'P', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 
    'CGA': 'R', 'CGG': 'R', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 
    'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 
    'GGU': 'G', 'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
    }

class RNA:
    def __init__(self, sequence: str) -> None:    
        """
        RNA class represents an RNA sequence.

        Args:
            sequence (str): RNA sequence string.
        """
        self.__sequence: str = sequence


    @property
    def sequence(self) -> str:
        """
        Returns the attribute sequence

        Returns:
            str: Sequence attribute
        """        
        return self.__sequence


class Protein:
    def __init__(self, rna_list: list[RNA]) -> None:
        """
        Protein class represents a protein sequence translated from an RNA sequence.

        Args:
            rna_instance (RNA): An instance of RNA class.
        """
        self.__rna_list: list[RNA] = rna_list
        self.__protein_sequences: list[str] = self._translate_rna_to_protein()


    @property
    def rna_list(self) -> list[RNA]:
        """
        Returns the attribute rna_list

        Returns:
            RNA: rna_list attribute
        """        
        return self.__rna_list
    
    @property
    def protein_sequences(self) -> list[str]:
        """
        Returns the attribute protein_sequence

        Returns:
            RNA: protein_sequence attribute
        """        
        return self.__protein_sequences


    def _translate_rna_to_protein(self) -> list[str]:
        """
        Translate RNA sequence to protein sequence using the standard genetic code.

        Returns:
            str: Translated protein sequence.
        """
        # An empty list to store proteins
        proteins: list[str] = []
        
        # List of RNA sequences
        sequences: list[RNA] = self.rna_list

        for sequence in sequences:
            
            # Get the sequence of the RNA instance
            seq: str = sequence.sequence

            # Initialize protein sequence
            protein: str = ''

            # A boolean value which will turn to True 
            # when the iteration hits a start codon
            building_protein: bool = False

            for start in range(0, len(seq), 3):

                # Get the triplets
                triplet: str = seq[start:start+3]

                # Check for start codon
                if triplet == 'AUG':
                    building_protein = True

                if building_protein and triplet in standard_genetic_code:
                    # Get the amino acid corresponding to the triplet
                    # from standard_genetic_code dictionary
                    amino_acid: str = standard_genetic_code[triplet]

                    if amino_acid == 'Stop':
                        # If the length of the sequence of amino acid
                        # is greater than or equal to 3 which is the 
                        # minimum number of amino acids a protein must have
                        # append the protein to the list
                        if len(protein) >= 3:
                            proteins.append(protein)
                        protein = ''
                        building_protein = False
                    else:
                        # Add the amino acid to the protein sequence
                        protein += amino_acid
        
        return proteins


class Fasta:
    def __init__(self, file_path: str) -> None:
        """
        Fasta class represents a FASTA file containing DNA sequences.

        Args:
            file_path (str): Path to the FASTA file.
        """
        self.__file_path: str = file_path

    @property
    def file_path(self) -> str:
        """
        Returns the attribute file_path

        Returns:
            str: file_path attribute
        """        
        return self.__file_path
    
    def _transcription(self, sequence:str) -> str:
        """
        Transcribes the given DNA sequence to RNA sequence

        Args:
            sequence (str): DNA sequence

        Returns:
            sequence (str): RNA sequence
        """        
        sequence = sequence.replace('T', 'U')
        return sequence


    def read_sequences(self) -> list[str]:
        """
        Reads a FASTA file and returns a list of DNA sequences.

        Returns:
            sequences (list[str]): List of DNA sequences.
        """
        path: str = self.file_path
        sequences: list[str] = []
        with open(path, 'r') as fasta_file:
            sequence: str = ''
            for line in fasta_file:
                line: str = line.strip()
                if line.startswith('>'):
                    # If a new sequence starts, append the current sequence to sequences list
                    if sequence:
                        sequences.append(sequence)
                    # Start a new sequence
                    sequence = ''
                else:
                    # Append sequence lines
                    sequence += line
            # Append the last sequence in the file to sequences list
            if sequence:
                sequences.append(sequence)

        # Return the list of DNA sequences
        return sequences
    
    def export_sequences(self, sequences: list[str]) -> list[RNA]:
        """
        Generates a list of RNA instances from list of DNA sequences

        Args:
            sequences (list[str]): A list of DNA sequences

        Returns:
            RNA_sequences (list[RNA]): A list of RNA instances
        """        
        
        RNA_sequences: list[RNA] = []
        for sequence in sequences:
            RNA_sequence: str = self._transcription(sequence)
            RNA_sequences.append(RNA(RNA_sequence))

        return RNA_sequences

