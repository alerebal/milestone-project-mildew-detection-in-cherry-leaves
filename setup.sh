mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
base='dark'\n\
primaryColor='#586e46'\n\
textColor='#bbb'\n\
secondaryBackgroundColor='#101c2c'\n\
\n\
" > ~/.streamlit/config.toml
