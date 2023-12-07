#!/bin/bash
set -Eeuo pipefail

cat >README.md <<EOF
\`\`\`
$(./bench.sh)
\`\`\`
EOF
