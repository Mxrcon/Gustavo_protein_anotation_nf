nextflow.enable.dsl = 2

include { DOWNLOAD_GENOMES } from "./modules/download_genomes/download_genomes.nf"
include { PROKKA } from "./modules/prokka/prokka.nf"
include { EXPORT_PROTEINS } from "./modules/export_proteins/export_proteins.nf"


workflow {
    id_list_ch = Channel.fromList(params.genomes_ids)
    DOWNLOAD_GENOMES(id_list_ch)
    PROKKA(DOWNLOAD_GENOMES.out)
    EXPORT_PROTEINS(PROKKA.out.anotated_genome)
}
