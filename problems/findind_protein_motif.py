"""
Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of
ålocations in the protein string where the motif can be found.
"""

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def prot_motifs(filename):
    prot_ids = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            prot_ids.append(line)

    website = 'http://www.uniprot.org/uniprot/'
    ext = '.fasta'

    http = urllib3.PoolManager()

    seqs = {}
    for id in prot_ids:
        pos = []
        url = website + id + ext
        fasta = http.request('GET', url)

        data = fasta.data.decode('utf-8').split('\n')

        seq = read_data(data)
        for i in range(0, len(seq)-3):
            if seq[i] == 'N':
                if seq[i+1] != 'P':
                    if seq[i+2] == 'S' or seq[i+2] == 'T':
                        if seq[i+3] != 'P':
                            pos.append(i+1)

        if pos:
            seqs[id] = pos

    return seqs


def read_data(fasta):
    seq = ''
    for line in fasta:
        if line.startswith('>'):
            continue
        else:
            seq += line.rstrip('\n')

    return seq



if __name__ == '__main__':
    filename = input('Enter a file path')
    seqs = prot_motifs(filename)
    for k, v in seqs.items():
            print(k)
            print(*v)
