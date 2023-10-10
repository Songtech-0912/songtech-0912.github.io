+++
title = "Genetics & medicine notes"
date = 2023-10-02
+++

These notes contain the second unit of notes from BIO 1010 at RPI.

<!-- more -->

## DNA

**DNA** (deoxyribonucleic acid) contains all the instructions used to build a living organism. It is a molecular blueprint for a living organisms, organized in a double helix shape, and first discovered in 1953.

DNA is built of nucleotides - molecules that are like letters in the DNA alphabet. There are four nucleotides, A (adenine), C (cytosine), G (guanine) and T (thymine). Each nucleotide is composed of a phosphate group, sugar (deoxyribose) and nitrogenous base. Each "ladder" in the DNA helix contains two base pairs - A is complementary with T, and C is complementary with G.

Nucleotides can be (confusingly classified) into two categories:

- Purines: adenine and guanine (A, G)
- Pyrimidines: thymine and cytosine (C, T)

The most important functions of DNA include:

- The **storage** of genetic information
- The ability to **replicate** to facilitate cell division
- The ability to be translated into amino acids to create proteins
- Generate genetic variation by adding minor alterations to gene information over time

## Polarity of DNA

We can describe the direction of DNA by referring to its 5' and 3' ends. The 5' end is the direction of the phosphate attached to the 5th carbon of the sugar, whereas the 3' end is the direction of the free hydroxyl group attached to the 3rd carbon of the sugar.

## DNA replication

DNA replication always takes place in the 5' to 3' direction, and takes several steps:

- Proteins bind to locations on the DNA called origins of replication to form the **pre-replication complex**
- The two strands of DNA are separated
	- Helicase proteins untwist and unzip DNA along both directions of the origin using ATP as their energy source
	- Single-stranded binding proteins prevents DNA from degradation during replication
- Within the replication bubble (the unzipped region of DNA) DNA replication begins:
    - Single-stranded binding protein (SSBP) keeps replication bubble open
    - Primase starts a new stand of RNA primer (a nucleotide sequence that is complimentary to the DNA strand) in the 5' -> 3' direction
    - DNA polymerase III synthesizes DNA from the RNA primers by moving 5' -> 3'
    - Disconnected fragments of strands synthesized by DNA polymerase III are called Okazaki fragments and their RNA is replaced by DNA using DNA polymerase I
    - Ligase creates phosphodiester bonds between Okazaki fragments to link strands together into a continuous strand
    - DNA polymerase III uses proofreading to check for mismatched base pairs

| Protein | Function |
|---------|----------|
| DNA polymerase I | Replace RNA primer with DNA |
| DNA polymerase III | Extend RNA primers with DNA |
| Helicase | Separates strands of DNA |
| Primase | Makes RNA primers |
| Ligase | Seals gaps in DNA |

## Packaging DNA

The DNA of a single cell completely unwound would take up to 2 meters in length. Thus, DNA is tightly wound around proteins called histones that link together to form nucleosomes. These are then bound together, then looped and condensed to finally form chromosomes.

## Central Dogma of Biology

The **central dogma of biology** is that DNA transcribes to form RNA, RNA translates to form proteins.

## The genetic code

The genetic code is the set of rules that converts RNA base sequences to amino acid sequences that are used to make proteins. There are 20 amino acids, a fact first suggested by George Gamow. The code is based on sets of 3 nucleotides, called codons, and the code is redundant, meaning more than one codon can code for the same amino acid.

## Genes and genetic variation

A **gene** is a group of base sequences that code for specific amino acids that form proteins. A gene determines the phenotype (observable characteristics) of an organism and is heritable.

## Mutations

A **mutation** is a change in the nucleotide sequence of DNA caused by random chance. In some cases, it can be **base substitutions** - one nucleotide could be replaced with another. In other cases, it can be deletions or insertions, which can lead to significant changes in the amino acids sequence and correspondingly the proteins produced. For instance, a single base substitution causes sickle cell anemia.

## Transcription & Translation

- RNA polymerase copies DNA to mRNA (messenger RNA)
- mRNA heads outside the nucleus to ribosomes
- Using the mRNA transcript as template, tRNA molecules attach to it and link to amino acids, which are joined into a polypeptide
- The polypeptide is folded into a unique 3D shape to create a protein

