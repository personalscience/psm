FROM rocker/r-ver:4.3.1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    libxml2-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    libfontconfig1-dev \
    libfreetype6-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev \
    zlib1g-dev \
    libgit2-dev \
    r-recommended \
    wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Quarto
RUN curl -fsSL https://github.com/quarto-dev/quarto-cli/releases/download/v1.6.39/quarto-1.6.39-linux-arm64.deb -o quarto.deb \
    && dpkg -i quarto.deb \
    && rm quarto.deb

# Set working directory
WORKDIR /usr/src/app

# Copy project files
COPY renv.lock .
COPY .Renviron .
COPY ./renv ./renv
COPY ./psmr ./psmr
COPY ./actino ./actino
COPY ./R ./R
COPY ./src ./src
COPY ./tinytex-0.54 ./tinytex-0.54
COPY installed_tex_packages.txt /usr/src/app/installed_tex_packages.txt

# Install renv and restore environment
RUN Rscript -e "install.packages('renv', repos='https://cran.rstudio.com')" \
    && Rscript -e "Sys.setenv(RENV_CONFIG_CACHE_SYMLINKS = FALSE); renv::restore()"

# Install TinyTeX and configure LaTeX
RUN Rscript -e "install.packages('tinytex', repos='https://cran.rstudio.com')" \
    && Rscript -e "tinytex::install_tinytex(force = TRUE)" \
    && Rscript -e "tinytex::tlmgr_install(readLines('/usr/src/app/installed_tex_packages.txt'))"

# Define working directory for dynamic host file mounts
WORKDIR /data

# Default command to render Quarto files
CMD ["quarto", "render", ".", "--output-dir", "docs"]
