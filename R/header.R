# header.R  : load everything required for general script processing

load(file.path(here::here(),"assets/psmObjects.rda"))


knitr::opts_chunk$set(echo=FALSE, warning=FALSE, message=FALSE)

library(tidyverse)
library(ggthemes)
library(phyloseq)
library(psmr)
library(knitr)
library(kableExtra)

theme_set( theme_light(base_family = "MarkPro"))
theme_set(theme_economist() +theme(axis.title.x=element_blank()))# + scale_colour_economist())


if (Sys.info()["sysname"] == "Darwin") {
    quartzFonts(Candara = quartzFont(rep("Candara", 4)), MarkPro = quartzFont(rep("MarkPro", 4)))
} else if (Sys.info()["sysname"] == "Windows") {
    windowsFonts(Candara = windowsFont("Candara"), MarkPro = windowsFont("MarkPro"))
} else {
    # Linux fallback: Use system default fonts
    options(device = "pdf")  # Set default graphics device to PDF
}
