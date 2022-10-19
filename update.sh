source venv/bin/activate
python automations/generate_toc.py
python automations/generate_content.py


git add -A
git commit -m "Just another update"
git push
