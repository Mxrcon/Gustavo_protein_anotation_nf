nextflow.enable.dsl = 2

params.results_dir = "${params.outdir}/multifasta_proteins"
params.save_mode = 'copy'
params.should_publish = true

process EXPORT_PROTEINS {
    tag "${genomeName}"
    publishDir params.results_dir, mode: params.save_mode, enabled: params.should_publish

    input:
    tuple val(genomeName), path(gbkFile)

    output:
    path("*.fasta")

    script:

    """
    export_proteins.py ${gbkFile}
    """

    stub:

    """
    echo "export_proteins.py ${gbkFile}"
    touch ${genomeName}.fasta
    """
}
