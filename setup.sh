mkdir -p ~/.streamlit/
echo "[theme]\n\
base='dark'\n\
primaryColor='#586e46'\n\
textColor=#bbb'\n\
secondaryBackgroundColor='#101c2c'\n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
