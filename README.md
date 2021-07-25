# Gustavo Poteins Nextflow pipeline

Um pipeline muito simples para baixar genomas do ncbi, anota-los com o prokka e exportar as proteínas anotadas e as proteínas hipotéticas detectadas com eles.

## Instalações requeridas
* [git](https://git-scm.com/downloads) 
* Java 8.0 ou superior
* [Docker](https://docs.docker.com/engine/install/ubuntu/)

OBS: teste a instalação do docker com:
```
    docker run hello-world
``` 

* Instalando Nextflow
```
curl -s https://get.nextflow.io | bash
sudo mv nextflow /usr/local/bin
```

## Rodando o pipeline

1. Acesse o site do NCBI em genomes e anote os códigos de acesso que você deseja submeter ao programa

`OBS: lembre-se de seguir o modelo apenas preenchendo com as informações que você obteve na sua pesquisa com o ncbi`

2. Clone o repositório em uma pasta com o seguinte comando: 
```
git clone https://github.com/Mxrcon/Gustavo_proteins_nf.git
```

3. Abra a pasta `Gustavo_proteins_nf ` recém criada e acesse o arquivo `params/params.yaml` e preencha os IDS que você deseja, seguindo o padrão de 1 id por linha na seguinte forma: `- "ID que você achou no ncbi"`
4. Dentro da pasta  `Gustavo_proteins_nf ` execute o seguinte comando:
```
nextflow run main.nf -params-file params/params.yaml
```
5. Aguarde a execução e abra a pasta criada com os outputs :smile:


