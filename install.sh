#!/bin/bash
mkdir -p ~/bin
cat <<EOT > ~/bin/pplog
#!/bin/bash
cd "$PWD" && source env/bin/activate && python -m pplog "\$1"
EOT
chmod +x ~/bin/pplog
