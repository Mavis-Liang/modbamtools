import subprocess
samtools_output = subprocess.run(['samtools', 'view', 'gm12878_ul_sup_megalodon_HP_chr20.bam' '-H'], capture_output=True, text=True).stdout

SQ = samtools_output[samtools_output.startswith('@SQ')]

chroms = [i.split(':|\s+')[2] for i in SQ]
ends = [int(i.split(':|\s+')[4]) for i in SQ]

for chrom, end in zip(chroms, ends):
    print(chrom + ": 1 - " + str(end))





#modbamtools_cmd = ['modbamtools', 'length($0) > 5']
#ip = 'foo\nfoofoo\n'.encode('utf-8')
#result = subprocess.run(cmd, stdout=subprocess.PIPE, input=ip)
#result.stdout.decode('utf-8')