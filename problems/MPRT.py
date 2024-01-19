"""
Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of
ålocations in the protein string where the motif can be found.
"""
import sys, re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data

def read_data(fasta):
    seq = ''
    for line in fasta:
        if not line.startswith('>'):
            seq += line.rstrip('\n')            

    return seq

def prot_motifs(prot_ids):
    website = 'http://www.uniprot.org/uniprot/'
    ext = '.fasta'

    http = urllib3.PoolManager()

    seqs = {}
    for id in prot_ids:
        pos = []
        url = website + id[:6] + ext
        fasta = http.request('GET', url)

        data = fasta.data.decode('utf-8').split('\n')

        aa_seq = read_data(data)
        res = re.finditer(r'(?=(N[^P](S|T)[^P]))',aa_seq, re.I)
        pos = [match.start()+1 for match in res]

        if len(pos) > 0:
            seqs[id] = pos

    return seqs

# def prot_motifs(prot_ids):
#     # prot_ids = []
#     # with open(filename, 'r') as f:
#     #     for line in f:
#     #         line = line.replace('\n', '')
#     #         prot_ids.append(line)

#     website = 'http://www.uniprot.org/uniprot/'
#     ext = '.fasta'

#     http = urllib3.PoolManager()

#     seqs = {}
#     for id in prot_ids:
#         pos = []
#         url = website + id + ext
#         fasta = http.request('GET', url)

#         data = fasta.data.decode('utf-8').split('\n')

#         seq = read_data(data)
#         for i in range(0, len(seq)-3):
#             if seq[i] == 'N':
#                 if seq[i+1] != 'P':
#                     if seq[i+2] == 'S' or seq[i+2] == 'T':
#                         if seq[i+3] != 'P':
#                             pos.append(i+1)

#         if pos:
#             seqs[id] = pos

#     return seqs

if __name__ == '__main__':
    input_f = sys.argv[1]
    prot_seqs = ReadInput(input_f)

    pos = prot_motifs(prot_seqs)

    for k, v in pos.items():
            print(k)
            print(*v)
