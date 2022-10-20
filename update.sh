source venv/bin/activate
python automations/generate_toc.py
python automations/generate_content.py
python automations/yaml_to_json.py


git add -A
git commit -m "Just another update"
git push
