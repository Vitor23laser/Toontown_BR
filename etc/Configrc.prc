#
# constant config settings
#

chan-config-sanity-check #f
window-title Toontown
require-window 0
language portuguese
icon-filename toontown ico

cull-bin shadow 15 fixed
cull-bin shadow 14 fixed
cull-bin gui-popup 60 unsorted
default-model-extension .bam
plugin-path .
# downloader settings
decompressor-buffer-size 32768
extractor-buffer-size 32768
patcher-buffer-size 512000
downloader-timeout 15
downloader-timeout-retries 4
downloader-disk-write-frequency 4
downloader-byte-rate 125000
downloader-frequency 0.1
want-render2dp 1

# texture settings
max-texture-dimension 256
textures-power-2 down

# loader settings
load-file-type toontown
dc-file phase_3/etc/toon.dc
dc-file phase_3/etc/otp.dc
aux-display pandadx9
aux-display pandadx8
aux-display pandagl
aux-display tinydisplay
compress-channels #t
display-lists 0
text-encoding utf8
direct-wtext 0
text-never-break-before ,.-:?!;。？！、
early-random-seed 1

# 
# server type 
#
server-type dev
