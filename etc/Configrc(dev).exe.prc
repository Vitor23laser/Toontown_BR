# This is the PRC configuration file for settings that are
# specific to developer instances of Toontown Online.

# Window settings
window-title Toontown

# Notify settings
console-output true

# Server settings
server-version tto-dev

# Developer settings
want-dev false
schellgames-dev false
exec-chat true
log-private-info true
want-qa-regression true

# Chat settings
want-whitelist false

# Audio settings
audio-library-name miles_audio

# Resources settings
vfs-mount phase_3.mf . 0
vfs-mount phase_3.5.mf . 0
vfs-mount phase_4.mf . 0
vfs-mount phase_5.mf . 0
vfs-mount phase_5.5.mf . 0
vfs-mount phase_6.mf . 0
vfs-mount phase_7.mf . 0
vfs-mount phase_8.mf . 0
vfs-mount phase_9.mf . 0
vfs-mount phase_10.mf . 0
vfs-mount phase_11.mf . 0
vfs-mount phase_12.mf . 0
vfs-mount phase_13.mf . 0

# DC file
dc-file etc/ttbr.dc

# RPC
want-rpc-server #f
rpc-server-endpoint http://0.0.0.0:1337/

# Code Redemption
want-code-redemption-mysql #f
want-code-redemption-init-db #t
code-redemption-self-test #f
want-unique-code-generation #t

# Parties
want-parties-mysql #f
want-parties-init-db #t
