import os
import yaml


with open("config.yml", "r") as f:
    conf = yaml.load(f, )

content_folder = "content"
for training in list(conf.keys()):
    training_name = training.replace("|todo", "")
    for i, lesson in enumerate(conf[training], start=1):
        markdown_text = ""
        for j, topic in enumerate(conf[training][lesson], start=1):
            # Header of topic
            markdown_text += f"### {i}.{j} {topic}\n"
            
            # Content of topic
            topic_content = ""
            potential_file_path = f"{content_folder}/{training_name}/{lesson}/{topic}.md"
            if os.path.isfile(potential_file_path):
                with open(potential_file_path, "r") as f:
                    file_content = f.read()
                topic_content += f"{file_content}\n"
            else:
                topic_content += "...\n\n"
        
            markdown_text += topic_content
        
        filepath = f"{training_name}/{i}. {lesson}.md"
        try:
            with open(filepath, "w") as f:
                f.write(markdown_text)
        except FileNotFoundError:
            os.mkdir(training_name)
            with open(filepath, "w") as f:
                f.write(markdown_text)