### RNA vs. DNA

- RNA uses uracil instead of thymine
- RNA's single-stranded nature and 3D shape allows it to serve many different roles in cell functioning unlike DNA which has a single function

### Transcription

Each gene has a promoter sequence (which indicates where to start transcription), a terminator sequence (which indicates where to end transcription), and genetic instructions. Transcription begins near the promoter sequence. The RNA polymerase attaches to the promoter sequence, separates the strands of DNA, and then synthesizes the RNA by adding nucleotides that are complementary to the template strand of the DNA. Then, the RNA polymerase continues to move along the DNA until it reaches the terminator sequence.

| Term | Definition |
|---|---|
| Coding strand | The strand of DNA identical to the resulting RNA, with T substituted for U; it contains the promoter and terminator |
| Template strand | The strand of DNA complementary to the coding strand, which RNA polymerase reads off of |
| RNA polymerase | The protein that performs transcription |
| Transcription start site | The first nucleotide to be transcribed; located downstream from the promoter |
| mRNA | Messanger RNA; the RNA produced by transcription |
| Intron | Sections of the RNA that do not code for amino acids for a protein |

After transcription, what happens depends on the type of cell. In prokaryote cells, no further processing of the RNA is necessary; in eukaryote cells, a 5' cap, 3' tail is added, and introns are removed by the spliceosome, making the RNA mRNA, and the mRNA floats out of the nucleus and enters the cytoplasm.

Sometimes, genes undergo **alternative splicing**, which is when certain non-intron sequences are spliced out as well as introns, which allows changing the protein created during translation.

### Translation

Ribosomes attach to the ribosome binding sites on mRNA, and are used to synthesize polypeptides that make up proteins. To do this, they take 3-base sequences in RNA, called codons.  Molecules called tRNA help translate codons to amino acids. To do this, they have two ends:

- One end has a complementary sequence of 3-base sequences, called anticodons, which attach to the mRNA sequence
- The other end carries an amino acid corresponding to the codon

The first codon translated is always an AUG codon, known as the **start codon**. As the ribosome moves along the mRNA, it adds more amino acids together by creating peptide bonds to form a polypeptide. It stops once it reaches a **stop codon**. While being synthesized, polypeptides fold into a unique 3D shape, becoming a protein. The unique shape of a protein allows it to perform its function. 

The table of which codons match with which amino acids is known as a codon table, and is shown below:

