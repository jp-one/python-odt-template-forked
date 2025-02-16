# Use the base image from ghcr.io/unoconv/unoserver-docker
FROM ghcr.io/unoconv/unoserver-docker

# As root
USER root

ARG FONTS_FOLDER=/usr/share/fonts

# [Custom Font] Install custom fonts (copy font files)
# Place font files in the `./unoserver/customfonts` folder
# to ensure they are installed during the build process.
COPY unoserver/customfonts ${FONTS_FOLDER}/customfonts
RUN fc-cache -vf

# As worker
USER ${UID}
WORKDIR ${HOME}
