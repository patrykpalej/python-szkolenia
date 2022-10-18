source venv/bin/activate
python generate_toc.py
python generate_content.py


git add -A
git commit -m "Just another update"
git push
