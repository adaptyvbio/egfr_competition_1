mmseqs easy-search sequences.fasta databases/swissprot swissprot.m8 tmp --format-output "query,target,fident,alnlen,mismatch,qcov,tcov"
mmseqs easy-search sequences.fasta databases/uspto uspto.m8 tmp --format-output "query,target,fident,alnlen,mismatch,qcov,tcov"
mmseqs easy-search sequences.fasta databases/thdpb thpdb.m8 tmp --format-output "query,target,fident,alnlen,mismatch,qcov,tcov"
mmseqs easy-search sequences.fasta databases/paper paper.m8 tmp --format-output "query,target,fident,alnlen,mismatch,qcov,tcov"