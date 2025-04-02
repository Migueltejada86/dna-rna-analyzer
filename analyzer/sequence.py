class SequenceAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def count_nucleotides(self):
        return {base: self.sequence.count(base) for base in 'ATCGU'}

    def gc_content(self):
        gc = self.sequence.count('G') + self.sequence.count('C')
        return round(gc / len(self.sequence) * 100, 2) if self.sequence else 0

    def transcribe(self):
        return self.sequence.replace('T', 'U')

    def translate(self):
        codon_table = {
            'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
            'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
            'UAA': '*', 'UAG': '*', 'UGA': '*'
        }
        rna_seq = self.transcribe()
        protein = ""
        for i in range(0, len(rna_seq) - 2, 3):
            codon = rna_seq[i:i+3]
            protein += codon_table.get(codon, '?')
        return protein

    def find_kmers(self, k):
        return [self.sequence[i:i+k] for i in range(len(self.sequence) - k + 1)]
