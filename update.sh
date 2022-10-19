source venv/bin/activate
python automation/generate_toc.py
python automation/generate_content.py


git add -A
git commit -m "Just another update"
git push
