mkdir -p ~/.streamlit/
echo "\
base='dark'
primaryColor='#586e46'
textColor='#bbb'
secondaryBackgroundColor='#101c2c'
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" >> ~/.streamlit/config.toml
