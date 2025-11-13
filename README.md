# Personal Science Guide to the Microbiome

This is a Quarto project called "Personal Science Guide to the Microbiome" (I abbreviate it "PSM").  Think of it like a PhD thesis documenting years of experiments involving 16S microbiome tests on a variety of people. My project outputs in html, epub, docx, and pdf.

Many charts and tables are generated using R code and many custom R packages and data objects. Although most of the charts are still useful, the raw data is unlikely to ever need updating. For that reason, the processing scripts are frozen to R 4.3 and Quarto 1.5, with the whole environment locked into a docker container.

## Source documents

You should be able to generate this document using the files in this repo, plus the dockerfile  The source for the dockerfile [here](docker-setup/Dockerfile). 

A working version of the docker container is on dockerhub at:

[https://hub.docker.com/repository/docker/personalscience/psm-quarto/general](https://hub.docker.com/repository/docker/personalscience/psm-quarto/general)


## Make the documents from scratch

Connect to the local directory that contains the source documents.


```sh
docker run --rm -v "$(pwd):/data" -w /data psm-quarto:latest
```

You may need to do a ` docker tag personalscience/psm-quarto:latest psm-quarto:latest` before running that, if the names are not already set up.

After you run that Docker command the final html document will be at

file://docs/index.html


