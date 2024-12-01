# Personal Science Guide to the Microbiome

This is a Quarto project called "Personal Science Guide to the Microbiome" (I abbreviate it "PSM").  Think of it like a PhD thesis documenting years of experiments involving 16S microbiome tests on a variety of people. My project outputs in html, epub, docx, and pdf.

Many charts and tables are generated using R code and many custom R packages and data objects. Although most of the charts are still useful, the raw data is unlikely to ever need updating. For that reason, the processing scripts are frozen to R 4.3 and Quarto 1.5, with the whole environment locked into a docker container.

## Source documents

Everything necessary to generate the document is in the Github repo [personalscience/psm-quarto](https://github.com/personalscience/psm-quarto). The source for the dockerfile is in that repo under [docker-setup](https://github.com/personalscience/psm-quarto/tree/main/docker-setup).

A working version of the docker container is at:

[https://hub.docker.com/repository/docker/personalscience/psm-quarto/general](https://hub.docker.com/repository/docker/personalscience/psm-quarto/general)


## Make the documents from scratch

Connect to the local directory that contains the source documents.


```sh
docker run --rm -v "$(pwd):/data" -w /data psm-quarto:latest
```

The final html document will be at

file://docs/index.html


