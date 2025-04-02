from analyzer.sequence import SequenceAnalyzer

def main():
    print("Analizador de ADN/ARN")
    seq = input("Ingrese una secuencia de ADN o ARN: ").strip().upper()
    analyzer = SequenceAnalyzer(seq)

    print("\n--- Resultados ---")
    print("Conteo de nucleótidos:", analyzer.count_nucleotides())
    print("Contenido GC (%):", analyzer.gc_content())
    print("Transcripción a ARN:", analyzer.transcribe())
    print("Traducción a proteína:", analyzer.translate())

    k = int(input("\nIngrese valor de k para buscar k-mers: "))
    print("K-mers encontrados:", analyzer.find_kmers(k))

if __name__ == "__main__":
    main()