![Codon table](https://www.researchgate.net/profile/Anders-Esberg/publication/267702580/figure/fig2/AS:661826920513537@1534803242980/The-codon-table-The-genetic-code-is-composed-of-four-different-letters-U-C-A-and-G.png)

(Source: ResearchGate)

### DNA repair

Every day, errors in DNA accumulate to up to a quintillion a day. DNA repairs are conducted by enzymes. For example, RNA polymerase can sometimes add mismatched bases, but other proteins conduct mismatch repair. Exposure to environmental toxins, UV radiation, etc. can cause chemical errors in DNA, which are fixed in a process called nucleotide excision repair.

## Human karyotype

Human has 23 pairs of chromosomes, 22 pairs of autosomal chromosomes and 1 pair of sex chromosomes.

## Mitosis vs Meiosis

Both mitosis and meiosis are types of cell replication. **Mitosis** produces genetically-identical diploid cells via chromosomal duplication, is a 4-stage process, and is used by all somatic (body) cells. **Meiosis** produces genetically-distinct haploid cells, is a 8-stage process, and is used by gametes (sperm and egg cells)


| Term | Definition |
|------|-----------|
| Homologous pair | A pair of chromosomes with the same size and similar genes (but often different sequences) |
| Diploid | Has both chromosomes from each homologous pair |
| Haploid | Has one chromosomes from each homologous pair |
| Ploidy | Whether a cell is haploid or diploid |


| Phase | Mitosis | Meiosis I | Meiosis II |
|-------|------|----|----|
| Prophase |  DNA condenses | DNA condenses, homologous pairs pair up & cross over | DNA condenses |
| Metaphase | Chromosomes move to the middle and line up | Homologous pairs move to middle and line up | Chromosomes move to middle and line up |
| Anaphase | Chromatids separate & move away from the middle | Homologous chromosomes move away from the middle | Chromatids separate & move away from the middle |
| Telophase | Cytokinesis to form 2 diploid daughter cells | Cytokinesis to form 2 diploid daughter cells | Cytokinesis to form 2 haploid daughter cells each (4 total) |


## Gene regulation

Every cell in the body has a copy of the **same genome**. But each cell has a different function. How do we explain that cells can do different things, if they all use the same genome? The answer is with **gene regulation**, which determines which genes are turned on and off and thus determines which proteins to be made, changing the function of a cell.

In bacteria, related genes can be placed together to form an **operon**, which share a promoter and terminator. 

Sugars are often used by cells as their source of energy. Lactose must be broken before being metabolized, whereas glucose can be metabolized directly. One common area of gene regulation for bacteria is in producing beta-galactosidase and beta-galactoside permease, two enzymes crucial in being able to transport break down lactose within bacteria. These enzymes are coded for in the _lac_ operon.

One form of gene regulation occurs in transcription. Transcription starts at the **promoter**, a region of DNA that RNA polymerase attaches to. Next to the promoter is the **operator**, a section of DNA to which a **repressor** protein can bind. When lactose is not present, the repressor binds to the operator and prevents the RNA polymerase from transcribing the operon. This represses the gene. When lactose is present, however, lactose binds to the repressor, and changes the shape of the repressor. This makes the repressor unable to bind to the operator, allowing the operon to be transcribed. Mutations in both the repressor and operator can interfere with this process.

Another form of gene regulation also occurs in transcription. Bacteria typically have a preference for glucose over lactose, but when glucose levels are low, levels of cyclic AMP (cAMP) molecule, an indicator of "hunger", increase. The promoter for the _lac_ operon is a **weak promoter**, which means RNA polymerase binds relatively weakly to the promoter. To counter this, there is an **activation site** before the promoter, which an **activator protein** can bind to, in order to make the weak promoter behave like a strong promoter. When cAMP levels are high, cAMP binds to the activator protein, allowing the activation protein to bind. Meanwhile, when cAMP levels are low, cAMP does not bind to the activator protein, preventing the activation protein from binding.

## Eukaryotic gene regulation

First, DNA is packed very tightly around histones and bundled in tight coils around chromosome. By keeping DNA tightly packaged, it cannot be transcribed, which suppresses genes.

Second, upstream (before) the promoter are DNA sequences called **enhancers**. Transcription factors are proteins that can bind to the enhancer to help RNA polymerase bind to the promoter. They can be considered analogous to activator proteins in prokaryotes.

## Homeobox genes

A fly's body has 3 sections - head, thorax, and abdomen. HOX (homeobox) genes are transcription factors that regulate the body plan of an embryo to grow along the head-tail direction. The expression of the HOX genes are crucial for many animals, not just flies - humans have it as well - to develop a proper body plan.

Many organisms share much of the same DNA. The reasons for this are:

- Descent from common ancestor
- Common cellular mechanisms across all organisms
- Key genes are conserved because mutations would reduce fitness

## Epigenetics

**Epigenetics** is the study of heritable changes in gene expression that do not involve changes to the underlying DNA sequence. That is, an organism's DNA (genome) can remain unchanged, but gene expression can change. The **epigenome** is how your genome is expressed. Epigenome is like "software" if genome is "hardware". Many factors can affect the epigenome:

- Methyl groups can attach to DNA and activate or repress gene expressions
- Acetyl groups can attach to histone packaging of DNA and make genes accessible
- Small RNA molecules can attach to genes and turn genes on and off

RNA interference is when intereference RNA (iRNA) molecules destroy mRNA become they reach ribosomes and causes translation to not occur. This is often used to prevent viral mRNA to prevent viruses from injection their DNA into a cell's DNA, thus protecting a cell from a virus. iRNA can be further divided into micro-interference RNA (miRNA), which can silence many genes, and short-interference RNA (siRNA), which silence specific genes.
